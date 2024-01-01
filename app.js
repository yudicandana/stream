const { spawn } = require('child_process');
const moment = require('moment');

function streamVideo(videoPath, rtmpServer, streamKey, shouldLoop) {
    const rtmpUrl = `${rtmpServer}/${streamKey}`;

    const ffmpegArgs = [
        '-re',
        '-i', videoPath,
        '-c:v', 'libx264',
        '-b:v', '2500k',
        '-preset', 'fast',
        '-c:a', 'aac',
        '-b:a', '160k',
        '-f', 'flv',
        rtmpUrl
    ];

    const ffmpegProcess = spawn('ffmpeg', ffmpegArgs);

    ffmpegProcess.stderr.on('data', (data) => {
        const stderrLine = data.toString();
        if (stderrLine.includes('time=')) {
            const timeString = stderrLine.match(/time=\s*(\S+)/)[1];
            const duration = moment.duration(timeString);
            console.log(`Streaming... Time: ${duration.hours()}:${duration.minutes()}:${duration.seconds()}`);
        }
    });

    ffmpegProcess.on('close', (code) => {
        console.log(`Streaming finished with code ${code}.`);
        if (shouldLoop) {
            console.log('Restarting stream...');
            streamVideo(videoPath, rtmpServer, streamKey, shouldLoop);
        }
    });

    ffmpegProcess.on('error', (err) => {
        console.log(`Error: ${err.message}`);
    });
}

const videoPath = 'downloaded_video.mp4';
const rtmpServer = 'rtmp://push-spe.lvb.shopee.co.id/live/';
const streamKey = 'id-live-819315668719122-54588066?speSecret=b4e6b7793271db2522785f4da4faad32&speTime=65972F2F&pushDomain=push-spe.lvb.shopee.co.id&cdnID=SHOPEE&session_id=54588066';
const shouldLoop = true;

streamVideo(videoPath, rtmpServer, streamKey, shouldLoop);

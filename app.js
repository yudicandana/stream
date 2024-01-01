const ffmpeg = require('fluent-ffmpeg');
const moment = require('moment');

// Fungsi untuk streaming video ke RTMP server
function streamVideo(videoPath, rtmpServer, streamKey, shouldLoop) {
    const rtmpUrl = `${rtmpServer}/${streamKey}`; // Menggabungkan server dan kunci menjadi URL lengkap
    const stream = ffmpeg(videoPath)
        .format('flv') // Menggunakan format FLV untuk streaming
        .videoCodec('libx264') // Menggunakan codec x264
        .audioCodec('aac') // Menggunakan codec audio AAC
        .on('start', (commandLine) => console.log(`Started: ${commandLine}`)) // Log saat mulai streaming
        .on('stderr', (stderrLine) => {
            if (stderrLine.includes('time=')) {
                const timeString = stderrLine.match(/time=\s*(\S+)/)[1];
                const duration = moment.duration(timeString);
                console.log(`Streaming... Time: ${duration.hours()}:${duration.minutes()}:${duration.seconds()}`);
            }
        })
        .on('error', (err, stdout, stderr) => {
            console.log(`Error: ${err.message}`);
            console.log('FFmpeg STDOUT:', stdout);
            console.log('FFmpeg STDERR:', stderr);
        })
        .on('end', () => {
            console.log('Streaming finished.');
            if (shouldLoop) {
                console.log('Restarting stream...');
                streamVideo(videoPath, rtmpServer, streamKey, shouldLoop); // Memulai kembali streaming jika loop diaktifkan
            }
        })
        .outputOptions('-preset veryfast') // Opsi enkoding untuk performa
        .outputOptions('-crf 25') // Opsi enkoding untuk kualitas
        .outputOptions('-flvflags no_duration_filesize') // Opsi khusus untuk FLV
        .output(rtmpUrl) // URL RTMP server tujuan
        .run(); // Jalankan streaming
}

// Path ke file video Anda
const videoPath = 'a.mp4';

// Server RTMP dan kunci stream
const rtmpServer = 'rtmp://push-spe.lvb.shopee.co.id/live/';
const streamKey = 'id-live-819315668719122-54586242?speSecret=43fda0fc853344c0a6a7e9edd6ebe10e&speTime=65970E62&pushDomain=push-spe.lvb.shopee.co.id&cdnID=SHOPEE&session_id=54586242';

// Opsi Loop: true untuk loop, false untuk tidak
const shouldLoop = false; // Atur ini sesuai kebutuhan

// Memulai proses streaming
streamVideo(videoPath, rtmpServer, streamKey, shouldLoop);

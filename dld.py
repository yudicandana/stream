import subprocess
import time

def download_m3u8_video(m3u8_url, output_file, max_retries=3, wait_time=5):
    retry_count = 0
    success = False

    while retry_count < max_retries and not success:
        try:
            # Membangun perintah FFmpeg dengan level log debug
            command = [
                "ffmpeg",
                "-user_agent", "Mozilla/5.0",
                "-loglevel", "debug",  # Level log yang lebih rinci
                "-i", m3u8_url,
                "-c", "copy",
                "-bsf:a", "aac_adtstoasc",
                output_file
            ]

            # Menjalankan perintah FFmpeg dan menangkap outputnya
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            # Anda bisa melakukan parsing stdout atau stderr di sini untuk mendapatkan info detail
            # Misalnya, mencari kata 'error' atau informasi spesifik lainnya

            if process.returncode == 0:
                print(f"Video berhasil diunduh ke {output_file}")
                success = True
            else:
                raise subprocess.CalledProcessError(process.returncode, command)

        except subprocess.CalledProcessError as e:
            print(f"Percobaan {retry_count + 1} gagal: {e}")
            retry_count += 1
            if retry_count < max_retries:
                print(f"Menunggu {wait_time} detik sebelum mencoba kembali...")
                time.sleep(wait_time)

    if not success:
        print("Gagal mengunduh video setelah beberapa percobaan.")

# Meminta pengguna memasukkan URL M3U8
url_m3u8 = input("Masukkan URL M3U8: ")

# Lokasi dan nama file output
output_video = "downloaded_video.mp4"

# Memanggil fungsi untuk mendownload video
download_m3u8_video(url_m3u8, output_video)

Persyaratan Sistem
Node.js
NPM (Node Package Manager)
FFmpeg
Langkah Instalasi
Instal Node.js dan NPM:


Windows: Anda bisa mengunduh FFmpeg dari situs web FFmpeg dan mengikuti instruksi pemasangan.
macOS: Gunakan Homebrew dengan perintah brew install ffmpeg.

Linux: Biasanya tersedia di repositori sistem. Gunakan manajer paket seperti apt atau yum. Contoh: sudo apt-get install ffmpeg.
Setup Proyek:
Buat folder baru untuk proyek Anda.
Buka terminal atau command prompt, dan navigasikan ke folder proyek (cd path/to/your/folder).
Jalankan npm init dan ikuti instruksi untuk membuat file package.json.
Instal Paket Node.js yang Diperlukan:

Dalam folder proyek Anda, jalankan perintah berikut untuk menginstal fluent-ffmpeg dan moment:

npm install fluent-ffmpeg moment


Cara Penggunaan
Tambahkan Kode Aplikasi:

Salin kode aplikasi streaming ke file JavaScript di dalam folder proyek Anda, misalnya app.js.
Konfigurasi Alat Streaming:

Edit file app.js untuk mengatur videoPath, rtmpServer, dan streamKey sesuai kebutuhan Anda.

Atur shouldLoop menjadi true untuk loop video, atau false untuk memutarnya sekali saja.
Menjalankan Alat Streaming:

Buka terminal atau command prompt.
Navigasikan ke direktori proyek Anda.
Jalankan alat streaming dengan perintah node app.js.

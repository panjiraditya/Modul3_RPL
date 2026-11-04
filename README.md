# Aplikasi Perpustakaan

## Deskripsi
Aplikasi manajemen perpustakaan untuk mempermudah pengelolaan data buku, peminjaman, dan pengembalian. Aplikasi ini dibangun dengan menerapkan arsitektur Model-View-Controller (MVC) untuk memisahkan antarmuka pengguna, logika bisnis, dan interaksi data.

## Struktur Direktori MVC
- **models/**: Berisi file yang menangani interaksi langsung dengan database (kueri, simpan, ubah, hapus data).
- **views/**: Berisi file antarmuka pengguna (GUI/UI) yang akan dilihat dan berinteraksi langsung dengan pengguna.
- **controllers/**: Berisi logika bisnis yang menerima input dari *views*, memprosesnya, dan menghubungkannya dengan *models*.

## Panduan Instalasi & Konfigurasi Database MySQL
1. Pastikan server MySQL (misalnya melalui XAMPP) sudah berjalan.
2. Buka phpMyAdmin, lalu buat database baru dengan nama `perpustakaan`.
3. Impor skema database (file `.sql`) yang tersedia di repositori ini ke dalam database tersebut.
4. Buka file konfigurasi koneksi database di dalam proyek, lalu sesuaikan nama host (`localhost`), user (`root`), password (` ` / kosong), dan nama database (`db_perpustakaan`).

## Cara Menjalankan Aplikasi
1. Buka terminal dan arahkan ke direktori proyek.
2. Instal semua dependensi yang dibutuhkan dengan perintah: `pip install -r requirements.txt`.
3. Jalankan aplikasi menggunakan perintah: `python main.py` *(sesuaikan `main.py` dengan nama file utama aplikasi Anda)*.
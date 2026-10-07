from models.buku_model import BukuModel

def test_buku():
    buku = BukuModel()
    
    # 0. Menambahkan Buku Baru Secara Manual
    print("=== Tambah Data Buku Baru ===")
    judul_input = input("Masukkan judul buku: ")
    penulis_input = input("Masukkan nama penulis: ")
    tahun_input = input("Masukkan tahun rilis/terbit: ")
    
    # Konversi tahun ke integer jika diperlukan oleh model Anda
    buku.create_buku(judul_input, penulis_input, int(tahun_input))
    print("Data buku berhasil ditambahkan!\n")

    # 1. Menampilkan Daftar Buku Saat Ini
    print("=== Daftar Buku Saat Ini ===")
    semua_buku = buku.get_all_buku() 
    for row in semua_buku:
        print(f"[{row['id_buku']}] {row['judul']} - {row['penulis']} ({row['tahun_terbit']})")
    print()

    # 2. Proses Update Data pada ID 13
    print("Mengubah data buku dengan ID 16...")
    buku.update_buku(16, "Python MVC Edisi Revisi", "Guido van Rossum", 2024)

    # 3. Menampilkan Daftar Buku (Setelah Update)
    print("=== Daftar Buku (Setelah Update) ===")
    semua_buku_update = buku.get_all_buku()
    for row in semua_buku_update:
        print(f"[{row['id_buku']}] {row['judul']} - {row['penulis']} ({row['tahun_terbit']})")
    print()

    # 4. Proses Delete Data pada ID 15
    print("Menghapus data buku dengan ID 13...")
    buku.delete_buku(13)

    # 5. Menampilkan Daftar Buku (Setelah Delete)
    print("=== Daftar Buku (Setelah Delete) ===")
    semua_buku_delete = buku.get_all_buku()
    for row in semua_buku_delete:
        print(f"[{row['id_buku']}] {row['judul']} - {row['penulis']} ({row['tahun_terbit']})")

if __name__ == "__main__":
    test_buku()
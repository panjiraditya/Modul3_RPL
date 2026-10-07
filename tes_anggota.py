from models.anggota_model import AnggotaModel

def test_anggota():
    anggota = AnggotaModel()

    print("--- MENGUJI CREATE ANGGOTA ---")
    
    # Mengambil input manual dari pengguna
    nama_input = input("Masukkan nama anggota: ")
    alamat_input = input("Masukkan alamat anggota: ")
    
    # Menambahkan data anggota berdasarkan input
    anggota.create_anggota(nama_input, alamat_input)

    print("\n--- MENGUJI READ ANGGOTA ---")
    # Membaca dan menampilkan data anggota
    anggota.read_anggota()

if __name__ == "__main__":
    test_anggota()
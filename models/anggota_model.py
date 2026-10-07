from config.database import Database

class AnggotaModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "anggota"

    def create_anggota(self, nama, alamat):
        if self.conn:
            cursor = self.conn.cursor()
            query = f"INSERT INTO {self.table_name} (nama, alamat) VALUES (%s, %s)"
            val = (nama, alamat)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            print(f"Berhasil: Anggota baru bernama '{nama}' telah ditambahkan.")
            return True

    def read_anggota(self):
        if self.conn:
            # Menggunakan dictionary=True agar hasil query berupa dictionary
            cursor = self.conn.cursor(dictionary=True) 
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            
            print("\n--- DAFTAR ANGGOTA ---")
            if not results:
                print("Belum ada data anggota.")
            else:
                for row in results:
                    # Menyesuaikan dengan nama kolom: id_anggota, nama, alamat
                    print(f"ID: {row['id_anggota']} | Nama: {row['nama']} | Alamat: {row['alamat']}")
            return results

# Pengujian langsung (jika file ini dijalankan)
if __name__ == "__main__":
    anggota = AnggotaModel()
    
    print("--- MENGUJI CREATE ANGGOTA ---")
    anggota.create_anggota("Budi Santoso", "Jl. Merpati No. 10")
    anggota.create_anggota("Siti Aminah", "Jl. Mawar No. 5")
    
    print("\n--- MENGUJI READ ANGGOTA ---")
    anggota.read_anggota()
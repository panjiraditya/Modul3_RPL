from config.database import Database

class BukuModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "buku"

    def get_all_buku(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = "SELECT id_buku, judul, penulis, tahun_terbit FROM buku" 
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            return data
        return []

    def create_buku(self, judul, penulis, tahun):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                # PERIKSA: Pastikan nama kolom 'tahun_terbit' sama persis dengan yang ada di database Anda
                query = "INSERT INTO buku (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
                
                # Eksekusi query
                cursor.execute(query, (judul, penulis, tahun))
                
                # WAJIB ADA: Perintah ini untuk menyimpan perubahan secara permanen
                self.conn.commit() 
                
                cursor.close()
                return True
            except Exception as e:
                print(f"Terjadi kesalahan saat simpan data: {e}") # Akan mencetak error di terminal
                return False
        return False

    def update_buku(self, id_buku, judul, penulis, tahun):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                # PERIKSA: Pastikan nama kolom 'tahun_terbit' sama persis dengan yang ada di database
                query = "UPDATE buku SET judul = %s, penulis = %s, tahun_terbit = %s WHERE id_buku = %s"
                cursor.execute(query, (judul, penulis, tahun, id_buku))
                
                # WAJIB ADA
                self.conn.commit()
                
                cursor.close()
                return True
            except Exception as e:
                print(f"Terjadi kesalahan saat update data: {e}")
                return False
        return False

    def delete_buku(self, id_buku):
        if self.conn:
            cursor = self.conn.cursor()
            query = f"DELETE FROM {self.table_name} WHERE id_buku = %s"
            val = (id_buku,)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            # Teks print disesuaikan
            print("Data buku berhasil dihapus!\n")
            return True
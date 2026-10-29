import hashlib
from config.database import Database

class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "users"

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def autentikasi(self, username, password):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            password_hash = self.hash_password(password)
            query = f"SELECT id_user, username, role FROM {self.table_name} WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password_hash))
            user = cursor.fetchone()
            cursor.close()
            return user
        return None

    # Tugas 1: Fungsi Registrasi User Baru dengan Hash SHA-256
    def register_user(self, username, password, role='anggota'):
        if self.conn:
            cursor = self.conn.cursor()
            password_hash = self.hash_password(password)
            query = f"INSERT INTO {self.table_name} (username, password, role) VALUES (%s, %s, %s)"
            try:
                # Berikan indentasi pada blok kode di dalam try
                cursor.execute(query, (username, password_hash, role))
                self.conn.commit()
                return True
            except Exception as e:
                # Tangkap error jika terjadi kegagalan (misal: username sudah ada)
                print(f"Terjadi kesalahan saat registrasi: {e}")
                return False
            finally:
                # Pastikan cursor selalu ditutup baik berhasil maupun gagal
                cursor.close()
        return False
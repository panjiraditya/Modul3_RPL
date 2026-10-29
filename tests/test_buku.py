from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()
    
    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor
    
    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)
    
    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()

def test_get_all_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()
    
    # Mock koneksi dan cursor
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor
    
    # Membuat data tiruan yang seolah-olah dikembalikan oleh database
    data_dummy = [
        {'id_buku': 1, 'judul': 'Laskar Pelangi', 'penulis': 'Andrea Hirata', 'tahun_terbit': 2005},
        {'id_buku': 2, 'judul': 'Bumi Manusia', 'penulis': 'Pramoedya', 'tahun_terbit': 1980}
    ]
    
    # Mengatur agar cursor.fetchall() mengembalikan data dummy tersebut
    mock_cursor.fetchall.return_value = data_dummy
    
    # Eksekusi fungsi yang diuji
    hasil = model.get_all_buku()
    
    # Verifikasi apakah cursor.execute dipanggil (sesuaikan string query dengan yang ada di model Anda)
    mock_cursor.execute.assert_called_once()
    
    # Verifikasi apakah hasil fungsi cocok dengan data dummy
    assert hasil == data_dummy
    assert len(hasil) == 2
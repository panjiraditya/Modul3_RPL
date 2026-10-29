import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        # Inisialisasi Model dan View untuk Anggota
        self.model = AnggotaModel()
        self.view = AnggotaView()
        
        # Binding tombol simpan
        self.view.btn_simpan.configure(command=self.simpan_data)
        
        # Muat data awal
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Kosongkan tabel
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
            
        # Ambil data dari model
        data_anggota = self.model.get_all_anggota()
        
        # Masukkan ke tabel View (asumsi field: id_anggota, nama, email, telepon)
        for anggota in data_anggota:
            self.view.tabel.insert("", "end", values=(anggota['id_anggota'], anggota['nama'], anggota['email'], anggota['telepon']))

    def simpan_data(self):
        # Ambil data dari form
        nama = self.view.entry_nama.get()
        email = self.view.entry_email.get()
        telepon = self.view.entry_telepon.get()
        
        if not nama or not email or not telepon:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return
            
        # Simpan via model
        berhasil = self.model.create_anggota(nama, email, telepon)
        
        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.view.entry_nama.delete(0, 'end')
            self.view.entry_email.delete(0, 'end')
            self.view.entry_telepon.delete(0, 'end')
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def run(self):
        self.view.mainloop()
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()

        # Menampilkan informasi role pada judul jendela aplikasi
        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")

        # 1. PERBAIKAN: Binding semua tombol ke fungsinya masing-masing
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_perbarui.configure(command=self.perbarui_data)
        self.view.btn_hapus.configure(command=self.hapus_data)
        
        # BINDING TOMBOL LOG OUT
        self.view.btn_logout.configure(command=self.logout)

        # 2. PERBAIKAN: Tambahkan event binding agar saat tabel diklik, form otomatis terisi
        self.view.tabel.bind("<ButtonRelease-1>", self.pilih_data_tabel)

        # OTORISASI: Jika bukan admin, nonaktifkan form input dan SEMUA tombol aksi
        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci")
            self.view.btn_perbarui.configure(state="disabled", text="Akses Terkunci")
            self.view.btn_hapus.configure(state="disabled", text="Akses Terkunci")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        self.muat_data_tabel()

    # 3. PERBAIKAN: Fungsi baru untuk memindahkan data dari tabel ke form input saat diklik
    def pilih_data_tabel(self, event):
        # Abaikan jika bukan admin karena form terkunci
        if self.user_role != "admin":
            return 
            
        selected_item = self.view.tabel.selection()
        if selected_item:
            item_values = self.view.tabel.item(selected_item[0], 'values')
            
            # Bersihkan isi form saat ini
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            
            # Isi form dengan data dari baris tabel yang diklik
            self.view.entry_judul.insert(0, item_values[1])
            self.view.entry_penulis.insert(0, item_values[2])
            if len(item_values) > 3:
                self.view.entry_tahun.insert(0, item_values[3])

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()
        for buku in data_buku:
            # GANTI 'tahun' dengan nama kolom yang benar sesuai database, misal 'tahun_terbit'
            tahun_buku = buku.get('tahun_terbit', '') 
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], tahun_buku))
            
    def simpan_data(self):
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()
        
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return
            
        berhasil = self.model.create_buku(judul, penulis, tahun)
        
        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")
 
    def hapus_data(self):
        selected_item = self.view.tabel.selection()
        
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data di tabel yang ingin dihapus terlebih dahulu!")
            return

        item_values = self.view.tabel.item(selected_item[0], 'values')
        id_buku = item_values[0]
        
        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus buku ini?")
        
        if konfirmasi:
            berhasil = self.model.delete_buku(id_buku)
            if berhasil:
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                # Bersihkan form jika kebetulan sedang menampilkan data yang dihapus
                self.view.entry_judul.delete(0, 'end')
                self.view.entry_penulis.delete(0, 'end')
                self.view.entry_tahun.delete(0, 'end')
                self.muat_data_tabel() 
            else:
                messagebox.showerror("Error", "Gagal menghapus data buku.")

    def perbarui_data(self):
        selected_item = self.view.tabel.selection()
        
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data di tabel yang ingin diperbarui terlebih dahulu!")
            return

        item_values = self.view.tabel.item(selected_item[0], 'values')
        id_buku = item_values[0]
        
        judul_baru = self.view.entry_judul.get()
        penulis_baru = self.view.entry_penulis.get()
        tahun_baru = self.view.entry_tahun.get()
        
        if not judul_baru or not penulis_baru or not tahun_baru:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi untuk memperbarui data!")
            return

        berhasil = self.model.update_buku(id_buku, judul_baru, penulis_baru, tahun_baru)
        
        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal memperbarui data buku.")

    # FUNGSI LOG OUT
    def logout(self):
        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin log out?")
        
        if konfirmasi:
            self.view.destroy()
            
            # Import diletakkan di dalam fungsi untuk mencegah Error Circular Import
            from controllers.auth_controller import AuthController
            app_login = AuthController()
            app_login.run()

    def run(self):
        self.view.mainloop()
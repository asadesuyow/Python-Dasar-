import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

# Inisialisasi daftar kendaraan yang sudah membayar
kendaraan_yang_telah_bayar = []

# Fungsi untuk menghitung biaya parkir
def hitung_biaya_parkir():
    try:
        waktu_masuk = datetime.strptime(entry_waktu_masuk.get(), "%H:%M")
        waktu_keluar = datetime.strptime(entry_waktu_keluar.get(), "%H:%M")
        
        selisih_waktu = waktu_keluar - waktu_masuk
        waktu_parkir = selisih_waktu.total_seconds() / 3600  # Menghitung selisih waktu dalam jam
        
        harga_per_jam = 2000
        biaya_parkir = waktu_parkir * harga_per_jam
        label_hasil.config(text=f"Biaya parkir: Rp {biaya_parkir:.2f}")
        
        # Menambahkan data kendaraan ke daftar yang sudah membayar
        nomor_plat = entry_nomor_plat.get()
        data_kendaraan = (nomor_plat, waktu_masuk.strftime("%H:%M"), waktu_keluar.strftime("%H:%M"), f"Rp {biaya_parkir:.2f}")
        kendaraan_yang_telah_bayar.append(data_kendaraan)
        update_tabel()
    except ValueError:
        messagebox.showerror("Error", "Format waktu masuk/waktu keluar tidak valid!")

# Fungsi untuk mengupdate tabel kendaraan yang sudah membayar
def update_tabel():
    for i in tree.get_children():
        tree.delete(i)
    for data_kendaraan in kendaraan_yang_telah_bayar:
        tree.insert("", "end", values=data_kendaraan)

# Fungsi untuk mencari nomor plat kendaraan
def cari_nomor_plat():
    nomor_plat_cari = entry_cari_nomor_plat.get()
    for data_kendaraan in kendaraan_yang_telah_bayar:
        if nomor_plat_cari == data_kendaraan[0]:
            detail_data = "\n".join(data_kendaraan)
            messagebox.showinfo("Detail Kendaraan", f"Data Kendaraan:\n{detail_data}")
            return
    messagebox.showinfo("Hasil Pencarian", f"Nomor Plat {nomor_plat_cari} tidak ditemukan.")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Parkir")

# Label dan entry untuk nomor plat kendaraan
label_nomor_plat = tk.Label(root, text="Nomor Plat:")
label_nomor_plat.pack()
entry_nomor_plat = tk.Entry(root)
entry_nomor_plat.pack()

# Label dan entry untuk waktu masuk
label_waktu_masuk = tk.Label(root, text="Waktu Masuk (HH:MM):")
label_waktu_masuk.pack()
entry_waktu_masuk = tk.Entry(root)
entry_waktu_masuk.pack()

# Label dan entry untuk waktu keluar
label_waktu_keluar = tk.Label(root, text="Waktu Keluar (HH:MM):")
label_waktu_keluar.pack()
entry_waktu_keluar = tk.Entry(root)
entry_waktu_keluar.pack()

# Tombol untuk menambahkan kendaraan ke daftar dan menghitung biaya parkir
tambah_button = tk.Button(root, text="Tambahkan dan Hitung Biaya Parkir", command=hitung_biaya_parkir)
tambah_button.pack()

# Label untuk menampilkan hasil perhitungan biaya parkir
label_hasil = tk.Label(root, text="")
label_hasil.pack()

# Label dan entry untuk mencari nomor plat kendaraan
label_cari_nomor_plat = tk.Label(root, text="Cari Nomor Plat:")
label_cari_nomor_plat.pack()
entry_cari_nomor_plat = tk.Entry(root)
entry_cari_nomor_plat.pack()

# Tombol untuk mencari nomor plat kendaraan
cari_button = tk.Button(root, text="Cari", command=cari_nomor_plat)
cari_button.pack()

# Membuat tabel untuk menampilkan daftar kendaraan yang sudah membayar
tree = ttk.Treeview(root, columns=("Nomor Plat", "Waktu Masuk", "Waktu Keluar", "Biaya"), show="headings")
tree.heading("Nomor Plat", text="Nomor Plat")
tree.heading("Waktu Masuk", text="Waktu Masuk")
tree.heading("Waktu Keluar", text="Waktu Keluar")
tree.heading("Biaya", text="Biaya")
tree.pack()

# Tombol untuk menambahkan kendaraan ke daftar yang sudah membayar
tambah_ke_daftar_button = tk.Button(root, text="Tambahkan ke Daftar", command=update_tabel)
tambah_ke_daftar_button.pack()

root.mainloop()

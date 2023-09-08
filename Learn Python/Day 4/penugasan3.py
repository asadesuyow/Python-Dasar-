import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Fungsi untuk menyimpan data siswa ke dalam file teks
def simpan_data():
    nama_lengkap = entry_nama_lengkap.get()
    tanggal_lahir = entry_tanggal_lahir.get()
    asal_sekolah = entry_asal_sekolah.get()
    nisn = entry_nisn.get()
    nama_ayah = entry_nama_ayah.get()
    nama_ibu = entry_nama_ibu.get()
    nomor_telepon = entry_nomor_telepon.get()
    alamat = entry_alamat.get("1.0", "end-1c")

    data_siswa = [nama_lengkap, tanggal_lahir, asal_sekolah, nisn, nama_ayah, nama_ibu, nomor_telepon, alamat]

    tree.insert('', 'end', values=data_siswa)

    with open("data_siswa.txt", "a") as file:
        file.write("\t".join(data_siswa) + "\n")

    messagebox.showinfo("Info", "Data siswa berhasil disimpan")

    # Setel ulang nilai-nilai input field
    entry_nama_lengkap.delete(0, "end")
    entry_tanggal_lahir.delete(0, "end")
    entry_asal_sekolah.delete(0, "end")
    entry_nisn.delete(0, "end")
    entry_nama_ayah.delete(0, "end")
    entry_nama_ibu.delete(0, "end")
    entry_nomor_telepon.delete(0, "end")
    entry_alamat.delete("1.0", "end")

# Fungsi untuk menghapus data yang dipilih dari tabel
def hapus_data():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Peringatan", "Pilih data siswa yang akan dihapus.")
        return

    for item in selected_item:
        data = tree.item(item, 'values')
        with open("data_siswa.txt", "r") as file:
            lines = file.readlines()
        with open("data_siswa.txt", "w") as file:
            for line in lines:
                if "\t".join(data) not in line:
                    file.write(line)
        tree.delete(item)

# Fungsi untuk menampilkan data yang tersimpan
def tampilkan_data():
    tree.delete(*tree.get_children())
    with open("data_siswa.txt", "r") as file:
        for line in file:
            data = line.strip().split("\t")
            tree.insert('', 'end', values=data)

# Membuat jendela tkinter
root = tk.Tk()
root.title("DATA SISWA BARU")

# Label dan Entry untuk Nama Lengkap
label_nama_lengkap = tk.Label(root, text="Nama Lengkap:")
label_nama_lengkap.pack()
entry_nama_lengkap = tk.Entry(root)
entry_nama_lengkap.pack()

# Label dan Entry untuk Tanggal Lahir
label_tanggal_lahir = tk.Label(root, text="Tanggal Lahir:")
label_tanggal_lahir.pack()
entry_tanggal_lahir = tk.Entry(root)
entry_tanggal_lahir.pack()

# Label dan Entry untuk Asal Sekolah
label_asal_sekolah = tk.Label(root, text="Asal Sekolah:")
label_asal_sekolah.pack()
entry_asal_sekolah = tk.Entry(root)
entry_asal_sekolah.pack()

# Label dan Entry untuk NISN
label_nisn = tk.Label(root, text="NISN:")
label_nisn.pack()
entry_nisn = tk.Entry(root)
entry_nisn.pack()

# Label dan Entry untuk Nama Ayah
label_nama_ayah = tk.Label(root, text="Nama Ayah:")
label_nama_ayah.pack()
entry_nama_ayah = tk.Entry(root)
entry_nama_ayah.pack()

# Label dan Entry untuk Nama Ibu
label_nama_ibu = tk.Label(root, text="Nama Ibu:")
label_nama_ibu.pack()
entry_nama_ibu = tk.Entry(root)
entry_nama_ibu.pack()

# Label dan Entry untuk Nomor Telepon
label_nomor_telepon = tk.Label(root, text="Nomor Telepon:")
label_nomor_telepon.pack()
entry_nomor_telepon = tk.Entry(root)
entry_nomor_telepon.pack()

# Label dan Entry untuk Alamat
label_alamat = tk.Label(root, text="Alamat:")
label_alamat.pack()
entry_alamat = tk.Text(root, height=5, width=30)
entry_alamat.pack()

# Tombol untuk menyimpan data
button_simpan = tk.Button(root, text="Simpan Data", command=simpan_data)
button_simpan.pack()

# Tombol untuk menghapus data
button_hapus = tk.Button(root, text="Hapus Data", command=hapus_data)
button_hapus.pack()

# Tombol untuk menampilkan data yang tersimpan
button_tampilkan = tk.Button(root, text="Tampilkan Data", command=tampilkan_data)
button_tampilkan.pack()

# Membuat Treeview untuk menampilkan data dalam tabel
tree = ttk.Treeview(root, columns=("Nama Lengkap", "Tanggal Lahir", "Asal Sekolah", "NISN", "Nama Ayah", "Nama Ibu", "Nomor Telepon", "Alamat"))
tree.heading("#1", text="Nama Lengkap")
tree.heading("#2", text="Tanggal Lahir")
tree.heading("#3", text="Asal Sekolah")
tree.heading("#4", text="NISN")
tree.heading("#5", text="Nama Ayah")
tree.heading("#6", text="Nama Ibu")
tree.heading("#7", text="Nomor Telepon")
tree.heading("#8", text="Alamat")
tree.pack()

root.mainloop()

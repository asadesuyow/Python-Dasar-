import tkinter as tk
from tkinter import ttk

def hitung_total():
    harga_barang = float(entry_harga.get())
    kuantitas_barang = int(entry_kuantitas.get())
    
    total_harga = harga_barang * kuantitas_barang
    
    hasil_label.config(text=f"Total: Rp.{total_harga:.2f} ")

# Membuat jendela tkinter
window = tk.Tk()
window.title("Program Kasir Sederhana")

# Membuat frame input
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10)

# Label untuk harga barang
label_harga = ttk.Label(input_frame, text="Harga:", anchor="center")
label_harga.grid(row=0, column=0, padx=10, pady=5)

# Entry (kotak input) untuk harga barang
entry_harga = ttk.Entry(input_frame)
entry_harga.grid(row=1, column=0, padx=10, pady=5)

# Label untuk kuantitas barang
label_kuantitas = ttk.Label(input_frame, text="Kuantitas:", anchor="center")
label_kuantitas.grid(row=2, column=0, padx=10, pady=5)

# Entry untuk kuantitas barang
entry_kuantitas = ttk.Entry(input_frame)
entry_kuantitas.grid(row=3, column=0, padx=10, pady=5)

# Tombol hitung total
hitung_button = ttk.Button(input_frame, text="Total", command=hitung_total,)
hitung_button.grid(row=4, column=0, pady=10)

# Label untuk hasil total
hasil_label = ttk.Label(window, text="")
hasil_label.pack()

# Menjalankan aplikasi
window.mainloop()
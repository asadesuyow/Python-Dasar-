nama = input("Masukkan Nama: ")
gaji = int(input("Masukkan Gaji: "))

tunjangan = 0.2 * gaji
pajak = 0.15 * (gaji+tunjangan)
gajiBersih = int(gaji+tunjangan-pajak)

print("............................")
print("Nama : ", nama)
print("Gaji : ", gaji)
print("Tunjangan : ", tunjangan)
print("Gaji Bersih : ", gajiBersih)
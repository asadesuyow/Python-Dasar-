def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_trapesium(panjang_atas, panjang_bawah, tinggi):
    return 0.5 * (panjang_atas + panjang_bawah) * tinggi

pilihan = input("Pilih bentuk (persegi / persegi panjang / trapesium): ").lower()

if pilihan == "persegi":
    sisi = float(input("Masukkan panjang sisi: "))
    print(f"Luas persegi: {luas_persegi(sisi)}")
    print(f"Keliling persegi: {keliling_persegi(sisi)}")
elif pilihan == "persegi panjang":
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    print(f"Luas persegi panjang: {luas_persegi_panjang(panjang, lebar)}")
    print(f"Keliling persegi panjang: {keliling_persegi_panjang(panjang, lebar)}")
elif pilihan == "trapesium":
    panjang_atas = float(input("Masukkan panjang sisi atas: "))
    panjang_bawah = float(input("Masukkan panjang sisi bawah: "))
    tinggi = float(input("Masukkan tinggi: "))
    print(f"Luas trapesium: {luas_trapesium(panjang_atas, panjang_bawah, tinggi)}")
else:
    print("Pilihan tidak valid. Silakan pilih antara 'persegi', 'persegi panjang', atau 'trapesium'.")
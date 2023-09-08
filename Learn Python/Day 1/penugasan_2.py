user = input("Menghitung Tabung/Balok : ")

if user =="Tabung":
    t = int(input("Masukan Tinggi : "))
    j = int(input("Masukan Jari - Jari : "))
    vol = 22/7*j*j*t
    print("Volume Tabung : ", vol)

if user =="Balok":
    p = int(input("Masukan Panjang : "))
    l = int(input("Masukan Lebar : "))
    t = int(input("Masukan Tinggi : "))
    vlm = p*l*t
    print("Volume Balok : ", vlm)

else:
    print ("Tidak terdaftar")
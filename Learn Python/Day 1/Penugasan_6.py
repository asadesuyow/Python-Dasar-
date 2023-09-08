while True :
    nilai = int(input("Masukan Nilai Siswa : "))
    if nilai >= 75:
        print ("Tuntas")
        break

    else:
        remed = (input("Remedial {Y/T}: "))
        if remed == "T":
            print ("Tidak Lulus")
            break

        if remed == "Y":
            print ("Silahkan mengerjakan soal kembali")
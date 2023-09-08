import turtle # mengimpor modul turtle
t = turtle.Turtle() # membuat objek kura-kura
t.pencolor("red") # mengatur warna pena menjadi merah
t.circle(100) # menggambar lingkaran dengan radius 100
t.penup() # mengangkat pena agar tidak meninggalkan jejak
t.goto(0, -50) # memindahkan kura-kura ke posisi (0, -50)
t.pendown() # menurunkan pena agar bisa menulis
t.write("Halo", align="center", font=("Arial", 20, "bold")) # menulis teks "Halo" dengan font Arial ukuran 20 dan tebal
turtle.done() # menampilkan hasil gambar

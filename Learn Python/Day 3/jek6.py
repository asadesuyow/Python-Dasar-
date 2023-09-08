import turtle as t

# Fungsi untuk menggambar lingkaran dengan warna
def draw_circle(color, radius):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Membuat objek turtle
t.speed(0)
t.bgcolor("black")  # Mengatur latar belakang menjadi hitam

# Menggambar bagian dasar logo
t.penup()
t.goto(0, -200)
t.pendown()
draw_circle("#E53033", 200)  # Warna merah dasar

# Menggambar bagian putih tengah logo
t.penup()
t.goto(0, -140)
t.pendown()
draw_circle("white", 140)

# Menggambar bagian hitam tengah logo
t.penup()
t.goto(0, -130)
t.pendown()
draw_circle("black", 130)

# Menggambar bagian putih dalam logo
t.penup()
t.goto(0, -120)
t.pendown()
draw_circle("white", 120)

# Menggambar lingkaran merah dalam logo
t.penup()
t.goto(0, -100)
t.pendown()
draw_circle("#E53033", 100)

# Menggambar lingkaran hitam dalam logo
t.penup()
t.goto(0, -90)
t.pendown()
draw_circle("black", 90)

# Menggambar bagian putih dalam logo
t.penup()
t.goto(0, -80)
t.pendown()
draw_circle("white", 80)

# Menggambar bagian hitam dalam logo
t.penup()
t.goto(0, -70)
t.pendown()
draw_circle("black", 70)

# Menutup jendela ketika di-klik
t.exitonclick()
import turtle

# Fungsi untuk menggambar Bendera Merah Putih Indonesia
def draw_indonesian_flag():
    # Membuat objek turtle
    t = turtle.Turtle()
    t.speed(0)  # Set kecepatan turtle ke maksimum

    # Mengubah latar belakang menjadi warna hitam
    turtle.bgcolor("black")

    # Menggambar Bendera Indonesia
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Menggambar latar merah
    t.color("red")
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(60)
        t.right(90)
    t.end_fill()

    # Menggambar latar putih
    t.penup()
    t.goto(-200, 40)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(40)
        t.right(90)
    t.end_fill()

    # Menutup jendela ketika di-klik
    turtle.exitonclick()

# Memanggil fungsi untuk menggambar Bendera Merah Putih Indonesia
draw_indonesian_flag()

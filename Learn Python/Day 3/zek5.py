import turtle

# Fungsi untuk menggambar bendera dengan tiang
def draw_flag():
    # Membuat objek turtle
    t = turtle.Turtle()
    t.speed(2)

    # Menggambar tiang bendera
    t.penup()
    t.goto(-10, -200)
    t.pendown()
    t.color("brown")  # Warna tiang
    t.begin_fill()
    t.forward(20)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(200)
    t.end_fill()

    # Menggambar bendera
    t.penup()
    t.goto(-10, 0)
    t.pendown()
    t.color("red")  # Warna bendera
    t.begin_fill()
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.end_fill()

    # Menutup jendela ketika di-klik
    turtle.exitonclick()

# Memanggil fungsi untuk menggambar bendera dengan tiang
draw_flag()

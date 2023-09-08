import turtle

# Membuat objek turtle
t = turtle.Turtle()
t.speed(0)  # Set kecepatan turtle ke maksimum

# Menggambar bendera Indonesia
# Garis vertikal merah
t.penup()
t.goto(-100, 100)
t.pendown()
t.color("red")
t.begin_fill()
t.forward(200)
t.right(90)
t.forward(20)
t.right(90)
t.forward(200)
t.right(90)
t.forward(20)
t.end_fill()

# Garis horizontal putih
t.penup()
t.goto(-100, 80)
t.pendown()
t.color("white")
t.begin_fill()
t.forward(200)
t.right(90)
t.forward(20)
t.right(90)
t.forward(200)
t.right(90)
t.forward(20)
t.end_fill()

# Menutup jendela ketika di-klik
turtle.exitonclick()

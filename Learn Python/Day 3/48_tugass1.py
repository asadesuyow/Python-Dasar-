import turtle

# Membuat objek turtle
t = turtle.Turtle()

# Fungsi untuk menggambar persegi panjang
def drawRectangle(width, height):
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

# Fungsi untuk menggambar segitiga
def drawTriangle(side_length):
    for _ in range(3):
        t.forward(side_length)
        t.left(120)

# Fungsi untuk menggambar trapezium
def drawTrapezium(base1, base2, height):
    t.forward(base1)
    t.left(45)
    t.forward(height)
    t.left(135)
    t.forward(base2)
    t.left(45)
    t.forward(height)
    t.left(135)

# Fungsi untuk menggambar jajar genjang
def drawParallelogram(base, height):
    t.forward(base)
    t.left(45)
    t.forward(height)
    t.left(135)
    t.forward(base)
    t.left(45)
    t.forward(height)
    t.left(135)

# Fungsi untuk menggambar belah ketupat
def drawDiamond(side_length):
    for _ in range(2):
        t.forward(side_length)
        t.left(45)
        t.forward(side_length)
        t.left(135)

# Menggambar bangun datar
t.penup()
t.goto(-100, 100)
t.pendown()

drawRectangle(100, 50)
t.penup()
t.goto(50, 100)
t.pendown()

drawTriangle(100)
t.penup()
t.goto(-100, 50)
t.pendown()

drawTrapezium(100, 50, 40)
t.penup()
t.goto(100, 0)
t.pendown()

drawParallelogram(80, 50)
t.penup()
t.goto(0, -50)
t.pendown()

drawDiamond(60)

# Menutup jendela ketika di-klik
turtle.exitonclick()


import turtle

# Membuat objek turtle
t = turtle.Turtle()

# Fungsi untuk menggambar persegi panjang
def drawRectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Fungsi untuk menggambar segitiga
def drawTriangle(side_length, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
    t.end_fill()

# Fungsi untuk menggambar trapezium
def drawTrapezium(base1, base2, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(base1)
    t.left(45)
    t.forward(height)
    t.left(135)
    t.forward(base2)
    t.left(45)
    t.forward(height)
    t.left(135)
    t.end_fill()

# Fungsi untuk menggambar jajar genjang
def drawParallelogram(base, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(base)
    t.left(45)
    t.forward(height)
    t.left(135)
    t.forward(base)
    t.left(45)
    t.forward(height)
    t.left(135)
    t.end_fill()

# Fungsi untuk menggambar segilima
def drawPentagon(side_length, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(side_length)
        t.left(72)
    t.end_fill()

# Menggambar dan mengisi warna bangun datar
t.penup()
t.goto(-100, 100)
t.pendown()

drawRectangle(100, 50, 'red')
t.penup()
t.goto(50, 100)
t.pendown()

drawTriangle(100, 'yellow')
t.penup()
t.goto(-100, 50)
t.pendown()

drawTrapezium(100, 50, 40, 'green')
t.penup()
t.goto(100, 0)
t.pendown()

drawParallelogram(80, 50, 'blue')
t.penup()
t.goto(0, -50)
t.pendown()

drawPentagon(60, 'purple')

# Menutup jendela ketika di-klik
turtle.exitonclick()

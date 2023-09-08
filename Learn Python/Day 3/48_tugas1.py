import turtle

t = turtle.Turtle()

panjang = 200
lebar = 50
tinggi = 100
pa = 100
pb = 200

for i in range(2):
  t.forward(panjang)
  t.right(90)
  t.forward(lebar)
  t.right(90)

t.penup()
t.goto(200,0)
t.pendown()

for i in range (3):
  t.forward(panjang)
  t.left(120)

t.penup()
t.goto(-100,0)
t.pendown()

for i in range (2):
  t.forward(pa)
  t.left(135)
  t.forward(tinggi)
  t.right(90)
  t.forward(tinggi)
  t.left(135)
  t.forward(pb)
turtle.done()
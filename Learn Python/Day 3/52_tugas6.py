import turtle as pp

#set bg sama speed
pp.bgcolor("black")
pp.speed(200)

#lingkaran luar
pp.fillcolor("blue")
pp.pencolor("white")
pp.pensize(20)
pp.begin_fill()
pp.circle(90)
pp.end_fill()



#lingkaran dalem
pp.pensize(2)
pp.up()
pp.goto(10.76417048275058, 128.04430882760155)
pp.down()
pp.setheading(20)
pp.fillcolor("black")
pp.begin_fill()
pp.circle(20, 320)
pp.end_fill()


#buat naro cursor ke dalem lingkarannya
pp.up()
pp.goto(-5.906835398039438e-15, 30.000000000000053)
pp.setheading(90)
pp.down()

#isi lingkaran(jari)
pp.fillcolor("red")
pp.begin_fill()
pp.left(90)
pp.pencolor("white")
pp.forward(10)
pp.right(90)
pp.forward(15)
pp.backward(15)
pp.right(90)
pp.forward(40)
pp.left(90)
pp.forward(15)
pp.setheading(0)
pp.circle(12,90)
pp.forward(60)

#jari kelingking
pp.circle(5, 180)
pp.forward(25)
pp.right(180)
pp.forward(27)

#jari manis
pp.circle(5, 180)
pp.forward(27)
pp.right(180)
pp.forward(29)

#jari tengah
pp.circle(5, 180)
pp.forward(29)
pp.right(180)
pp.forward(50)

#jari telunjuk
pp.circle(8, 180)
pp.forward(65)

#jari jempol
pp.speed(1)

pp.right(130)
pp.forward(30)
pp.circle(10, 180)
pp.forward(29)
pp.right(50)
pp.forward(6)
pp.circle(13, 70)

#bagian bawah buat nempelin garis jari ke bagian tangannya(biar warna merah merata)
pp.right(75)
pp.forward(13)
pp.end_fill()

pp.hideturtle()
pp.done()
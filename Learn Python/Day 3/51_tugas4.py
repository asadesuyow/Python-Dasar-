import turtle

# Fungsi untuk menggambar pohon Fibonacci
def fibonacci_tree(turtle, branch_len, angle, level):
    if level > 0:
        turtle.forward(branch_len)
        turtle.right(angle)
        fibonacci_tree(turtle, branch_len - 15, angle, level - 1)
        turtle.left(angle * 2)
        fibonacci_tree(turtle, branch_len - 15, angle, level - 1)
        turtle.right(angle)
        turtle.backward(branch_len)

# Inisialisasi objek turtle
t = turtle.Turtle()
t.speed(0)  # Set kecepatan turtle ke maksimum

# Posisi awal dan orientasi
t.left(90)
t.up()
t.backward(100)
t.down()

# Panggil fungsi untuk menggambar pohon Fibonacci
fibonacci_tree(t, 100, 30, 5)

# Menutup jendela ketika di-klik
turtle.exitonclick()

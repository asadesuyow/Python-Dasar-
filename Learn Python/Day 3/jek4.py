import turtle

# Fungsi rekursif untuk menggambar pohon Fibonacci
def fibonacci_tree(t, branch_length, levels):
    if levels == 0:
        return
    else:
        t.forward(branch_length)
        t.right(30)
        fibonacci_tree(t, branch_length - 10, levels - 1)
        t.left(60)
        fibonacci_tree(t, branch_length - 10, levels - 1)
        t.right(30)
        t.backward(branch_length)

# Membuat objek turtle
t = turtle.Turtle()
t.speed(0)  # Set kecepatan maksimum

# Mengatur posisi awal dan arah
t.left(90)
t.up()
t.backward(100)
t.down()

# Memanggil fungsi untuk menggambar pohon Fibonacci
fibonacci_tree(t, 100, 6)

# Menutup jendela ketika di-klik
turtle.exitonclick()

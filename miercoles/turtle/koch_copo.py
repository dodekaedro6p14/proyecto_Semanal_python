import turtle

turtle.bgcolor("black")
turtle.pencolor("cyan")
turtle.title("copo de nieve de Koch")

def koch(size, n):                  # Dibujar curva de Koch
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)

def main(level):                    # Tres curvas de Koch se combinan en un copo de nieve de Koch
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle()

level = int(input("Introduzca el pedido de copos de nieve de Koch:"))   # Ingresar orden
main(level)
input("Enter para salir")

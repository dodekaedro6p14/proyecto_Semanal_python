import turtle as tu

tu.bgcolor("black")
tu.pencolor("cyan")
tu.title("copo de nieve de Koch")

def koch(size, n):                  # Dibujar curva de Koch
    if n == 0:
        tu.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            tu.left(angle)
            koch(size/3, n-1)

def main(level):                    # Tres curvas de Koch se combinan en un copo de nieve de Koch
    tu.setup(600, 600)
    tu.penup()
    tu.goto(-200, 100)
    tu.pendown()
    tu.pensize(2)
    koch(400, level)
    tu.right(120)
    koch(400, level)
    tu.right(120)
    koch(400, level)
    tu.hideturtle()

level = int(input("Introduzca el pedido de copos de nieve de Koch:"))   # Ingresar orden
main(level)
input("Enter para salir")

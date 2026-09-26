from turtle import Screen, Pen
import colorsys

screen = Screen()
screen.title("thursday")
screen.bgcolor("black")


t = Pen()
#pen.speed('fastest')

poesia = 0.0                                # rando de colores is 0.0 to 1.0

for i in range(200):
    color = colorsys.hsv_to_rgb(poesia, 1, 1)  # pen wants RGB
    t.pencolor(color)
    t.forward(i * 2)                        # incrementa tamaño
    t.right(121)                            # 120 grados de un tringulo equilatero
    poesia += 0.005                         # incremento por 1/200

t.hideturtle()

input()

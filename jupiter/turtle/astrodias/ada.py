from turtle import Screen, Pen
import colorsys 

scre = Screen()
scre.title("demo")
scre.bgcolor("black")

t = Pen()
poesia = 0.0

for i in range(200):
    color = colorsys.hsv_to_rgb(poesia, 1, 1)
    t.pencolor(color)
    t.forward(i * 2)
    t.right(121)
    
    for e in range(2):
        t.circle(5 * e)

        poesia += 0.005

t.hiderturtle()
input("Enter para salir")


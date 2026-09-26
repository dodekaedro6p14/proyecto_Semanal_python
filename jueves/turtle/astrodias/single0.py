from turtle import Screen, Pen
import colorsys

screen = Screen()
screen.title("Rainbow Spiral")
screen.bgcolor("black")


t = Pen()
#pen.speed('fastest')

hue = 0.0  # range is 0.0 to 1.0

for i in range(200):
    color = colorsys.hsv_to_rgb(hue, 1, 1)  # pen wants RGB
    t.pencolor(color)
    t.forward(i * 2)  # double size
    t.right(121)  # 120 degrees is an equilateral triangle
    hue += 0.005  # increment by 1/200

t.hideturtle()

screen.exitonclick()
import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()

s.title("Dodecaedro")
s.bgcolor("black")
#p = pen()
#t.speed("fastest")

hue = 0.0 # range is 0.0 to 1.0


for x in range(200):
  color = colorsys.hsv_to_rgb(hue, 1, 1) # pen wants RGB
  t.pencolor(color)
  t.width(x/100 + 1)
  t.forward(x)
  t.left(79)
  hue += 0.005

t.hideturtle()

s.exitonclick()
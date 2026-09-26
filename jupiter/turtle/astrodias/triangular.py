import turtle 
import colorsys

p = turtle.Pen()
p.reset()
p.down()
p.speed(22)


for i in range(100):
    p.forward(i)
    p.left(22222)

dog = 0

for i in range(100):
    color = colorsys.hsv_to_rgb(dog,1,1)
    turtle.pencolor(color)
    dog += 0.01
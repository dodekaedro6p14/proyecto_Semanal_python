import turtle
import colorsys




turtle.Screen()
turtle.bgcolor("black")
#turtle.pencolor("red")
turtle.title("Monday")
turtle.speed()

hue = 0.0 # range is 0.0 to 1.0


for i in range (30):
    color = colorsys.hsv_to_rgb(hue, 1, 1) # pen wants RGB 
    turtle.pencolor(color)
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
    hue += 0.05




#turtle.exitonclick()


input('Enter para salir')

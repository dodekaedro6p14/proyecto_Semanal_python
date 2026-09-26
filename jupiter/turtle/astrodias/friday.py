
import turtle
from itertools import cycle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
s.title("friday") 
#t.speed(0)

COLOR_CHOICES = ["red", "orange", "yellow", "green", "blue", "purple"]
# colors used in the spiral

colors = cycle(COLOR_CHOICES) # cycles through the colors


def drawSpiral(myTurtle):
    "Write a function that draws a spiral alternating colors through the rainbow."
    for i in range(0, 500, 5):
        myTurtle.penup()
        myTurtle.setpos(0, 0)
        myTurtle.color(next(colors))
        myTurtle.pendown()
        myTurtle.circle(i)
        myTurtle.left(10)

drawSpiral(t)

input()

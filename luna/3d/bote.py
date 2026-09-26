import turtle
from math import sin, cos

WIN = turtle.Screen()
WIN.setup(1080, 720)
WIN.tracer(0)
WIN.bgcolor("black")
turtle.speed(10)
WIN.title("D3M0 D1BUJ0 3D WH1N TURTL3")
counter = 0

def rotated(x, y, z):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c

class Demo:
    
    VERTICES = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
                (-1, -1,  1), (1, -1,  1), (1, 1,  1), (-1, 1, 1)]


    def __init__(self):
        self.counter = 0
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.color("pink")

    def draw(self):
        for i in range(360):
            turtle.fd(10)
            turtle.rt(5)

demo = Demo()
while True:
    demo.draw()
    WIN.update()
   



input("Enter para salir")

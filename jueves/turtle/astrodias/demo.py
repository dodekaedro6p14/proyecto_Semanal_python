import turtle
import random

s = turtle.Screen()
s.bgcolor('black')
t = turtle.Turtle()
t.pencolor('white')
t.speed(0)

for x in range(100):
    angle = random.randint(0, 45)
    t.right(angle)
    dis1 = random.randint(0, 150)
    t.fd(dis1)
    t.back(dis1)

input('Enter para salir')

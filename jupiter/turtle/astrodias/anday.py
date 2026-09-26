from turtle import *

Screen()
bgcolor("black")
pencolor("yellow")
title("Sunday- Ypsilon : yelllow")
lan = forward
largo = 100
def cubo(largo):
    for i in range(4):
        lan(50)
        right(90)

def spiral():
    for i in range (12):
        cubo(100)
        right(30)

spiral()
cubo(2)
input("Enter")

from turtle import *

Screen()
bgcolor("black")
pencolor("green")
title("Sunday- gamma : GREEN")
lan = forward
largo = 100
def cubo(largo):
    for i in range(4):
        lan(50)
        right(90)

def spiral():
    for i in range (15):
        cubo(100)
        right(24)

spiral()
cubo(2)
input("Enter")

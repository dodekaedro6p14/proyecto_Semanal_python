from turtle import *

setup(width=900, height=600)
title('tarea de Julio')
bgcolor('black')
speed(10)
pencolor('yellow')
hideturtle()

def cruz():
    for i in range(4):
        fd(50)
        lt(90)
        fd(50)
        rt(90)
        fd(50)
        rt(90)

def spiral():
    pensize(1)
    for i in range(8):
        cruz() 
        rt(45)
        pu(); setpos(-200, -200); pd()
        pencolor('orange')
            
        
spiral()

input('Enter para salir')

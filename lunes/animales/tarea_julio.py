##  Diseñando a tarea del pdf Hacki...

from turtle import *

setup(width=900, height=600)
title('tarea de Julio')
bgcolor('black')
speed(10)
pencolor('#f50057')

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
        
spiral()

input('Enter para salir')

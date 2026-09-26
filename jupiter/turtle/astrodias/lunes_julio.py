## Creando lunes del mes de julio 18/07/2022

from turtle import *

##  Diseñando la ventana
title('diseño_julio')
speed(10)
setup(width=900, height=650)
bgcolor('black')
## Ubicacion 200*200
def circle():
    penup()
    pensize(2)
    setpos(200, 200)
    pendown()
    color('#f50057')
    speed(10)
    for i in range(360):
        fd(1)
        rt(1)

circle()
## ubicacion (-200, 200)  Arriba izquierda
def cuadrado(length):
    penup()
    setpos(-200, 200)
    pendown()
    for i in range(4):
        fd(length)
        rt(90)
        
cuadrado(30)
cuadrado(50)
cuadrado(100)
## Ubicacion (-200, -200) Abajo izquierda
def cubo(lado):
    for i in range(4):
        fd(lado)
        rt(90)

def spiral(times=30):
    pensize(1)
    penup()
    setpos(-200, -200)
    pendown()
    lengthh = 10
    for i in range(times):
        cubo(lengthh)
        rt(5)
        lengthh = lengthh + 5

spiral()
## Ubicación (-200, -200) Abajo Derecha
def cruz():
    for i in range(4):   # Numero de veces que se mueve turtle
        fd(25)
        lt(90)
        fd(25)
        rt(90)
        fd(25)
        rt(90)

def spiral2():
    pensize(1)
    penup()
    setpos(200, -200)
    pendown()    
    for i in range(8):   # N° de veces que se crea la cruz()
        cruz()
        rt(45)           ## N° de rotacion de la cruz()

spiral2()
###########################################3#
input('Enter para Salir')

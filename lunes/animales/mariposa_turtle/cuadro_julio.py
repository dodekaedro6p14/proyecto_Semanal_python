from turtle import *

setup(width=900, height=600)
title('Cuadro de Julio')
bgcolor('black')
speed(10)
pencolor('#b71c1c')

## Ubicacion (200, 200) 

def cubo(lado):
    for i in range(4):
        fd(lado)
        rt(90)

def spiral(times=30):                     ## Cantidad de cubo() que giran
    pensize(1)
    penup()
    setpos(100, 200)
    pendown()
    lengthh = 10                          ## longitud
    for i in range(times):
        cubo(lengthh)
        rt(5)
        lengthh = lengthh + 5             ## Incrementa la longitud

spiral()
###########################################################
## Ubicación (-200, 200) Arriba Izquierda

def poligono(lado, n):
    for i in range(n):
        fd(lado)
        rt(120)                           ## Angulos(triangulo)

def espiral():
    pensize(1)
    penup()
    setpos(-200, 100)
    pendown()
    for i in range (10, 200, 5):          ## 10=giro, 200= longitud. 5 = incremento
        poligono(i, 3)                    ## Cantidad de lados 
        rt(10)                            ## Angulos de giro del poligono()  

espiral()
##########################################################
## Ubicación (-200, -200 Abajo Izquierda

def poligono_B(lado, n):
    for i in range(n):
        fd(lado)
        rt(150)

def espiral_C():
    pensize(1)
    penup()
    setpos(-100, -200)
    pendown()
    for i in range (10, 200, 5):
        poligono_B(i, 3)
        rt(10)

espiral_C()
#########################################################
## Ubicación (-200, 200) Abajo Derecha


#def triangulo():


#def espiral_D():
#    pensize(1)
#    penup()
#    setpos(200, -200)
#    pendown()




input('Enter')


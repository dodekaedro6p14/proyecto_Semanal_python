## diseñando una flor con turtle
##                  03/07/2022
from turtle import *
## Diseñando la ventana
title('Flor amarilla')
speed(10)
bgcolor("#f5f5f5")
setup(width=850, height=600)   ##   width(ancho) , height(alto)
def circle():
    for i in range(500):    ##   360 =
        fd(1)
        rt(1)

def quartercircle():
    for i in range(90):
        fd(1)
        rt(1)

def hoja():
    for i in range(2):
        quartercircle()
        rt(90)

def flowerhead():            ## flor cantidad de petalos
    for i in range(12):
        hoja()
        rt(30)

def flower():
    penup()
    speed(0)
    pensize(3)
    setpos(200, 200)
    pendown()
    color('yellow')
    flowerhead()

flower()
###############################################   LIBRO
t =Turtle()
addshape('my_libro350.gif')
t.penup()
t.setpos(-250, 0)
t.pendown()
t.shape('my_libro350.gif')

############################################
def flower2():
    penup()
    pensize(2)
    setpos(50,-200)
    pendown()
    color('yellow')
    flowerhead()

flower2()
##################################################

def flower3():
    penup()
    pensize(2)
    setpos(500, -500)
    pendown()
    color('yellow')
    flowerhead()

flower3()
############################## Escritura
penup()
setpos(200,-200)
pendown()
t.write('Poesía y los Fantasmas de la Realidad', font=('Courier',10,'italic'))

input ('Enter Para Salir...')


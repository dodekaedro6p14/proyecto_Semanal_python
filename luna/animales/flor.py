##                  03/07/2022
from turtle import *

title('Flor cyan')
speed(10)
bgcolor("#CCFF99")
setup(width=1500, height=800)

def circle():
    for i in range(360):
        fd(1)
        rt(1)

def quartercircle():
    for i in range(90):
        fd(1)
        rt(1)

def petal():
    for i in range(2):
        quartercircle()
        rt(90)

def flowerhead():            ## flor cantidad de petalos
    for i in range(5):
        petal()
        rt(30)

def flower():
    penup()
    speed(0)
    color('green')
    pensize(3)
    setpos(200, 200)
    pendown()
    #setheading(90)
    #fd(100)
    #petal()
    #fd(150)
    color('cyan')
    flowerhead()

t =Turtle()
t.penup()
t.setpos(-425, 25)
t.pendown()

flower()
def flower2():
    penup()
    speed(6)
    pensize(2)
    setpos(50,-200)
    pendown()
    petal()
    color('cyan')
    flowerhead()

flower2()
##################################################
def flower3():
    penup()
    speed(10)
    pensize(1)
    setpos(150, -150)
    pendown()
    color('cyan')
    flowerhead()

flower3()
##################################################

penup()
setpos(200,-200)
pendown()
#t.write('Poesía y los Fantasmas de la Realidad', font=('Courier',30,'italic'))

input ('Presione Enter Para Salir...')


from turtle import *

setup(width=900, height=600)
title('MARIPOSA')
bgcolor('black')
speed(10)
rt(3)
hideturtle()
def alas():
    fd(50)      #1
    rt(45)
    fd(50)      #2
    lt(90)
    fd(50)      #3
    rt(45)
    fd(50)      #4            ##
    rt(135)
    fd(50)      #5
    rt(45)
    fd(50)      #6            ## fin segunda ala ++
    lt(155)
    fd(40)      #7
    rt(45)
    fd(40)      #8
    rt(135)
    fd(40)      #9
    rt(45)
    fd(40)      #10           # Fin 3ra ala +-
    lt(140)
    fd(40)      #11
    rt(45)
    fd(40)      #12              
    rt(135)
    fd(40)      #13
    rt(45)
    fd(40)      #14           #fin 4 ala --
    lt(155)
    fd(50)      #15
    rt(45)
    fd(50)      #16           # fin 1ra ala -+
#alas()    
################################# mariposa central
color('#c11b17','#ff0000')
begin_fill()
def mariposa():
    for i in range(6):
        alas() 
        rt(75)
        
mariposa()
end_fill()
#############################   insertando flores
def mediacircle():
    for i in range(90):
        fd(1.5)
        rt(1)

def petal():
    for i in range(2):
        mediacircle()
        rt(90)

def flohead():
    pencolor('white')
    for i in range(12):
        petal()
        rt(30)
def flohead2():
    pencolor('yellow')
    for i in range(15):
        petal()
        rt(24)

def flohead3():
    pencolor('orange')
    for i in range(24):
        petal()
        rt(15)
def flohead4():
    pencolor('#FF3333')
    for i in range(6):
        petal()
        rt(60)

def flower():
    penup(); pensize(1); setpos(200,200)
    pendown()
    flohead()

def flomer():
    penup(); pensize(1); setpos(200, -200)
    pendown()
    flohead2()

def flamer():
    penup(); pensize(1); setpos(-200, 200)
    pendown()
    flohead3()

def flimar():
    penup(); pensize(1); setpos(-200, -200)
    pendown()
    flohead4()

flower()
flomer()
flamer()
flimar()
################################ insertando mi lilbro
t = Turtle()
t.pencolor('blue')
t.penup()
t.setpos(-395,-295); t.pendown()
t.write('Poesía y los Fantasmas de la realidad', font=('Courier',12, 'italic'))
#addshape('../ima/my_libro.gif')
#t.penup()
#t.setpos(0, 0); t.pendown()
#t.shape('../ima/my_libro.gif')
################################
input('Enter para salir')


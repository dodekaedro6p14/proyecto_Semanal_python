from turtle import *

setup(width=900, height=600)
title('MARIPOSA')
bgcolor('#b5eaaa')
speed(10)
rt(3)
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
################################ insertando mi lilbro
t = Turtle()
t.pencolor('blue')
t.penup()
t.setpos(-395,-295)
t.write('Poesía y los Fantasmas de la realidad', font=('Courier',12, 'italic'))
#addshape('my_libro.gif')
#t.penup()
#t.setpos(0, 0 )
#t.pendown()
#t.shape('my_libro.gif')
################################
input('Enter para salir')


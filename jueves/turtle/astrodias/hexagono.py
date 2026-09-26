from turtle import *

setup(width=1080, height=720)
title('hexagono FORMATION')
bgcolor('black'); pencolor('#66FF33')
speed(10); ht()        ## circulo exterior

addshape('../ima/iso.gif')


penup()
setpos(0, -200)
pendown()
circle(200)

pu()
setpos(0,200)
pd()
seth(30)             ## poligino de 6 lados:
for i in range(6):
    rt(60)
    fd(200)
    

home()
seth(330)
for i in range(6):
    lt(60)
    fd(50)

pu()
setpos(150, 150)
pd()
dot(20, 'blue'); fd(50)

input ('Enter para Salir')


from turtle import *

setup(width=800, height=600)
title('ARBOL 2')
speed(10)
bgcolor('#000000')
pencolor('#FF00FF')

#####################
seth(90)
pu(); setpos(0, -100); pd()

def arbol(i):
    if i < 10:
        return
    else:
        fd(i)
        lt(30)
        arbol(3*i/4)
        rt(60)
        arbol(3*i/4)
        lt(30)
        bk(i)

arbol(100)

input('Enter para salir')

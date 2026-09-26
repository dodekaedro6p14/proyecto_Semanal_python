from turtle import *

## diseñando la ventana
title('Caracol')
speed(6)
setup(width=900, height=650)
bgcolor('black')
pencolor('cyan')

def caracol():
    penup()
    setpos(200, 200)
    pendown()
    for i in range(100):
       fd(i * 1)
       rt(45)
        

caracol()

input('Enter')



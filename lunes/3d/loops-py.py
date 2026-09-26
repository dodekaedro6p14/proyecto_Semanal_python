from turtle import *
# Diseñando la ventana
setup   (width=1500, height=800)
bgcolor ('black')
speed   (10)
title   ('sabado')

# Diseñando la aplicacion
def sabado():
    color('cyan')
    speed(10)
    for i in range(360):
        fd(1)
        rt(1)
penup(), setpos(-50, -50), pendown()
lt(45)

def sab2():
    color('cyan')
    for i in range(500):
        fd(10)
        rt(5)

sabado()
sab2()
input ('Presine Enter Para salir') 

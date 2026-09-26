from turtle import *

#t = turtle.Turtle()
Screen()
bgcolor("black")
pencolor("red")
title("Sunday")



def cuadrado(longitud):
   # cautro veces
   for i in range(4):
       # Ir hacia adelante
       forward(longitud)
       # y giras 90 grados
       right(90)
       

def espiral():
    for i in range(72):
        # dibujar un cuadrado de 100
        cuadrado(100)
        # y girar 5 grados
        right (5)
        
# Yo no quiero animaciones
speed(0)
# Dibujar un espiral
espiral()
# El input es para pausar el programa
input("Presiona Enter para salir...")


#t.hideturtle()
#turtle.done()

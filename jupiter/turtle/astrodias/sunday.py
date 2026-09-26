from turtle import *

Screen()
bgcolor("black")
pencolor("red")
title("Sunday- OMEGA RED")

longitud = 100
def cuadrado(longitud):    # cuanto veces    
    for i in range (4):     # ir hacia adelante
        forward(100)   # y giras 90 grados
        right(90)

def espiral():
    for i in range(36):     # cantidad de giros 72
        cuadrado(100)       # dibuja el cuadrado con un angulo de 100
        right(10)            # gira 5 grados

espiral()
cuadrado(2)
input("Presiona enter para salir...")

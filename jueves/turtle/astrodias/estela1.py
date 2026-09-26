from turtle import *



def cuadrado(longitud):
    # Cuatro veces...
    for i in range(4):
        # Ir hacia adelante
        forward(longitud)
        # Y girar 90 grados
        right(90)

def espiral():
    for i in range(72):
        # Dibujar un cuadrado de 100
        cuadrado(100)
        # Y girar 5 grados
        right(5)


# Yo no quiero animaciones
speed(0)
# Dibujar un espiral
espiral()
# El input es para pausar el programa
input("Presiona Enter para salir...")
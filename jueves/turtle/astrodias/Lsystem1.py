from turtle import *

#Screen()
bgcolor("black")
pencolor("red")
title("Lsystems")

length = 5  #Largo en que avanza la tortuga
angle  = 90 #Angulo de inclinacion de la tortuga

def draw_path(path):       # Definimos la variable
    for symbol in path:
        if symbol == 'F':  # Mientras se repirt F
            fd(length)
        elif symbol == '-':
            lt(angle)
        elif symbol == '+':
            rt(angle)

def apply_rule(path):         # Definimos la variable
    rule = "F-F+F+FF-F-F+F"   # Comportamiento de la tortuga
    return path.replace("F", rule)          

path = "F-F-F-F"              # Variable


path = apply_rule(path)       # Repetir el ciclo
path = apply_rule(path)
path = apply_rule(path)
draw_path(path)               # Nombre de la variable

speed(1)                      # Velocidad de la tortuga

exitonclick()
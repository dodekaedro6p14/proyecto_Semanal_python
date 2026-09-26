from turtle import *

setup(width=800, height=600)
title('F-system')
speed(0)
bgcolor('#000000')
pencolor('#00FF7F')
ht()
#####################
penup()
setpos(-150, -150)
pendown()
length = 4
angle = 90

def draw_path(axion):
    for symbol in axion:
        if symbol == 'F':
            fd(length)
        elif symbol =='-':
            lt(angle)
        elif symbol == '+':
            rt(angle)
        
def apply_rule(axion):
    rule = 'FF-F-F-F-FF'
    return axion.replace('F', rule)


axion = "F-F-F-F"
axion = apply_rule(axion)
axion = apply_rule(axion)
draw_path(axion)

input('Enter para salir')

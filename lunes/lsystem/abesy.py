from turtle import *

setup(width=800, height=720)
title('L-system, Formato 3')
speed(0)
bgcolor('#000000')
pencolor('#FF33CC')

penup()
setpos(150, 150)
pendown()
################################
length = 10
angle  = 90

def split_path(path):
    i = 0
    lst = []
    while i < len(path):
        if path[i] == 'F':
            lst.append(path[i:i+2])
            i = i +2
        else:
            lst.append(path[i])
            i = i + 1

    return lst

def apply_rule(path, rules):
    lst = split_path(path)
    for i in range(len(lst)):
        symbol = lst[i]
        if symbol in rules:
            lst[i] = rules[symbol]
    path = ''.join(symbol for symbol in lst)
    return path

def draw_path(path):
    lst = split_path(path)
    for symbol in lst:
        if symbol == 'Fl' or symbol == 'Fr':
            fd(length)
        elif symbol == '-':
            lt(angle)
        elif symbol == '+':
            rt(angle)
        elif symbol == '*':
            circle(5)
rules = {
        'Fl': 'Fl+Fr+',
        'Fr': '-Fl-Fr*'
}

path = 'Fl+Fr+'

for i in range(7):  #catidad de ejecuciones
    path = apply_rule(path, rules)

print(path)
hideturtle()
draw_path(path)
input('Enter para Salir')

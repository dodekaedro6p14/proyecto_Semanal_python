from turtle import *

title('GOTAS DE LLUVIA')
bgcolor('#000000')
setup(width=800, height=600)
ht()
speed(10)

################################# gota

def lluvia():
    for i in range(10):
        pensize(0.5)
        pencolor('white')
        pu(); setpos(0, 250); pd()
        seth(180)
        lt(85)
        fd(450)
        clear()
        dot(10, 'cyan') 
        clear()

lluvia()

################################ programa
input('Enter Para Salir')

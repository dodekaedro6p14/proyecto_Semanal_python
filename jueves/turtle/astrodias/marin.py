## Creando una Mariposa 18/07/2022

from turtle import *

setup(width=900, height=600)
title('marin.py')
bgcolor('#000000')
#speed(0)
color('yellow', '#d50000')
ht()
begin_fill()
def alas():
    fd(50); rt(45); fd(50); lt(90); fd(50); rt(45); fd(50); rt(135); fd(50); rt(45); fd(50); lt(155);
    fd(40); rt(45); fd(40); rt(135); fd(40); rt(45); fd(40); # Fin 3ra ala +-
    lt(140); fd(40); rt(45); fd(40); rt(135); fd(40); rt(45); fd(40)      #14           #fin 4 ala --
    lt(155); fd(50); rt(45); fd(50)      #16           # fin 1ra ala -+
    
################################
def alas_b():
    fd(30); rt(45); fd(30); lt(90); fd(30); rt(45); fd(30);   ##
    rt(135); fd(30); rt(45); fd(30);  ## fin segunda ala ++
    lt(155); fd(20); rt(45); fd(20); rt(135); fd(20); rt(45); fd(20)## Fin 3ra ala +-
    lt(140); fd(20); rt(45); fd(20); rt(135); fd(20); rt(45); fd(20)## fin 4 ala --
    lt(155); fd(30); rt(45); fd(30)    # fin 1ra ala -+

#################################
def mariposa():
    #pencolor('red')
    for i in range(6):
        alas() 
        rt(75)
        
mariposa()
################################
def mariposa_b():
    pensize(1)
    penup()
    setpos(150, 205)
    pendown()
    #pencolor('#d50000')
    for i in range(6):
        alas_b()
        rt(75)

mariposa_b()
###############################
def mariposa_c():
    penup()
    setpos(140, -195)
    pendown()
    #pencolor('#b71c1c')
    for i in range(5):
        alas_b()
        lt(85)

mariposa_c()
##############################
def mariposa_d():
    penup()
    setpos(260, 0)
    pendown()
    #pencolor('#d50000')
    for i in range(7):
        alas_b()
        lt(18)

#mariposa_d()
#############################
def mariposa_e():
    penup()
    setpos(-150, 205)
    pendown()
    #pencolor('#b71c1c')
    for i in range(6):
        alas_b()
        rt(75)

mariposa_e()
##############################
def mariposa_f():
    penup()
    setpos(-140, -195)
    pendown()
    #pencolor('orange')
    for i in range(5):
        alas_b()
        lt(85)

mariposa_f()
###########################333
def mariposa_g():
    penup()
    setpos(-260, 0)
    pendown()
    #pencolor('yellow')
    for i in range(7):
        alas_b()
        lt(18)

#mariposa_g()
##########################   INSERT IMAGEN DE LIBR
penup()
setpos(0, 0)
pendown()
addshape('../ima/mi_libro_recortada.gif')
shape('../ima/mi_libro_recortada.gif')
end_fill()
######################################3
input('Enter para salir')


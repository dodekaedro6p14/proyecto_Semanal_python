# Creando una Mariposa 18/07/2022
from turtle import *
setup(width=900, height=600)
title('MARIPOSA')
bgcolor('#b5eaaa')
color('#c11e17','#ff0000')
begin_fill()
def alas():
    fd(50)      #1
    rt(45)
    fd(50)      #2
    lt(90)
    fd(50)      #3
    rt(45)
    fd(50)      #4            ##
    rt(135)
    fd(50)      #5
    rt(45)
    fd(50)      #6            ## fin segunda ala ++
    lt(155)
    fd(40)      #7
    rt(45)
    fd(40)      #8
    rt(135)
    fd(40)      #9
    rt(45)
    fd(40)      #10           # Fin 3ra ala +-
    lt(140)
    fd(40)      #11
    rt(45)
    fd(40)      #12              
    rt(135)
    fd(40)      #13
    rt(45)
    fd(40)      #14           #fin 4 ala --
    lt(155)
    fd(50)      #15
    rt(45)
    fd(50)      #16           # fin 1ra ala -+

#alas()    
################################
def alas_b():
    fd(30)      #1
    rt(45)
    fd(30)      #2
    lt(90)
    fd(30)      #3
    rt(45)
    fd(30)      #4            ##
    rt(135)
    fd(30)      #5
    rt(45)
    fd(30)      #6            ## fin segunda ala ++
    lt(155)
    fd(20)      #7
    rt(45)
    fd(20)      #8
    rt(135)
    fd(20)      #9
    rt(45)
    fd(20)      #10           # Fin 3ra ala +-
    lt(140)
    fd(20)      #11
    rt(45)
    fd(20)      #12              
    rt(135)
    fd(20)      #13
    rt(45)
    fd(20)      #14           #fin 4 ala --
    lt(155)
    fd(30)      #15
    rt(45)
    fd(30)      #16           # fin 1ra ala -+

#alas_b()
#################################
def mariposa():
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
    for i in range(6):
        alas_b()
        rt(75)

mariposa_b()
###############################
def mariposa_c():
    penup()
    setpos(140, -195)
    pendown()
    for i in range(5):
        alas_b()
        lt(85)

mariposa_c()
##############################
def mariposa_d():
    penup()
    setpos(260, 0)
    pendown()
    for i in range(7):
        alas_b()
        lt(18)

mariposa_d()
#############################
def mariposa_e():
    penup()
    setpos(-150, 205)
    pendown()
    for i in range(6):
        alas_b()
        rt(75)

mariposa_e()
##############################
def mariposa_f():
    penup()
    setpos(-140, -195)
    pendown()
    for i in range(5):
        alas_b()
        lt(85)

mariposa_f()
###########################333
def mariposa_g():
    penup()
    setpos(-260, 0)
    pendown()
    for i in range(7):
        alas_b()
        lt(18)

mariposa_g()
end_fill()
##########################   INSERT IMAGEN DE LIBR
penup()
setpos(0, 0)
pendown()
#addshape('mi_libro_recortada.gif')
#shape('mi_libro_recortada.gif')
input('Enter para salir')


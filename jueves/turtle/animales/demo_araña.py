from turtle import *

####################################################### Diseñando la ventana
setup(width=900, height=650)
bgcolor("#7e354d")
pencolor("cyan")
title("ARAÑA")
ht()
speed(10)
########################################################   INICO DEL PROGRMA
def poto():
    for i in range(90):
        fd(1)
        rt(1)
poto()        
def cuerpo():
    for i in range(80):
        fd(1)
        rt(0.5)
cuerpo()
lt(175)
def hombroa():
    for i in range(15):
        fd(1)
        rt(9)
hombroa()
####################################################### PATA A1 DERECHA
lt(120)
def a1():
    for i in range(80):
        fd(1)
        lt(0.5)
a1()
rt(175) 
def ab():
    for i in range (90):
        fd(1)
        rt(0.5)
ab()
#########################################################  PATA B-2 DERECHA
lt(150)
def b1():
    for i in range(80):
        fd(1)
        lt(0.5)
b1()
rt(170)
def bb():
    for i in range(90):
        fd(1)
        rt(0.55)
bb()
#########################################################   PATA C-3 
lt(130)
def cb():
    for i in range(90):
        fd(1)
        rt(0.55)
cb()
rt(170)
def c1():
    for i in range(80):
        fd(1)
        lt(0.5)
c1()
#########################################################   PATA D-4
lt(155)
def db():
    for i in range(90):
        fd(1)
        rt(0.55)
db()
rt(170)
def d1():
    for i in range(80):
        fd(1)
        lt(0.5)
d1()
########################################################   CABEZA 
lt(175)
def hombro_b():
    for i in range(18):
        fd(1)
        rt(10)
hombro_b()
rt(160)
def boca_izquierdaa():
    for i in range(22):
        fd(1)
        rt(5)
boca_izquierdaa()
rt(150)
def boca_izquierdab():
    for i in range(27):
        fd(1)
        lt(5.2)
boca_izquierdab()
#########################################################   MITAD DEL PROGRAMA (BOCa)
#rt(5)
def boca_derechaa():
    for i in range(27):
        fd(1)
        lt(5.2)
boca_derechaa()
rt(160)
def boca_derechab():
    for i in range(22):
        fd(1)
        rt(5)
boca_derechab()
rt(160)
def hombro_ad():
    for i in range(18):
        fd(1)
        rt(10)
hombro_ad()
########################################################    PATA E-4 IZQUIERDA
rt(175)
def e1():
    for i in range(80):
        fd(1)
        lt(0.5)
e1()
rt(170)
def eb():
    for i in range(90):
        fd(1)
        rt(0.55)
eb()
########################################################    PATA F-3 IZQUIERDA
lt(155)
def fb():
    for i in range(80):
        fd(1)
        lt(0.5)
fb()        
rt(170)
def f1():
    for i in range(90):
        fd(1)
        rt(0.55)
f1()
########################################################    pata g-2 
lt(130)
def gb():
    for i in range(90):####90
        fd(1)
        rt(0.55)
gb()
rt(170)
def g1():
    for i in range(80):######80
        fd(1)
        lt(0.5)
g1()
########################################################    PATA H-1 izquierda
lt(150)
def hb():
    for i in range(90):
        fd(1)
        rt(0.5)
hb()
rt(175)
def h1():
    for i in range(80):
        fd(1)
        lt(0.5)
h1()
########################################################     cola
lt(120)
def hombro_aa():
    for i in range(15):
        fd(1)
        rt(9)
hombro_aa()
lt(175)
def cuerpo_a():
    for i in range(80):
        fd(1)
        rt(0.5)
cuerpo_a()
def poto_a():
    for i in range(90):
        fd(1)
        rt(1)
poto_a()
#########################################################   AGREGANDO LIBRO:
#l = Turtle()
#l.addshape('mi_libro_recortada.gif')
#l.shape('mi_libro_recortada.gif')
#########################################################   COORDEADAS
t = Turtle()
t.ht()
t.penup()
t.setpos(0, 200)
t.pendown()
t.pencolor('red')
t.rt(90)
t.fd(400)
t.penup()
t.setpos(5, 200)
t.pendown()
t.fd(600)
t.penup()
t.setpos(-5, 200)
t.pendown()
t.fd(600)
#########################################################   FIN DEL PROGRMA
input("Presione enter Para Salir...")


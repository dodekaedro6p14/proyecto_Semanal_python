from turtle import *

##  Diseñando la ventana
title('PULPO')
setup(width=900, height=650)
bgcolor('#1b5e20')
pensize(2)
color('#ffff00')
# ## INICIO ## #
#############################                           CABEZA
def cabeza():
    for i in range(110):
        fd(0.7)
        rt(1)

cabeza()
fd(25)
lt(35)
#############################               
def hombro_d():
    for i in range(20):
        fd(1)
        rt(1)

hombro_d()
############################1B                    Tentaculo AAA
def aab():
    for i in range(270):
        fd(0.5)
        lt(1)

aab()
#############################12
def aac():
    for i in range(180):
        fd(0.25)
        rt(1)

aac()
#############################1PUNTA         
lt(220)
def aad():
    for i in range(100):
        fd(0.2)
        lt(1)
aad()
#############################13
lt(50)
def aaa():
    for i in range(250):
        fd(0.75)
        rt(1)
aaa()
############################2B              
rt(190)
def bbb():
    for i in range(95):
        fd(0.8)
        lt(1)

bbb()
############################2A              
def bbc():
    for i in range(210):
        fd(0.6)
        rt(1)

bbc()
###########################2PUNTA
lt(200)
def bbd():
    for i in range(130):
        fd(0.58)
        lt(1)
bbd()
###########################23
lt(73)
def bba():
    for i in range(100):
        fd(1.2)
        rt(1)

bba()
##########################3B
rt(220)
def ccb():
    for i in range(100):
        fd(0.5)
        lt(1)

ccb()
#########################32
def ccc():
    for i in range(220):
        fd(0.8)
        rt(1)

ccc()
########################3PUNTA (corazon)
lt(200)
def ccd():
    for i in range(150):
        fd(0.7)
        lt(1)

ccd()
########################33
lt(70)
def cca():
    for i in range(103):
        fd(0.7)
        rt(1)
cca()
########################       CENTRO DEL PULPO
fd(25)
lt(180)
fd(25)
########################43  
def dda():
    for i in range(103):
        fd(0.7)
        rt(1)
dda()
#######################4PUNTA   ( CORAZÓN)
lt(70)
def ddd():
    for i in range(150):
        fd(0.7)
        lt(1)
ddd()
#######################42
lt(200)
def ddc():
    for i in range(220):
        fd(0.8)
        rt(1)
ddc()
#######################4B
def ddb():
    for i in range(100):
        fd(0.5)
        lt(1)
ddb()
#######################53
lt(138)
def eea():
    for i in range(100):
        fd(1.2)
        rt(1)

eea()
######################5PUNTA  tentaculo 5
lt(75)
def eed():
    for i in range(130):
        fd(0.58)
        lt(1)

eed()
#######################52   
lt(210)
def eec():
    for i in range(210):
        fd(0.6)
        rt(1)

eec()
########################5B
rt(13)
def eeb():
    for i in range(95):
        fd(0.8)
        lt(1)

eeb()
########################63              <<<<<<<
rt(200)
def ffa():
    for i in range(250):
        fd(0.75)
        rt(1)

ffa()
########################6PUNTA      MANO
lt(50)
def ffd():
    for i in range(100):
        fd(0.2)
        lt(1)

ffd()
#########################62                       TENTACULOS
rt(140)
def ffc():
    for i in range(180):
        fd(0.25)
        rt(1)

ffc()
########################6B         FIN DE TENTACULOS
def ffb():
    for i in range(270):
        fd(0.5)
        lt(1)

ffb()
#######################
def hombro_i():
    for i in range(20):
        fd(1)
        rt(1)
hombro_i()
########################  cabeza
lt(35)
fd(26)
def cab():
    for i in range(110):
        fd(0.7)
        rt(1)
cab()
######################## TERMINO DEL PROGRAMA
t = Turtle()
t.pencolor('red')
t.penup()
t.setpos(-250, 0)
t.pendown()
t.fd(500)
t.penup()
t.setpos(0, 250)
t.pendown()
t.rt(90)
t.fd(500)
t.penup()
t.setpos(-100,-100)
t.pendown()
t.lt(90)
t.fd(200)
t.penup()
t.setpos(-200, -200)
t.pendown()
t.fd(400)
t.penup()
t.setpos(-62.5, 200)
t.pendown()
t.rt(90)
t.fd(400)
t.penup()
t.setpos(62.5, 200)
t.pendown()
t.fd(400)
#######################################

input('Enter')

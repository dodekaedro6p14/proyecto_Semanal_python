from turtle import *

##  Diseñando la ventana
title('PULPO')
setup(width=900, height=650)
bgcolor('black')
pensize(1)
color('yellow')
# ## INICIO ## #
def pulpo_solo():
    #### aqui va todo el contenido
    lt(5)
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
############################333AAb                    Tentaculo AAA
    def aab():
        for i in range(270):
            fd(0.5)
            lt(1)

    aab()
#############################222AAc
    def aac():
        for i in range(180):
            fd(0.25)
            rt(1)

    aac()
#############################PUNTAAAd                VUELTA ATRAS
    lt(220)
    def aad():
        for i in range(100):
            fd(0.2)
            lt(1)
    aad()
#############################333AAa
    lt(50)
    def aaa():
        for i in range(250):
            fd(0.75)
            rt(1)
    aaa()
############################BASEBBB                FIN TENTACULO AAA INICIO TENTACILO BBB
    rt(190)
    def bbb():
        for i in range(200):
            fd(0.8)
            lt(1)

    bbb()
############################222BBc              TENTACULO BBB
    def bbc():
        for i in range(150):
            fd(0.25)
            rt(1)
    bbc()
###########################PUNTABBd        FINAL TENTACULO BBd
    lt(230)
    def bbd():
        for i in range(100):
            fd(0.25)
            lt(1)
    bbd()
###########################333BBa
    rt(5)
    def bba():
        for i in range(180):
            fd(1)
            rt(1)

    bba()
##########################BASECCB
    rt(220)
    def ccb():
        for i in range(100):
            fd(0.5)
            lt(1)

    ccb()
#########################222CCc
    def ccc():
        for i in range(220):
            fd(0.8)
            rt(1)

    ccc()
########################PUNTA CCd     FINAL TENTACULO CCC   (corazon)
    lt(200)
    def ccd():
        for i in range(150):
            fd(0.7)
            lt(1)

    ccd()
########################333CCa
    lt(70)
    def cca():
        for i in range(120):
            fd(0.7)
            rt(1)

    cca()
########################        CENTRO DEL PULPO
    lt(44)
    fd(28)
    lt(110)
    fd(27)
########################333DDa       INICIO TENTACULO DDa
    lt(45)
    def dda():
        for i in range(120):
            fd(0.7)
            rt(1)

    dda()
#######################PUNTADDd  FIN TENTACULO CORAZÓN
    lt(70)
    def ddd():
        for i in range(150):
            fd(0.7)
            lt(1)

    ddd()
#######################222DDc
    lt(200)
    def ddc():
        for i in range(220):
            fd(0.8)
            rt(1)

    ddc()
#######################BASEDDb
    def ddb():
        for i in range(100):
            fd(0.5)
            lt(1)

    ddb()
#######################333EEa       tentaculo a
    lt(140)
    def eea():
        for i in range(180):
            fd(1)
            rt(1)

    eea()
######################PUNTA
    def eed():
        for i in range(100):
            fd(0.25)
            lt(1)

    eed()
#######################222EEC
    lt(230)
    def eec():
        for i in range(150):
            fd(0.25)
            rt(1)

    eec()
########################baseEEB
    def eeb():
        for i in range(195):
            fd(0.8)
            lt(1)

    eeb()
########################333FFA
    rt(190)
    def ffa():
        for i in range(250):
            fd(0.75)
            rt(1)

    ffa()
########################PUNTAFFd
    lt(50)
    def ffd():
        for i in range(100):
            fd(0.2)
            lt(1)

    ffd()
#########################PUNTAffc                        TENTACULOS
    rt(140)
    def ffc():
        for i in range(180):
            fd(0.25)
            rt(1)

    ffc()
########################222ffb
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
########################
def pulpos():
    for i in range(4):
        pulpo_solo()
        rt(90)


pulpos()

#########################       PLANO CARTESIANO
#t = Turtle()
#t.pencolor('red')
#t.penup()
#t.setpos(-250, 0)
#t.pendown()
#t.fd(500)
#t.penup()
#t.setpos(0, 250)
#t.pendown()
#t.rt(90)
#t.fd(500)
#t.penup()
#t.setpos(-100,-100)
#t.pendown()
#t.lt(90)
#t.fd(200)
#t.penup()
#t.setpos(-200, -200)
#t.pendown()
#t.fd(400)
#t.penup()
#t.setpos(-62.5, 200)
#t.pendown()
#t.rt(90)
#t.fd(400)
#t.penup()
#t.setpos(62.5, 200)
#t.pendown()
#t.fd(400)

##################################################

input('Enter')

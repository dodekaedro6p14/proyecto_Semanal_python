from turtle import *

title('GEOMETRIA')
bgcolor('#000000')
setup(width=800, height=600)
ht()
speed(10)
########################################## TRIANGULOS
pu()
setpos(-200, -120)
pd()
pencolor('#66FF00')
for i in range(3):
    fd(400)
    lt(120)

pu()
setpos(200, 120)
pd()
seth(180)
for i in range(3):
    fd(400)
    lt(120)

###################################### CIRCULOS
c = Turtle()
c.ht()
c.pu()
c.setpos(0, 225)
c.pd()
c.pencolor('#66FF00')
c.circle(-117)
c.circle(-97)

c.pu()
c.setpos(-200, -120)
c.pd()
c.seth(300)
c.circle(117)
c.circle(97)

c.pu()
c.setpos(200, -120)
c.pd()
c.seth(60)
c.circle(117)
c.circle(97)

########################################

input('Enter Para Salir')

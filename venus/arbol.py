from turtle import *

setup(width=800, height=600); ht()
title('FELIZ NAVIDAD PARA TODOS')
bgcolor('#000000')
addshape('portada.gif')
pencolor('#66FF00');
pensize(5)
speed(1)
##hiderturtle()
################################### IMAGEN DE FONDO
i = Turtle()
i.shape('portada.gif')

###################################  ARBOL DE NAVIDAD
pu()
pos(0, 200)
pd()
rt(45); fd(100); seth(180); fd(30); seth(0)
rt(45); fd(120); seth(180); fd(40); seth(0)
rt(45); fd(150); seth(180); fd(45); seth(0)
rt(45); fd(150); seth(180); fd(45); seth(180); fd(190)
seth(270); pencolor('#330000'); fd(30)

pu()
setpos(0, 200)
pd()
seth(180)
pencolor('#00FF00')
lt(45); fd(100); seth(0); fd(30); seth(180)
lt(45); fd(120); seth(0); fd(40); seth(180)
lt(45); fd(150); seth(0); fd(45); seth(180)
lt(45); fd(150); seth(0); fd(45); seth(0); fd(190)
seth(270); pencolor('#330000'); fd(30)

######################################### ESTRELLA
e = Turtle()

e.ht()
e.pu()
e.setpos(0, 200)
e.pd()
e.seth(250)
e.color('#FF0000', '#FFFF00')
e.begin_fill()

for i in range(5):
    e.rt(144)
    e.fd(40)


e.end_fill()
######################################## ESFERAS    
d = Turtle()

d.speed(1)
d.ht()
d.pu(); d.setpos(50, 150); d.pd(); d.dot(25, 'blue') 
d.pu(); d.setpos(0, 120); d.pd(); d.dot(25,'red')
d.pu(); d.setpos(-50, 90); d.pd(); d.dot(25, '#FFFF00')
d.pu(); d.setpos(-90, 70); d.pd(); d.dot(25, '#33FF00')

d.pu(); d.setpos(90, 70); d.pd(); d.dot(25, 'blue')
d.pu(); d.setpos(50, 50); d.pd(); d.dot(25, 'red')
d.pu(); d.setpos(0, 30); d.pd(); d.dot(25, '#FFFF00')
d.pu(); d.setpos(-50, 10); d.pd(); d.dot(25, '#33FF00')
d.pu(); d.setpos(-90, 0); d.pd(); d.dot(25, 'blue')
d.pu(); d.setpos(-130, -10); d.pd(); d.dot(25, 'red')

d.pu(); d.setpos(130, 0); d.pd(); d.dot(25, '#FFFF00')
d.pu(); d.setpos(90, -20); d.pd(); d.dot(25, '#33FF00')
d.pu(); d.setpos(50, -40); d.pd(); d.dot(25, 'blue')
d.pu(); d.setpos(10, -60); d.pd(); d.dot(25, 'red')
d.pu(); d.setpos(-50, -80); d.pd(); d.dot(25, '#FFFF00')
d.pu(); d.setpos(-90, -100); d.pd(); d.dot(25, '#33FF00')
d.pu(); d.setpos(-130, -120); d.pd(); d.dot(25, 'blue')
d.pu(); d.setpos(-180, -140); d.pd(); d.dot(25, 'red')
d.pu(); d.setpos(-220, -160); d.pd(); d.dot(25, '#FFFF00')

d.pu(); d.setpos(140, -80); d.pd(); d.dot(25, '#33FF00')
d.pu(); d.setpos(100, -100); d.pd(); d.dot(25, 'blue')
d.pu(); d.setpos(50, -120); d.pd(); d.dot(25, 'red')
d.pu(); d.setpos(10, -140); d.pd(); d.dot(25, '#FFFF00')
d.pu(); d.setpos(-50, -160); d.pd(); d.dot(25, '#33FF00')

d.pu(); d.setpos(180, -120); d.pd(); d.dot(25, 'blue')
d.pu(); d.setpos(130, -140); d.pd(); d.dot(25, 'red')
d.pu(); d.setpos(90, -160); d.pd(); d.dot(25, '#FFFF00')

#################################################### ESCRITURA 1
w = Turtle()

w.hideturtle()
w.speed(1)
w.pencolor('#FFFFFF')
w.pu(); w.setpos(-380, 220); w.pd()
w.write('EL MEJOR REGALO ES:', True, align='left', font=('Arial', 50, 'normal'))

#################################################### LIBRO
t = Turtle()
n = Turtle()
m = Turtle()

t.speed(1)
n.speed(1)
m.speed(1)

addshape('fantasmas.gif')
addshape('noche.gif')
addshape('nebulosa.gif')

t.shape('fantasmas.gif')
n.pu(); n.setpos(220, 0); n.pd(); n.shape('nebulosa.gif')
m.pu(); m.setpos(-220, 0); m.pd(); m.shape('noche.gif')

################################################## ESCRITURA 2
l = Turtle()

l.hideturtle()
l.speed(1)
l.pencolor('#FFFFFF')
l.pu(); l.setpos(-380, -280); l.pd()
l.write('UN LIBRO DE "POESÍA".',True, align='left', font=('Arial', 50, 'normal'))





######################################
input('Enter Para Salir')

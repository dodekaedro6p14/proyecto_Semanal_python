from turtle import *

title('TESELADO SEMIRREGULAR')
bgcolor('#000000')
setup(width=800, height=600)
ht()
speed(10)
############################--
pu()
setpos(-150, -250)
pd()
pencolor('#FF3333')
circle(100)

############################-+
pu()
setpos(-150, 50)
pd()
pencolor('#FFFF66')
circle(100)

############################ ++
pu()
setpos(150, 50)
pd()
pencolor('#66FF00')
circle(100)

############################ +-
pu()
setpos(150, -250)
pd()
pencolor('#33FFFF')
circle(100)

############################ CUADRADO
v = Turtle()
v.ht()
v.pu()
v.setpos(-150, -150)
v.pd()
v.pencolor('#FFFFFF')
for i in range(4):
    v.fd(300)
    v.lt(90)

########################## TRIANGUNLO
t = Turtle()
t.ht()
t.pu()
t.setpos(-200,-120)
t.pd()
t.pencolor('#FF33FF')
for i in range(3):
    t.fd(400)
    t.lt(120)

t.pu()
t.setpos(-200, 120)
t.pd()
t.seth(0)
for i in range(3):
    t.fd(400)
    t.rt(120)

##########################  LINESAS
l = Turtle()
l.ht()
l.up()
l.setpos(-0, 250)
l.pd()
l.pencolor('#0000FF')
l.seth(270)
l.fd(500)

l.pu()
l.setpos(-300, -0)
l.pd()
l.seth(0)
l.fd(600)

############################ FIN DEL PROGRAMA
input('Enter Para Salir')



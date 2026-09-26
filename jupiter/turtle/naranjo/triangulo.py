from turtle import *

#screensize(900, 700)
setup(width=800, height=600)
title('triangulo')
bgcolor('black')
pencolor('yellow')
speed(10)

#circle(200)
############################     TRIANGULOS
penup()
setpos(-150, -110)
pendown()

for i in range (3):
    fd(333)
    lt(120)

penup()
setpos(-150, 110)
pendown()

for i in range (3):
     fd(333)
     rt(120)
#################################
#penup()
#setpos(0, 400)
#pendown()

penup()
setpos(0, 300)
pendown()
rt(90)
fd(600)

#penup()
#setpos(-200, 150)
#pendown()
#lt(45)
#fd(600)

#penup()
#setpos(200, 150)
#pendown()
#rt(90)
#fd(600)
#############################3
#clear()
penup()
setpos(0, 200)
pendown() 
rt(90)
circle(200)


input('Presione Enter para Salir')

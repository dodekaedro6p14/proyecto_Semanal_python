from turtle import *

title('CUBO DE METATRON')
bgcolor('#000000')
setup(width=800, height=600)
ht()
speed(10)
####################################### CIRCLES
# VERTICAL
pu(); setpos(0, 153.5); pd()   ## rosado arriba
pencolor('#FFCCCC')
circle(50)

pu(); setpos(0, 53.5); pd()
pencolor('#FF3399')
circle(50)

pu(); setpos(0, -47.5); pd() ## centro
pencolor('#9900FF')
circle(50)

pu(); setpos(0, -146.5); pd()
pencolor('#990000')
circle(50)

pu(); setpos(0, -246.5); pd()
pencolor('#FF0000')
circle(50)

# HORIZONTAL
pu(); setpos(-170, 53.5); pd() ## AMARILLOS
pencolor('#FFFF00')
circle(50)

pu(); setpos(-85, 0); pd()
pencolor('#CC3300'); pd()
circle(50)

pu(); setpos(-175, -150); pd() ## NARANJO
pencolor('#FF6600')
circle(50)

pu(); setpos(-90, -100); pd()
pencolor('#CC0000')
circle(50)

pu(); setpos(170, 53.5); pd() # CIAN
pencolor('#00FFFF')
circle(50)
         
pu(); setpos(85, 0); pd()
pencolor('#006666')
circle(50)

pu(); setpos(175, -150); pd() # AZUL
pencolor('#0000FF')
circle(50)

pu(); setpos(90, -100); pd()
pencolor('#0066FF')
circle(50)

##################################### TRIANGULOS
c = Turtle()
c.ht()
c.seth(0)
c.pu(); c.setpos(-171, -99.5); c.pd() #arriba
c.pencolor('#FFFFFF')
for i in range(3):
    c.fd(350)
    c.lt(120)

c.pu(); c.setpos(171, 99.5); c.pd()
c.seth(180)
for i in range(3):
    c.fd(350)
    c.lt(120)                          
                                      # cuadrados
c.pu(); c.setpos(0, 200); c.pd()  # abajo
c.pencolor('white')
c.seth(30)
for i in range(6):
    c.rt(60)
    c.fd(200)

c.pu(); c.setpos(0, -100); c.pd()
c.seth(330)
for i in range(6):
   c.lt(60)
   c.fd(100)
####################### LINEAS
l = Turtle()
l.pencolor('#FFFFFF')
l.ht()
l.seth(30)
l.pu(); l.setpos(-171, -99.5); l.pd()
l.fd(400)

l.pu(); l.setpos(-171, 99.5); l.pd()
l.seth(-30)
#l.pencolor('yellow')
l.fd(400)

##      linea x, y 

l.pu(); l.setpos(0, 200); l.pd()
l.seth(-90)
l.fd(400)

##l.pu(); l.setpos(-200, 0); l.pd()
#l.seth(0)
#l.fd(400)

####################################
input('Enter Para Salir')

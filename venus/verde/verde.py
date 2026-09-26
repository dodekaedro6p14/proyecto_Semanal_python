from turtle import * 

title('ARBOL')
bgcolor('#000000')
setup(width=800, height=600)
ht()

#####################################
pu(); setpos(-150, -150); pd()
pencolor('#99FF00')


def y (distance, level):
    speed(10)
    if level > 0:
        fd(distance) ## go up the trunk
        rt(30)
        y(distance * .8, level -1) ## left branch
        lt(90)
        y(distance * .7, level -1) ## right branch
        rt(60)
        bk(distance) #back down the trunk

setheading(90)
y(100, 9)

##############   ARBOL 2
#r = Turtle()
#r.pu(); r.setpos(200, 200); r.pd()
#r.pencolor('#66FF00')

#def m (distance)








input('Enter Para Salir')

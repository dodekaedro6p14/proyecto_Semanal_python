from turtle import * 

title('ARBOL')
bgcolor('#000000')
setup(width=800, height=600)
ht()
#####################################
pu(); setpos(-100, -150); pd()
pencolor('#00FA9A')

def y (distance, level):
    speed(10)
    if level > 0:
        fd(distance) ## go up the trunk
        rt(30)
        y(distance * .8, level -1) ## left branch  (.8)
        lt(90)
        y(distance * .7, level -1) ## right branch (.7)
        rt(60)
        circle(10)
        bk(distance) #back down the trunk

setheading(90)
y(80, 3)

input('Enter Para Salir')

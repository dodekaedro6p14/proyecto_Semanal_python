from turtle import *

title('FRACTAL TREES')
bgcolor('#000000')
setup(width=800, height=600)
ht()
speed(10)
pencolor('#00FFFF')
###################################
seth(90)

pu(); setpos(0, -100); pd()
#def y():
#    fd(100); rt(30); fd(70); bk(70)
#    lt(90); fd(50); bk(50)
#    rt(60); bk(100)

def y(distance, level):
    if level > 0:
        fd(distance); rt(30); 
        y(distance * .8, level -1)
        lt(90)
        pencolor('red')
        y(distance * .7, level -1)
        rt(60)
        pencolor('yellow')
        bk(distance)

setheading(90)

largo = 100
hoja = 9
y(largo, hoja )

##################################

input('ENTER PARA SALIR')

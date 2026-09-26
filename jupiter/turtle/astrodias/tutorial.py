from turtle import *

screensize(1980,1100)
setup(width=1500, height=800)
title('Flor Purpura')
bgcolor('black')
speed(10)

# Diseñando petalos
color("#9933FF","#FF22FF")
begin_fill()

lt(23)
while True:
    fd(250)
    lt(135)
    #circle(30)
    if abs(pos()) < 1:
        break

end_fill()
rt(23)
#############################################################33
t = Turtle()
t.penup(); t.setpos(50, 50)
t.pendown(); t.pencolor("#4a148c")

for i in range(4):
    t.fd(100)
    t.rt(90)

#t.lt(46)
###############################################################
pensize(6)
rt(46); circle(136)
lt(46)
#fd(300)

input ('Presione Enter Para Salir...')
#end_fill()
#done()



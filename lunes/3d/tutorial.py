from turtle import *

screensize(1980,1100)
setup(width=1500, height=800)
title('Flor Cyan')
bgcolor('#DDDDDD')
speed(10)
color("#9933FF","#FF22FF")
begin_fill()

lt(30)

while True:
    fd(200)
    lt(225)
    if abs(pos()) < 1:
        break

end_fill()

penup
setpos(-50, -50)
pendown

for i in range(4):
    fd(100)
    rt(90)

input ('Presione Enter Para Salir...')

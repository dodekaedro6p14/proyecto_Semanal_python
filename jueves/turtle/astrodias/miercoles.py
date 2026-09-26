## creamndo miercoels = 6/07/2023
from turtle import *

title('Miercoles')
bgcolor('black')
color ('orange', 'yellow',)
speed(10)
hideturtle()
## Aplicación
lt(20)
begin_fill()
while True:
    fd(200)
    lt(135)
    if abs(pos()) < 1:
#        while True:
#            fd(200)
#            lt(300)
#            circle(150)
#        break                 
        break
rt(5)
while True:
    fd(75)
    lt(300)
    circle(150)
    if abs(pos()) > 1:

        break

end_fill()
input ('Presione Enter para salir..')

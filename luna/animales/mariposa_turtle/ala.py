## Creando una Mariposa 18/07/2022

from turtle import *
from playsound import playsound
## Creadnola ventana ##########################################

setup(width=900, height=600)
title('Mariposa')
bgcolor('black')
#speed(10)
pencolor('#b71c1c')

###  Prueba de sonido
playsound('ala_cont/martes396.mp3')
print('playing sound using playsound')
def alas():
    for i in range(2):
        fd(50)
        lt(45)
        fd(50)
        lt(135)                                             

alas()
######################3########         INSErTANDO IMAGEN

addshape('mi_libro_recortada.gif')

shape('mi_libro_recortada.gif')

###################################




input('Enter')





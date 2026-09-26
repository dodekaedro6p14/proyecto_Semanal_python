from turtle import *

#################################################   
setup(width=900, height=600)
title('ELEFANTE')
bgcolor('#9e7bff')
pencolor('#7e587e')
pensize(3)
speed(10)
ht()
################################################ INICIO DEL PROGRAMA
### CABEZA
fd(30)  #1
rt(45)
fd(15)   #2
lt(90)
fd(15)   #3
rt(90) # oreja
fd(50)  #4
rt(80) # punta 90
fd(60)  #5
rt(90)  #E
fd(25)  #6
lt(90)#90
fd(20)   #7
lt(90)# cuerno 45
fd(50)  #8
lt(45)  #h
fd(30)  #9
lt(45)
fd(30)   #10
lt(90)  #j
fd(15)   #11
lt(150) #punta del cuerno
fd(10)   #12
rt(60) #l
fd(22)  #13
rt(55) #m
fd(24)  #14
rt(40)  # NNNNNNNNN
fd(42)  #15
rt(15)
fd(30)  #16
rt(90)  #ojo
fd(9)
rt(90)
fd(9)
rt(90)
fd(9)
rt(90)
fd(9)
rt(55) #t
fd(15)  #21
rt(30)
fd(25)  #22
##   Levantar lapiz
penup()
rt(145)
fd(70)
pendown()
lt(5)
fd(50)
lt(45) ## punta de nariz
fd(10)
rt(45)
fd(10)
rt(90)
fd(15)
############################################### 
lt(20)
fd(15)
rt(90)
fd(10)
rt(45)
fd(10)
lt(45)
fd(50)    ## PUNTA DE NARIZ
lt(5)
penup()
fd(70)
lt(45)
pendown()
fd(25)
rt(30)##########>>>>>>>>>>>>>>>
fd(15)
lt(55)
fd(9)
rt(90)
fd(9)
rt(90) ## ojo
fd(9)
rt(90)
fd(9)
rt(90)
fd(30)

########################################### FIN DEL PROGRAMA
t = Turtle()
t.pencolor('red')
t.setpos(0, 20)

t.rt(90)
t.fd(200)

##############################################
input('ENTER PARA SALIR')


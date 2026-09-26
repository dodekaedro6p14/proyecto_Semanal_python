import turtle as tu


t = tu.Turtle() #Turtle object     roo
s = tu.Screen() #Screen Object      wn
s.bgcolor("black") #Screen Bg color
s.title("Saturday")
t.left(90) #moving the turtle 90 degrees towards left
t.speed(20)#setting the speed of the turtle


def  draw(l): #recursive function taking length 'l' as argument
    if(l<10):
        return
    else:

        t.pensize(1) #Setting Pensize
        t.pencolor("yellow") #Setting Pencolor as yellow
        t.forward(l) #moving turtle forward by 'l'
        t.left(30) #moving the turtle 30 degrees towards left
        draw(3*l/4) #drawing a fractal on the left of the turtle object 'roo' with 3/4th of its length
        t.right(60) #moving the turtle 60 degrees towards right
        draw(3*l/4) #drawing a fractal on the right of the turtle object 'roo' with 3/4th of its length
        t.left(30) #moving the turtle 30 degrees towards left
        t.pensize(1)
        t.backward(l) #returning the turtle back to its original psition

draw (20) # drawing 20 times 

t.right(90)
t.speed(2000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        t.pensize(1)
        t.pencolor("magenta") #magenta
        t.forward(l)
        t.left(30)
        draw(3*l/4)
        t.right(60)
        draw(3*l/4)
        t.left(30)
        t.pensize(1)
        t.backward(l)

draw (20)


t.left(270)
t.speed(2000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        t.pensize(1)
        t.pencolor("red") #red
        t.forward(l)
        t.left(30)
        draw(3*l/4)
        t.right(60)
        draw(3*l/4)
        t.left(30)
        t.pensize(1)
        t.backward(l)

draw (20)

t.right(90)
t.speed(2000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        t.pensize(1)
        t.pencolor('#FFF8DC') #white
        t.forward(l)
        t.left(30)
        draw(3*l/4)
        t.right(60)
        draw(3*l/4)
        t.left(30)
        t.pensize(1)
        t.backward(l)

draw(20)
########################################################

def  draw(l):
    if(l<10):
        return
    else:

        t.pensize(1)
        t.pencolor("lightgreen") #lightgreen
        t.forward(l)
        t.left(30)
        draw(4*l/5)
        t.right(60)
        draw(4*l/5)
        t.left(30)
        t.pensize(1)
        t.backward(l)

draw (40)

t.right(90)
t.speed(2000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        t.pensize(1)
        t.pencolor("red") #red
        t.forward(l)
        t.left(30)
        draw(4*l/5)
        t.right(60)
        draw(4*l/5)
        t.left(30)
        t.pensize(1)
        t.backward(l)

draw (40)


t.left(270)
t.speed(2000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        t.pensize(1)
        t.pencolor("yellow") #yellow
        t.forward(l)
        t.left(30)
        draw(4*l/5)
        t.right(60)
        draw(4*l/5)
        t.left(30)
        t.pensize(1)
        t.backward(l)

draw (40)

t.right(90)
t.speed(2000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        t.pensize(1)
        t.pencolor('#FFF8DC') #white
        t.forward(l)
        t.left(30)
        draw(4*l/5)
        t.right(60)
        draw(4*l/5)
        t.left(30)
        t.pensize(1)
        t.backward(l)

draw (40)

########################################################
def  draw(l):
    if(l<10):
        return
    else:

        t.pensize(1)
        t.pencolor("cyan") #cyan
        t.forward(l)
        t.left(30)
        draw(6*l/7)
        t.right(60)
        draw(6*l/7)
        t.left(30)
        t.pensize(1)
        t.backward(l)

draw (60)

t.right(90)
t.speed(2000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        t.pensize(1)
        t.pencolor("yellow") #yellow
        t.forward(l)
        t.left(30)
        draw(6*l/7)
        t.right(60)
        draw(6*l/7)
        t.left(30)
        t.pensize(1)
        t.backward(l)

draw (60)


t.left(270)
t.speed(2000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        t.pensize(1)
        t.pencolor("magenta") #magenta
        t.forward(l)
        t.left(30)
        draw(6*l/7)
        t.right(60)
        draw(6*l/7)
        t.left(30)
        t.pensize(1)
        t.backward(l)

draw (60)

t.right(90)
t.speed(2000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        t.pensize(1)
        t.pencolor('#FFF8DC') #white
        t.forward(l)
        t.left(30)
        draw(6*l/7)
        t.right(60)
        draw(6*l/7)
        t.left(30)
        t.pensize(1)
        t.backward(l)
draw(60)
input('Enter para salir')

import sys
import turtle
from math import sin,cos

win = turtle.Screen()
win.setup(1000,1000)
win.tracer(0)
win.title('cuatro fantasticos, cuatro_cubos.py')
win.bgcolor('black')
counter = 0
running = True

def close_app():
    global running
    running = False

win.listen()
win.onkey(close_app, 'Escape')

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c

class Cube:
    EDGES = (0,5), (0,7), (0,2), (5,2), (5,7), (1,3), (1,6), (1,4), (3,4), (4,6), (3,6), (2,7)
    VERTICES = [(-1,-1,-1),(1,-1,-1), (1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),( 1,1,1),(-1,1,1)]

    def __init__(self, xpos, ypos, axes, color):
        self.xpos = xpos
        self.ypos = ypos
        self.counter = counter
        self.axes = axes
        self.c = color
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.color(self.c)

    def draw(self):

        for edge in self.EDGES:
            points = []
            
            for vertex in edge:
                x,y,z = self.VERTICES[vertex]

                if self.axes == '3':
                    x,z = rotate(x,z,self.counter) # Only this one to rotate around y
                    y,z = rotate(y,z,self.counter) # Only this for x
                    x,y = rotate(x,y,self.counter) # This for z
                    
                elif self.axes == 'x':
                    z,y = rotate(z,y,self.counter) # defecto y,z
                elif self.axes == 'y':
                    x,z = rotate(x,z,self.counter)
                elif self.axes == 'm':
                    x,y = rotate(x,y,self.counter)

            
                z += 5
                if z != 0:
                    f = 200/(z)
               
                sx, sy = x*f,y*f
                points.append(sx)
                points.append(sy)

            self.t.up()
            self.t.goto(points[0]+self.xpos, points[1]+self.ypos)
            self.t.down()
            self.t.goto(points[2]+self.xpos, points[3]+self.ypos)
            self.t.up()

# Cube( where on x, where on y, choose axis x,y,z or all 3)
cube = Cube(0,-105,'x', '#00FF00') #lime #00FF00
cube2 = Cube(105, 0,'y', 'red')
cube3 = Cube(-105, 0, 'y', 'yellow')
cube4 = Cube(0,105,'x', 'blue')
cube5 = Cube(0, 0, '3', 'white')

cube_list = (cube, cube2, cube3, cube4, cube5)

try:
    while running:
        for i in cube_list:
            i.t.clear()
            i.draw()
     
        win.update()
        cube.counter  += 0.015 ## lime
        cube2.counter += 0.015 ## red
        cube3.counter -= 0.015 ## yellow
        cube4.counter -= 0.015 ## blue
        cube5.counter -= 0.015

except turtle.Terminator:
    pass

sys.exit()

######3     insertando flores
def medicircle():
    for i in range(90):
        fd(1.5)
        rt(1)

def petal():
    for i in range(2):
        medicircle()
        rt(90)

def flohead():
    pencolor('white')
    for i in range(12):
        petal()
        rt(30)

input('Enter para salir de aqui')

import sys
import turtle
from math import sin,cos

win = turtle.Screen()
win.title('cubo_2.py')
win.setup(1000,1000)
win.tracer(0)

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
    EDGES = (0,5), (0,7), (0,2), (5,2),(5,7), (1,3), (1,6), (1,4),(3,4), (4,6), (3,6), (2,7)
    VERTICES = [(-1,-1,-1),(1,-1,-1), (1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),( 1,1,1),(-1,1,1)]

    def __init__(self, xpos, ypos,axes, color):
        self.xpos = xpos
        self.ypos = ypos
        self.counter = 0
        self.axes = axes
        self.c = color
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.color(self.c)
        self.distance = 300
        ##self._onkeyrealease(win.bye, 'p')
        

    def draw(self):
        for edge in self.EDGES:
            points = []
            
            for vertex in edge:
                x,y,z = self.VERTICES[vertex]

                if self.axes == '3':
                    x,z = rotate(x,z,self.counter) 
                    y,z = rotate(y,z,self.counter) 
                    x,y = rotate(x,y,self.counter) 
                    
                elif self.axes == 'x':
                    y,z = rotate(y,z,self.counter) 
                elif self.axes == 'y':
                    x,z = rotate(x,z,self.counter)
                elif self.axes == 'z':
                    x,y = rotate(x,y,self.counter)
            
                z += 5
                if z != 0:
                    f = self.distance/(z)
               
                sx, sy = x*f,y*f
                points.append(sx)
                points.append(sy)

            self.t.up()
            self.t.goto(points[0]+self.xpos, points[1]+self.ypos)
            self.t.down()
            self.t.goto(points[2]+self.xpos, points[3]+self.ypos)
            self.t.up()
            ##self.onkey(win.bye, 'p')

def move_up():
    for i in cube_list:
        if i.ypos <= 450:
            i.ypos += 50

def move_down():
    for i in cube_list:
        if i.ypos>=-450:
            i.ypos-=50

def move_right():
    for i in cube_list:
        if i.xpos<450:
            i.xpos += 50

def move_left():
    for i in cube_list:
        if i.xpos>=-450:
            i.xpos -= 50

def move_in():
    cube1.distance += 50
    cube2.distance += 20

def move_out():
    cube1.distance -= 50
    cube2.distance -= 30

# Cube(x,y,axes - x,y,z or 3 ,color)
cube1 = Cube(0,0,'3', 'cyan')
cube2 = Cube(0,0, '3', 'red')
cube2.distance = 250
cube1.distance = 500

cube_list = [cube1, cube2]

win.onkey(move_up, 'w')
win.onkey(move_down, 's')
win.onkey(move_right, 'd')
win.onkey(move_left, 'a')
win.onkey(move_in, 'q')
win.onkey(move_out, 'e')
win.onkey(win.bye, 'p')   ## creando el boton para salir2 


try:
    while running:
        cube1.t.clear()
        cube1.draw()
        cube2.t.clear()
        cube2.draw()
 
        win.update()
        cube1.counter -= 0.005
        cube2.counter += 0.020   
except turtle.Terminator:
    pass
sys.exit()
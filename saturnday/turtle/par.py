
import turtle
import time
from math import sin,cos

win = turtle.Screen()
win.setup(1000,1000)
win.tracer(0)
win.title('par.py')
win.bgcolor('black')
win.listen()
counter = 0

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c

class Cube:
    EDGES = (0,1), (1,2), (2,3), (3,0),(4,5), (5,6), (6,7), (7,4),(0,4), (1,5), (2,6), (3,7)
    VERTEXES = [(-1,-1,-1),(1,-1,-1), (1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),( 1,1,1),(-1,1,1)]

    def __init__(self, xpos, ypos, counter,axes, color):
        self.xpos = xpos
        self.ypos = ypos
        self.counter = counter
        self.axes = axes
        self.c = color
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.color(self.c)
        self.distance = 300
        self._clear = win.onkey(win.bye,'p')

    def draw(self):
        for edge in self.EDGES:
            points = []
            
            for vertex in edge:
                x,y,z = self.VERTEXES[vertex]

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

    def move_up(self):
        if self.ypos <= 450:
            self.ypos += 50

    def move_down(self):
        if self.ypos>=-450:
            self.ypos-=50

    def move_right(self):
        if self.xpos<450:
            self.xpos += 50

    def move_left(self):
        if self.xpos>=-450:
            self.xpos -= 50

    def move_in(self):
        if self.distance<1000:
            self.distance+=50

    def move_out(self):
        if self.distance>50:
            self.distance-= 50

# Cube(x,y,counter,axes,color)
cube = Cube(0,0,counter,'3', 'cyan')

win.onkey(cube.move_up, 'w')
win.onkey(cube.move_down, 's')
win.onkey(cube.move_right, 'd')
win.onkey(cube.move_left, 'a')
win.onkey(cube.move_in, 'q')
win.onkey(cube.move_out, 'e')

Run = True
while Run:
    cube.t.clear()
    cube.draw()
    win.update()
    cube.counter += 0.002

    def __init__(self) -> None:
        self.is_run = False
        
        def run(self):
            self.is_run = True
            while self.in_run:
                self.salir = win.bye()
                for salir in self.salir:
                    self.win.mainloops(win.onkey(win.bye, 'p'))
                    Run = False


    
    
    

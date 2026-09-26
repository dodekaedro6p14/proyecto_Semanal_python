
# Jean Joubert 14 April 2020
# Simple program to rotate cube in 3D space

import turtle
from math import sin,cos

win = turtle.Screen()
win.setup(1000,1000)
win.tracer(0)
win.listen()
counter = 0

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c

class Cube:
    EDGES = [(0,1), (1,2), (2,3), (3,0),\
             (0,4), (1,5), (2,6), (3,7), \
             (4,5), (5,6), (6,7), (7,4), \
             (4,8), (5,9), (6,10), (7,11), \
             (8,9), (9,10),(10,11),(11,8),\
             (0,12),(1,12),(2,12),(3,12), 
             (8,13),(9,13),(10,13),(11,13)] # Add on top/bottom pyramid sides
    
    VERTICES = [(-1,2,1),(1,2,1),(1,2,-1), (-1,2,-1),\
                (-2,0,2), (2,0,2),(2,0,-2),(-2,0,-2),\
                (-1,-2,1),(1,-2,1),(1,-2,-1),(-1,-2,-1),\
                (0,3,0),(0,-3,0)] # Add on 2 points at top and bottom to add pyramid

    def __init__(self, xpos, ypos, axes, color):
        self.xpos = xpos
        self.ypos = ypos
        self.counter = counter
        self.axes = axes
        self.c = color
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.color(self.c)
        self.distance = 300

    def draw(self):

        for edge in self.EDGES:
            points = []
            
            for vertex in edge:
                x,y,z = self.VERTICES[vertex]

                if self.axes == '3':
                    x,z = rotate(x,z,self.counter) # Only this one to rotate 
                    y,z = rotate(y,z,self.counter) # Only this for x
                    x,y = rotate(x,y,self.counter) # This for z
                    
                elif self.axes == 'x':
                    y,z = rotate(y,z,self.counter) # Only this for x
                elif self.axes == 'y':
                    x,z = rotate(x,z,self.counter)
                elif self.axes == 'z':
                    x,y = rotate(x,y,self.counter)
            
                z += 5
                if z != 0:
                    f = self.distance/(z)
               
                sx, sy = x*f,y*f
                points.append((sx,sy))

            self.t.up()
            self.t.goto(points[0][0]+self.xpos, points[0][1]+self.ypos)
            self.t.down()
            self.t.goto(points[1][0]+self.xpos, points[1][1]+self.ypos)
            self.t.goto(points[0][0]+self.xpos, points[0][1]+self.ypos)
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


# Cube(x,y,axes,color)
cube = Cube(0,0,'3', 'blue')


win.onkey(cube.move_up, 'w')
win.onkey(cube.move_down, 's')
win.onkey(cube.move_right, 'd')
win.onkey(cube.move_left, 'a')
win.onkey(cube.move_in, 'q')
win.onkey(cube.move_out, 'e')


while True:
    cube.t.clear()
    cube.draw()
 
    win.update()
    cube.counter += 0.008
    
    
    

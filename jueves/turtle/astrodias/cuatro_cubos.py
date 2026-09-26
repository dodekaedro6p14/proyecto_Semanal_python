
# Jean Joubert 14 April 2020
# Simple program to rotate cube in 3D space

import turtle
from math import sin,cos

win = turtle.Screen()
win.setup(1000,1000)
win.tracer(0)
counter = 0

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c

class Cube:
    EDGES = (0,1), (1,2), (2,3), (3,0),(4,5), (5,6), (6,7), (7,4),(0,4), (1,5), (2,6), (3,7)
    VERTICES = [(-1,-1,-1),(1,-1,-1), (1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),( 1,1,1),(-1,1,1)]

    def __init__(self, xpos, ypos,axes, color):
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
                    y,z = rotate(y,z,self.counter) # Only this for x
                elif self.axes == 'y':
                    x,z = rotate(x,z,self.counter)
                elif self.axes == 'z':
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
cube = Cube(0,-100,'z', 'blue')
cube2 = Cube(300,-100,'y', 'red')
cube3 = Cube(-300, -100, 'x', 'green')
cube4 = Cube(0,200,'3', 'black')

cube_list = (cube, cube2, cube3, cube4)

while True:
    for i in cube_list:
        i.t.clear()
        i.draw()
 
    win.update()
    cube.counter += 0.005
    cube2.counter+= 0.010
    cube3.counter += 0.015
    cube4.counter += 0.015
   

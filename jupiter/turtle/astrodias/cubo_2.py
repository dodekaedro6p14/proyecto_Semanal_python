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
    EDGES = (0,1), (1,2), (2,3), (3,0),(4,5), (5,6), (6,7), (7,4),(0,4), (1,5), (2,6), (3,7)
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
cube1 = Cube(0,0,'3', 'blue')
cube2 = Cube(0,0, 'y', 'red')
cube2.distance = 300
cube1.distance = 500

cube_list = [cube1, cube2]

win.onkey(move_up, 'w')
win.onkey(move_down, 's')
win.onkey(move_right, 'd')
win.onkey(move_left, 'a')
win.onkey(move_in, 'q')
win.onkey(move_out, 'e')

while True:
    cube1.t.clear()
    cube1.draw()
    cube2.t.clear()
    cube2.draw()
 
    win.update()
    cube1.counter += 0.005
    cube2.counter += 0.020
    
input("Enter para salir")    
    

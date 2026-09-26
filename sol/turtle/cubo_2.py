import turtle
from math import sin,cos

win = turtle.Screen()
win.setup(720,1080)
win.tracer(0)
win.title('metatron')
win.listen()
counter = 0
win.bgcolor("black")

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c
 
class Cube:
    VERTICES = [(-1,-1,-1),(1,-1,-1), (1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),( 1,1,1),(-1,1,1)]

    EDGES = (1,3),(1,6),(3,4),(4,1),(4,6),(6,3),(7,0),(7,5),(7,2),(0,5),(0,2),(5,2)
    def __init__(self, xpos, ypos,axes, color):
        self.xpos = xpos
        self.ypos = ypos
        self.counter = 0
        self.axes = axes
        self.c = color
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.color(self.c)
        self.distance = 100 #300

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
                    y,z = rotate(y,z,self.counter) # Only this for x
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
cube1 = Cube(0,0,'3', '#9403D3')
cube2 = Cube(0,0, '3', '#FF00FF')  #y
cube3 = Cube(0,0, '3', '#4B0082')
cube2.distance = 100 ##300
cube1.distance = 200
cube3.distance = 400

cube_list = [cube1, cube2, cube3]

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
    cube3.t.clear()
    cube3.draw()
 
    win.update()
    cube1.counter += 0.005
    cube2.counter -= 0.005
    cube3.counter += 0.007   

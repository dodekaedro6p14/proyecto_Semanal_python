import turtle
from math import sin,cos

win = turtle.Screen()
win.setup(720,1080)
win.tracer(0)
win.title('ajna.py')
win.listen()
counter = 0
win.bgcolor("black")

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c
 
class Cube:
    VERTICES = [(-1,-1,-1),(1,-1,-1), (1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),( 1,1,1),(-1,1,1),
    # CUBO A =    8              9              10             11             12             13              14             15
                (-1.5,0.5,1.5),(-0.5,0.5,1.5),(-0.5,1.5,1.5),(-1.5,1.5,1.5),(-1.5,1.5,0.5),(-0.5,1.5,0.5),(-0.5,0.5,0.5),(-1.5,0.5,0.5),
    # CUBO B =    16          17        18         19           20         21         22         23 
                (-1,-1.5,1),(0,-1.5,1),(0,-0.5,1),(-1,-0.5,1),(-1,-0.5,0),(0,-0.5,0),(0,-1.5,0),(-1,-1.5,0),
    # CUBO C =    24             25             26              27             28            29             30            31
                (0.5,0.5,-0.5),(0.5,-0.5,-0.5),(1.5,-0.5,-0.5),(1.5,0.5,-0.5),(0.5,0.5,0.5),(1.5,0.5,0.5),(1.5,-0.5,0.5),(0.5,-0.5,0.5)]

    EDGES = (12,8),(12,14),(14,8),(8,10),(14,10),(10,12),(19,21),(19,17),(19,23),(23,17),(23,21),(21,17),(28,27),(28,25),(28,30),(27,25),(27,30),(30,25)

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
cube1 = Cube(0,0,'3', '#FF00FF')
#cube2 = Cube(0,0, '3', '#9403D3')  #y
#cube3 = Cube(0,0, '3', '#4B0082')
#cube2.distance = 100 ##300
cube1.distance = 350
#cube3.distance = 400

#cube_list = [cube1, cube2]

win.onkey(move_up, 'w')
win.onkey(move_down, 's')
win.onkey(move_right, 'd')
win.onkey(move_left, 'a')
win.onkey(move_in, 'q')
win.onkey(move_out, 'e')

while True:
    cube1.t.clear()
    cube1.draw()
#    cube2.t.clear()
#    cube2.draw()
#    cube3.t.clear()
#    cube3.draw()
 
    win.update()
    cube1.counter += 0.005 # 0.005
#    cube2.counter -= 0.005
#    cube3.counter += 0.007   

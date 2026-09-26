# Jean Joubert 14 April 2020
# Simple rotation of 3d pyramid
import turtle
from math import sin,cos

win = turtle.Screen()
win.setup(600,600)
win.title("Demostracion de navidad")
win.bgcolor('black')
win.tracer(0)
counter = 0

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c
 
class Cube:
    VERTICES = (-1,-1,-1),(-1,1,-1),(1,1,-1),(1,-1,-1),(-1,-1,1),(-1,1,1),(1,1,1),(1,-1,1)
    EDGES = (0,7),(0,5),(0,2),(7,2),(2,5),(5,7),(1,6),(3,4),(1,3),(1,4),(6,3),(6,4)

    def __init__(self):
        self.counter = 0
        self.t = turtle.Turtle()
        self.p = turtle.Turtle()
        self.t.ht()
        self.t.color('green', 'orange')
        self.t.begin_fill()
        self.p.color('white')
        self.t.begin_fill()

    def draw(self):

        for edge in self.EDGES:
            points = []
            
            for vertex in edge:
                x,y,z = self.VERTICES[vertex]
                x,z = rotate(x,z,self.counter)
                y,z = rotate(y,z,self.counter)
                x,y = rotate(x,y,self.counter)
                
                z += 5
                if z != 0:
                    f = 400/(z)##z
               
                sx, sy = x*f,y*f
                points.append(sx)
                points.append(sy)

            self.t.up()
            self.t.goto(points[0], points[1])
            self.t.down()
            self.t.goto(points[2], points[3])
            self.t.up()
            self.p.ht()
            self.p.up(); self.p.goto(points[0], points[-1]); self.p.down()
            self.p.dot(10, 'blue')
            self.p.circle(5)
            ###
            ### invento
            ###
            self.p.up(); self.p.goto(points[-2], points[3]); self.p.down()
            self.p.dot(10, 'red')
            self.p.circle(5)
#           ##
            self.p.up(); self.p.goto(points[3], points[0]); self.p.down()
            self.p.dot(10, 'yellow')
            self.p.circle(5)
            ###
            ####
            self.t.end_fill()
            self.p.up(); self.p.goto(-100, -300); self.p.down()
            self.p.write('Esto es un texto ', True, align='left', font=('Arial', 20, 'normal'))


cube = Cube()
while True:
    cube.t.clear()
    cube.p.clear()
    cube.draw()
    win.update()
    cube.counter += 0.005 ## +=0.005 

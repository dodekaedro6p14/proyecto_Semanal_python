import turtle
import datetime
from math import sin,cos

win = turtle.Screen()
win.setup(600,600)
win.title("Demostracion pame.py")
win.bgcolor('black') ##CCFF99
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
        self.t    = turtle.Turtle()
        self.p    = turtle.Turtle()
        self.date = turtle.Turtle()
        self.t.ht()
        self.date.ht()
        self.t.color('orange')
        self.date.color('red')

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
#            self.t.up()
#            self.p.ht()
#            self.p.up(); self.p.goto(points[0], points[-1]); self.p.down()
#            self.p.dot(10, 'blue')
#            self.p.circle(5)
            ###
            ### invento
            ###
#            self.p.up(); self.p.goto(points[-2], points[3]); self.p.down()
#            self.p.dot(10, 'red')
#            self.p.circle(5)
            ###
            ####
            x = datetime.datetime.now()
            self.date.up(); self.date.goto(-200, 200); self.date.down()
            self.date.write(x.strftime("%c"), True, align = 'left', font=('Arial', 14, 'normal'))
            ### nueva materia
def circle():
    turtle.up(); turtle.goto(-4, 152); turtle.down()
    turtle.pencolor('red')
    for i in range(360):
        turtle.forward(2.7)
        turtle.right(1)
        turtle.ht()

circle()
cube = Cube()
while True:
    cube.t.clear()
    cube.p.clear()
    cube.date.clear()
    cube.draw()
    win.update()
    cube.counter += 0.005 ## +=0.005 
#    win.onkey(win.bye, 'ESC')
    turtle.ht()
if __name__ == '__menu__':
    app = cube()
    app.run()

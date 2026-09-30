import sys
import turtle
from math import sin,cos

win = turtle.Screen()
win.setup(600,600)
win.tracer(0)
win.title('Copo de nieve "nano_copo.py"')
win.bgcolor('black')
#counter = 0
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
    EDGES = (0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),##(0,4),(1,5),(2,6),(3,7)
    VERTEXES = [(-1,-1,-1),(-1,1,-1),(1,1,-1),(1,-1,-1),(-1,-1,1),(-1,1,1),( 1,1,1),(1,-1,1), (0, 0, 0)]

    def __init__(self):
        self.counter = 0
        self.t = turtle.Turtle()
        self.m = turtle.Turtle()
        self.t.ht()
        self.m.ht()
        #self.m.color('cyan')

        self.ball = turtle.Turtle()
        self.ball.color('red')
        self.ball.shape('circle')
        self.ball.up()
        self.ball.dx = 2.7
        self.ball.dy = -2.5


    def draw(self):
        for edge in self.EDGES:
            points = []            
            
            for vertex in edge:
                x,y,z = self.VERTEXES[vertex]
                x,z = rotate(x,z,self.counter) # Only this one to rotate around y
                y,z = rotate(y,z,self.counter) # Only this for x
                x,y = rotate(x,y,self.counter) # This for z                            
                z += 5
                if z != 0:
                    f = 500/(z)               

                sx, sy = x*f,y*f
                points.append(sx)
                points.append(sy)
            
            self.t.up()
            self.t.pensize(0.5)
            self.t.pencolor('white')
            self.t.goto(points[0], points[1])
            self.t.down()
            self.t.goto(points[2], points[3])
#            self.t.goto(points[0][0], points[0][1])
            self.t.up()
            self.m.ht(); self.m.goto(points[0], points[1]); self.m.down()
            self.m.dot(30, 'yellow')
            #self.m.circle(30) # tsmano de la circunferencia 

cube = Cube()
try:
    while running:
        cube.t.clear()
        cube.m.clear()
        cube.draw()
        win.update()
        cube.counter += 0.005

except turtle.Terminator:
    pass
sys.exit()
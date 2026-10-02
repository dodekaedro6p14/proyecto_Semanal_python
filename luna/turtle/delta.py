import sys
import turtle
from math import sin,cos

win = turtle.Screen()
win.bgcolor('black')
win.title('DELTA.py')
win.setup(600,600)
win.tracer(0)
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
    VERTICES = [(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),( 1,1,1),(-1,1,1),
    #delta cubo     #8           #9              #10             #11        
                ( 0.4,  0, 0),(0.5,-0.2,-0.1),(0.4,-0.4,0),( 0.3,-0.2, 0.1),
                (-0.2,-0.4,0),(-0.3,-0.2,0.1),(-0.2, 0, 0),(-0.1,-0.2,-0.1),
    # RECTANGULO b  #16          #17              #18             #19
                (-0.2,-0.4,0.3),(-0.4,-0.4,0.3),(-0.5,-0.2,0.4),(-0.3,-0.2,0.4),
                ( 0.1,0.3,-0.1),(-0.1,0.3,-0.1),(-0.2, 0.5,0.0),( 0.0, 0.5,0.0),
    # rectangulo C #24           #25              #26             #27                  
                ( 0.4,-0.4,-0.3),(0.2,-0.4,-0.3),( 0.3,-0.2,-0.4),(0.5,-0.2,-0.4),
                (   0, 0.3, 0.1),(-0.2, 0.3, 0.1),(-0.1, 0.5, 0.0),(0.1,0.5, 0.0)]

    EDGES = [(8,9),(9,10),(10,11),(11,8),(12,13),(13,14),(14,15),(15,12),
             (12,10),(13,11),(14,8),(15,9),
             (16,17),(17,18),(18,19),(19,16),(20,21),(21,22),(22,23),(23,20),
             (23,19),(18,22),(20,16),(21,17),
             (24,25),(25,26),(26,27),(27,24),(28,29),(29,30),(30,31),(31,28), 
             (28,24),(29,25),(30,26),(31,27)]

    def __init__(self, xpos, ypos, axes, color):
        self.t = turtle.Turtle()
        self.t.ht()
        self.xpos = xpos
        self.ypos = ypos
        self.counter = counter
        self.axes = axes
        self.c = color
        self.t.color(self.c)
        self.distance = 900

    def draw(self):      
        for edges in self.EDGES:
            points = []            
            for vertex in edges:
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
                    x,y = rotate(x,yself.counter)
       
                z += 5
                if z != 0:
                    f = self.distance/(z)
               
                sx, sy = x*f,y*f
                points.append(sx)
                points.append(sy)
                
            self.t.up()
            self.t.goto(points[0] + self.xpos, points[1]+self.ypos)
            self.t.down()
            self.t.goto(points[2] + self.xpos, points[3]+self.ypos)
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


#   Cube(x, y, axes, color)
cube = Cube(0,0, 'x', '#FF1493')

win.onkey(cube.move_up, 'w')
win.onkey(cube.move_down, 's')
win.onkey(cube.move_right, 'd')
win.onkey(cube.move_left, 'a')
win.onkey(cube.move_in, 'q')
win.onkey(cube.move_out, 'e')
win.onkey(win.bye, 'p')

try:
    while running:
        cube.t.clear()
        cube.draw()
        win.update()
        cube.counter += 0.005    

except turtle.Terminator:
    pass

sys.exit()
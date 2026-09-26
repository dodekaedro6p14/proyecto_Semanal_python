import turtle
from math import sin,cos

win = turtle.Screen()
win.bgcolor('black')
win.title('demostracion program ana.py')
win.setup(600,600)
win.tracer(0)
win.listen()
counter = 0

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c
 
class Cube:
    VERTICES = [(-1,-1,-1),(1,-1,-1), (1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),( 1,1,1),(-1,1,1)]
    EDGES = [(0,7),(5,2),(0,5),(7,2),(0,2),(7,5),
             (1,6),(1,4),(1,3),(4,3),(4,6),(6,3) ]

    def __init__(self, xpos, ypos, axes, color):
        self.t = turtle.Turtle()
        self.t.ht()
#        self.t.color('#FF1493')
        self.xpos = xpos
        self.ypos = ypos
        self.counter = counter
        self.axes = axes
        self.c = color
        self.t.color(self.c)
        self.distance = 300

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
cube = Cube(0,0, '3', '#FF1493')

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
    cube.counter += 0.0005    

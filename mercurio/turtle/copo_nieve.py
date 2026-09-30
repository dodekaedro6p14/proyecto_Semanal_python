import sys
import turtle
from math import sin,cos

win = turtle.Screen()
win.title('copo_nieve.py')
win.setup(800,800)
win.tracer(0)
win.listen()
win.bgcolor('black')

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
    EDGES = [(10,16), (0,9), (0,8), (8,10), (9,10), (34,28), (22,52), (40,46), (13,12), (13,11),
             ( 6,14),( 6,15),(14,16),(15,16),(17,19),(18,19),
             (24,25),(23,25),(22,21),(20,22),( 3,20),( 3,21),
             (29,31),(30,31),(26, 7),(27, 7),(28,27),(28,26),
             (35,37),(36,37),(32,34),(33,34),(33, 1),(32, 1),
             (43,41),(43,42),(40,38),(40,39),(38, 2),(39, 2),
             (46,44),(46,45),(44, 4),(45, 4),(47,49),(48,49),
             (52,50),(52,51),(50, 5),(51, 5),(53,55),(54,55)]
    VERTICES = [(-1,-1,-1),(1,-1,-1), (1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),( 1,1,1),(-1,1,1),
        #
      (-0.7,-0.85,-1), (-1,-0.85,-0.7), (-0.7,-0.7,-0.7), (-0.6,-0.43,-0.25), (-0.25,-0.43,-0.6), (-0.3,-0.3,-0.3),
        # 14            # 15            #   16              #   17              #   18              #   19        
      ( 0.7, 0.85, 1), ( 1, 0.85, 0.7), ( 0.7, 0.7, 0.7), ( 0.6, 0.43, 0.25), ( 0.25, 0.43, 0.6), ( 0.3, 0.3, 0.3),
        #   20          #   21          #   22              #   23              #   24              #   25
      (-0.7, 0.85,-1), (-1, 0.85,-0.7), (-0.7, 0.7,-0.7), (-0.6, 0.43,-0.25), (-0.25, 0.43,-0.6), (-0.3, 0.3,-0.3),        
        #   26          #   27          #   28              #   29              #   30              #   31
      (-0.7, 0.85, 1), (-1, 0.85, 0.7), (-0.7, 0.7, 0.7), (-0.6, 0.43, 0.25), (-0.25, 0.43, 0.6), (-0.3, 0.3, 0.3),
        #   32          #   33          #   34              #   35              #   36              #   37
      ( 0.7,-0.85,-1), ( 1,-0.85,-0.7), ( 0.7,-0.7,-0.7), ( 0.6,-0.43,-0.25), ( 0.25,-0.43,-0.6), ( 0.3,-0.3,-0.3),
        #   38          #   39          #   40              #   41              #   42              #   43
      ( 0.7, 0.85,-1), ( 1, 0.85,-0.7), ( 0.7, 0.7,-0.7), ( 0.6, 0.43,-0.25), ( 0.25, 0.43,-0.6), ( 0.3, 0.3,-0.3),      
        #   44          #   45          #   46              #   47              #   48              #   49
      (-0.7,-0.85, 1), (-1,-0.85, 0.7), (-0.7,-0.7, 0.7), (-0.6,-0.43, 0.25), (-0.25,-0.43, 0.6), (-0.3,-0.3, 0.3),
        #   50          #   51          #   52              #   53              #   54              #   55
      ( 0.7,-0.85, 1), ( 1,-0.85, 0.7), ( 0.7,-0.7, 0.7), ( 0.6,-0.43, 0.25), ( 0.25,-0.43, 0.6), ( 0.3,-0.3, 0.3)]

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
        ##self._onkeyrealease(win.bye, 'p')
        

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
            ##self.onkey(win.bye, 'p')

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
cube1 = Cube(0,0,'3', 'cyan')
cube2 = Cube(0,0, '3', 'red')
cube2.distance = 250
cube1.distance = 500

cube_list = [cube1]

win.onkey(move_up, 'w')
win.onkey(move_down, 's')
win.onkey(move_right, 'd')
win.onkey(move_left, 'a')
win.onkey(move_in, 'q')
win.onkey(move_out, 'e')

try:
    while running:
        cube1.t.clear()
        cube1.draw()
        cube2.t.clear()
        cube2.draw()
 
        win.update()
        cube1.counter -= 0.001
        cube2.counter += 0.020

except turtle.Terminator:
    pass
sys.exit()
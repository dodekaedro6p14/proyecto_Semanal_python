import turtle
from math import sin,cos

win = turtle.Screen()
win.title('DODEKAEDRO.py')
win.setup(1000,1000)
win.tracer(0)
win.listen()
win.bgcolor('black')
counter = 0

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c
 
class Cube:
    EDGES = [(0,1),(1,2),(2,3),(3,4),(4,0),
             (5,6),(6,7),(7,8),(8,9),(9,5),
             (10,11),(11,12),(12,13),(13,14),(14,15),(15,16),(16,17),(17,18),(18,19),(19,10),
             (0,16),(1,14),(2,12),(3,10),(4,18),(5,13),(6,15),(7,17),(8,19),(9,11)]
    ###            punt=0          p1              p2          p3          p4
    VERTICES = [(-0.6,-1.1,-0.8),(0.6,-1.1,-0.8),(1,-1.1,0.3),(0,-1.1,1),(-1,-1.1,0.3),
    ###            punto=5      p6          p7              p8              p9
                (1,1.1,-0.3),( 0,1.1,-1),(-1,1.1,-0.3), (-0.6,1.1,0.8), (0.6,1.1,0.8),
    ###         Puntos 10      p11         p12            p13         p14
                (0,-0.2,1.6),(1,0.2,1.2),(1.6,-0.2,0.6),(1.6,0.2,-0.6),(1,-0.2,-1.2),
    ###         punto 15        p16           p17          p18          p19
                (0,0.2,-1.6),(-1,-0.2,-1.2),(-1.6,0.2,-0.6),(-1.6,-0.2,0.6),(-1,0.2,1.2)]

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
    cube2.distance += 30
    cube3.distance += 70

def move_out():
    cube1.distance -= 50
    cube2.distance -= 30
    cube3.distance -= 70

# Cube(x,y,axes - x,y,z or 3 ,color)
cube1 = Cube(0,0,'x', 'yellow')
cube2 = Cube(0,0, 'y', 'red')
cube3 = Cube(0,0, '3', 'cyan')
cube2.distance = 180
cube1.distance = 250
cube3.distance = 360

cube_list = [cube1, cube2, cube3] ## def cubo2

win.onkey(move_up, 'w')
win.onkey(move_down, 's')
win.onkey(move_right, 'd')
win.onkey(move_left, 'a')
win.onkey(move_in, 'q')
win.onkey(move_out, 'e')
win.onkey(win.bye, 'p')   ## creando el boton para salir2 

while True:
    cube1.t.clear()
    cube1.draw()
    cube2.t.clear()
    cube2.draw()
#    cube3.t.clear()
#    cube3.draw()
 
    win.update()
    cube1.counter -= 0.005  ##DEF 0.005
    cube2.counter += 0.020   
#    cube3.counter += 0.002
    ##win.onkeyrelease(win.bye, 'p')## boton para salir
if __name__ == "__main__":
   Cube() 

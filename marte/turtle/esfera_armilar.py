import turtle
from math import sin,cos

win = turtle.Screen()
win.title('ESFERA ARMIl4R')
win.setup(1000,1000)
win.tracer(0)
win.listen()
win.bgcolor('black')
counter = 0

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c
 
class Cube:
            #   ESTRELLA
    EDGES = [#(0,2),(0,5),(0,8),(0,11),(1,2),(1,5),(1,8),(1,11),
             #(0,3),(0,4), #(0,6),(0,7),
             #(1,9),(1,10),(1,12),(1,13),
            #   ESFERA
            (3,4),(4,5),(5,6),(6,7),(7,8),
    (8,9),(9,10),(10,11),(11,12),(12,13),(13,2),(2,3)]
                 #0-[0]     1-[#13] 
    VERTICES = [(-2,0,2),   (2, 0,-2),
                ##########################
                  #2-[#12]              3-[#1]              4-[#2]            
                (-1,0,-1), (-0.889,0.443,-0.889), (-0.443,0.889,-0.443),
                  #5-[-#6]              6-[-#7]              7-[-#8]     
                ( 0,1, 0), (0.443,0.889,0.443),  (0.889,0.443,0.889),

                ##############################
                  #8-[#3]            9-[#4]            10-[#5]            
                (1, 0,1), (0.889,-0.443,0.889), (0.443,-0.889,0.443),
                  #11-[-#9]         12-[-#10]        13-[-#11]
                (0,-1,0), (-0.443,-0.889,-0.443), (-0.889,-0.443,-0.889)]

    def __init__(self, xpos, ypos,axes, color):
        self.xpos = xpos
        self.ypos = ypos
        self.counter = 0
        self.axes = axes
        self.c = color
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.pensize(0.5)
        self.t.circle(30)
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
    cube3.distance += 80

def move_out():
    cube1.distance -= 50
    cube2.distance -= 20
    cube3.distance -= 80

# Cube(x,y,axes - x,y,z or 3 ,color)
cube1 = Cube(0,0, '3', 'cyan')
cube2 = Cube(0,0, '3', 'red')
cube3 = Cube(0,0, '3', 'orange')
cube2.distance = 250
cube1.distance = 500
cube3.distance = 750

cube_list = [cube1, cube2, cube3]

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
    cube3.t.clear()
    cube3.draw()
 
    win.update()
    cube1.counter -= 0.001 #nodo normal: 0.005
    cube2.counter += 0.002
    cube3.counter -= 0.003
    ##win.onkeyrelease(win.bye, 'p')## boton para salir
if __name__ == "__main__":
   Cube() 

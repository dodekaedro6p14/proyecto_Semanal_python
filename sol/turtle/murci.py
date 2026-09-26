import turtle
from math import sin,cos

win = turtle.Screen()
win.bgcolor('black')
win.title('Murcielago gira en 3D ')
win.setup(600,600)
win.tracer(0)
win.listen()
counter = 0

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c
 
class Cube:
    VERTICES = [(-1,-1,-1),(1,-1,-1), (1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),( 1,1,1),(-1,1,1),
    # CENTRO cuello  #8       #9            #10         #11            #12
                ( 0, 0,-0.1),( 0, 0,-0.2),(-0.2,0,-0.2),(-0.8,0,-0.8),(-0.2,0,-0.5),
                     #13      #14           #15         #16             #17
                ( 0, 0,-0.8),(0.2,0,-0.5),( 0.8,0,-0.8),( 0.5,0,-0.2),(0.8, 0, 0),
                     #18      #19           #20         #21             #22
                (0.5,0, 0.2),(0.8, 0,0.8),( 0.2,0, 0.5),( 0.2, 0,  0),( 0.1, 0,  0),
                     #23      #24           #25         #26             #27
                (0.1, 0,0.2),(-0.3,0,0.5),(-0.1,0, 0.2),(-0.2,0, 0.1),(-0.4,0, 0.3),
                (-0.2, 0, -0.1)]
    EDGES = [( 8, 9),( 9,10),(10,11),(11,12),(12,13),(13,14),(14,15),(15,16),(16,17),(17,18),
             (18,19),(19,20),(20,21),(21,22),(22,23),(23,24),(24,25),(25,26),(26,27),(27,28),
             (28,8)]

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
        self.distance = 300 # d= 300

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
                    x,y = rotate(x,y,self.counter)
         
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
cube1 =  Cube(0,0, '3', '#FF0080')
cube2 =  Cube(0,0, '3', '#FF00FF')
cube3 =  Cube(0,0, '3', '#8000FF')
cube4 =  Cube(0,0, '3', '#0000FF')
cube5 =  Cube(0,0, '3', '#0080FF')
cube6 =  Cube(0,0, '3', '#00FFFF')
cube7 =  Cube(0,0, '3', '#00FF80')
cube8 =  Cube(0,0, '3', '#00FF00')
cube9 =  Cube(0,0, '3', '#80FF00')
cube10 = Cube(0,0, '3', '#FFFF00')
cube11 = Cube(0,0, '3', '#FF8000')
cube12 = Cube(0,0, '3', '#FF0000')
cube13 = Cube(0,0, '3', '#FF0080') #inicio
cube14 = Cube(0,0, '3', '#FF00FF')
cube15 = Cube(0,0, '3', '#8000FF')
cube16 = Cube(0,0, '3', '#0000FF')
cube17 = Cube(0,0, '3', '#0080FF')
cube18 = Cube(0,0, '3', '#00FFFF')
cube19 = Cube(0,0, '3', '#00FF80')
cube20 = Cube(0,0, '3', '#00FF00')
cube21 = Cube(0,0, '3', '#80FF00')
cube22 = Cube(0,0, '3', '#FFFF00')
cube23 = Cube(0,0, '3', '#FF8000')
cube24 = Cube(0,0, '3', '#FF0000')

cube1.distance = 50
cube2.distance = 100
cube3.distance = 150
cube4.distance = 200
cube5.distance = 250
cube6.distance = 300
cube7.distance = 350
cube8.distance = 400
cube9.distance = 450
cube10.distance= 500
cube11.distance= 550
cube12.distance= 600
cube13.distance= 650
cube14.distance= 700
cube15.distance= 750
cube16.distance= 800
cube17.distance= 850
cube18.distance= 900
cube19.distance= 950
cube20.distance= 1000
cube21.distance= 1050
cube22.distance= 1100
cube23.distance= 1150
cube24.distance= 1200

cube_list = [cube1, cube2, cube3, cube4, cube5,
             cube6,cube7,cube8,cube9,cube10,cube11,cube12,
             cube13,cube14,cube15,cube16,cube17,cube18,cube19,
             cube20,cube21,cube22,cube23,cube24]

win.onkey(move_up, 'w')
win.onkey(move_down, 's')
win.onkey(move_right, 'd')
win.onkey(move_left, 'a')
win.onkey(move_in, 'q')
win.onkey(move_out, 'e')
win.onkey(win.bye, 'p')

while True:
    cube1.t.clear();     cube1.draw()
    cube2.t.clear();     cube2.draw()
    cube3.t.clear();     cube3.draw()
    cube4.t.clear();     cube4.draw()
    cube5.t.clear();     cube5.draw()
    cube6.t.clear();     cube6.draw()
    cube7.t.clear();     cube7.draw()
    cube8.t.clear();     cube8.draw()
    cube9.t.clear();     cube9.draw()
    cube10.t.clear();    cube10.draw()
    cube11.t.clear();    cube11.draw()
    cube12.t.clear();    cube12.draw()
    cube13.t.clear();    cube13.draw()
    cube14.t.clear();    cube14.draw()
    cube15.t.clear();    cube15.draw()
    cube16.t.clear();    cube16.draw()
    cube17.t.clear();    cube17.draw()
    cube18.t.clear();    cube18.draw()
    cube19.t.clear();    cube19.draw()
    cube20.t.clear();    cube20.draw()
    cube21.t.clear();    cube21.draw()
    cube22.t.clear();    cube22.draw()
    cube23.t.clear();    cube23.draw()
    cube24.t.clear();    cube24.draw()

    win.update()
    cube1.counter +=  0.004    
    cube2.counter +=  0.0042
    cube3.counter +=  0.0044
    cube4.counter +=  0.0046
    cube5.counter +=  0.0048
    cube6.counter +=  0.005
    cube7.counter +=  0.0052
    cube8.counter +=  0.0054
    cube9.counter +=  0.0056
    cube10.counter += 0.0058
    cube11.counter += 0.006
    cube12.counter += 0.0062
    cube13.counter += 0.0064
    cube14.counter += 0.0066
    cube15.counter += 0.0068
    cube16.counter += 0.007
    cube17.counter += 0.0072
    cube18.counter += 0.0074
    cube19.counter += 0.0076
    cube20.counter += 0.0078
    cube21.counter += 0.008
    cube22.counter += 0.0082
    cube23.counter += 0.0084
    cube24.counter += 0.0086

if __name__ == "__main__":
    Cube()


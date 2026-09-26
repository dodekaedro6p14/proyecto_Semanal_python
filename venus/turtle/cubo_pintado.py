import turtle
from math import sin,cos

win = turtle.Screen()
win.setup(600,600)
win.tracer(0)
counter = 0
win.title('DODEKAEDRO')
win.bgcolor('black')

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c
 
class Cube:
    VERTICES = [(-1,-1,-1),(1,-1,-1), (1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),( 1,1,1),(-1,1,1)]
    TRIANGLES = [(0,7,2),(0,5,2),(5,7,2),(7,5,0),(6,1,3),(6,4,1),(1,3,4),(3,4,6)]
##    TRIANGLES = [(0,6,1),(6,3,1),(0,3,1),(6,3,0)]    ##,(0,4,3),(4,7,3)]   ## ,(5,4,7),(7,6,5),(7,6,3),(6,2,3),(5,1,2),(2,6,5)]

    def __init__(self):
        self.counter = 0
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.color('lime')
        self.t.fillcolor('#00FA9A')## color de relleno

    def draw(self):        
        for triangle in self.TRIANGLES:
            points = []
            
            for vertex in triangle:
                x,y,z = self.VERTICES[vertex]

                x,z = rotate(x,z,self.counter)
                y,z = rotate(y,z,self.counter)
                x,y = rotate(x,y,self.counter)
                            
                z += 5
                if z != 0:
                    f = 400/(z)
               
                sx, sy = x*f,y*f
                points.append(sx)
                points.append(sy)
                
            self.t.begin_fill()
            self.t.up()
            self.t.goto(points[0], points[1])
            self.t.down()
            self.t.goto(points[2], points[3])
            self.t.goto(points[4], points[5])
            self.t.goto(points[0], points[1])
            self.t.up()
            self.t.end_fill()


cube = Cube()
while True:
    cube.t.clear()
    cube.draw()
    win.update()
    cube.counter += 0.001   ##conteo de vueltas ('0.005')
    
##exitonclick()
##    win.input('Enter para salir')

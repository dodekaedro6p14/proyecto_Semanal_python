import turtle
from math import sin,cos

win = turtle.Screen()
win.setup(600,600)
win.tracer(0)
win.bgcolor('black')
win.title('bs1.py')
counter = 0

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c
 
class Cube:
    EDGES = (0,1), (1,2), (2,3), (3,0),(4,5), (5,6), (6,7), (7,4),(0,4), (1,5), (2,6), (3,7)
    VERTEXES = [(-1,-1,-1),(1,-1,-1), (1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),( 1,1,1),(-1,1,1)]

    def __init__(self, counter):
        self.counter = counter
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.color('white')

        self.ball = turtle.Turtle()
        self.ball.color('red')
        self.ball.shape('circle')
        self.ball.up()
        self.ball.dx = 1.7  # Velocidad de ball
        self.ball.dy = -1.5

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
                    f = 250/(z) # def 500/(z)
               
                sx, sy = x*f,y*f
                points.append((sx,sy))

            self.t.up()
            self.t.goto(points[0][0], points[0][1])
            self.t.down()
            self.t.goto(points[1][0], points[1][1])
            self.t.goto(points[0][0], points[0][1])
            self.t.up()

    def move_ball(self):
        self.ball.goto(self.ball.xcor()+self.ball.dx, self.ball.ycor()+self.ball.dy)
        if self.ball.xcor()>50 or self.ball.xcor()<-50: #def 85
            self.ball.dx *= -1
        if self.ball.ycor()>50 or self.ball.ycor()<-50:
            self.ball.dy *= -1

cube = Cube(counter)
while True:
    cube.t.clear()
    cube.draw()  
    win.update()
    cube.counter += 0.002  ## velocidad del cubo 
    cube.move_ball()  

    win.onkey(win.bye, 'p')

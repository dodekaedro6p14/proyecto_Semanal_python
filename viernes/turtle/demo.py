import turtle
import datetime
from math import sin,cos

win = turtle.Screen()
win.setup(600,600)
win.tracer(0)
win.listen()
win.title('Copo de nieve "nano_copo.py"')
win.bgcolor('black')
counter = 0
#x = datetime.datetime.now()

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c
 
class Cube:
    EDGES = (0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),##(0,4),(1,5),(2,6),(3,7)
    VERTEXES = [(-1,-1,-1),(-1,1,-1),(1,1,-1),(1,-1,-1),(-1,-1,1),(-1,1,1),( 1,1,1),(1,-1,1),(0,0,0)]

    def __init__(self):
        self.counter = 0
        self.t = turtle.Turtle()
        self.m = turtle.Turtle()
        self.date = turtle.Turtle()
        self.t.ht()
        self.m.ht()
        self.date.ht()
        self.m.color('cyan')
        self.date.color('white')

        self.ball = turtle.Turtle()
        self.ball.color('red')
        self.ball.shape('circle')
        self.ball.up()
        self.ball.goto(120,120)
        self.ball.dx = 1.7  # def 2.7
        self.ball.dy = -1.5

    def draw(self):
        for edge in self.EDGES:
            points = []                        
            for vertex in edge:
                x,y,z = self.VERTEXES[vertex]
                x,z = rotate(x,z,self.counter) 
                y,z = rotate(y,z,self.counter) 
                x,y = rotate(x,y,self.counter)                             
                z += 5
                if z != 0:
                    f = 500/(z)               

                sx, sy = x*f,y*f
                points.append(sx)
                points.append(sy)
            
            self.t.up(); self.t.pensize(0.5)
            self.t.pencolor('white')
            self.t.goto(points[0], points[1])
            self.t.down()
            self.t.goto(points[2], points[3])
            self.t.up()

            self.m.ht(); self.m.goto(points[0], points[1]); self.m.down()
            self.m.dot(30, 'yellow')
            x = datetime.datetime.now()
            self.date.up(); self.date.goto(-200, 200); self.date.down()
            self.date.write(x.strftime("%c"), True, align = 'left', font=('Arial', 14, 'normal'))

    def move_ball(self):
        self.ball.goto(self.ball.xcor()+self.ball.dx, self.ball.ycor()+self.ball.dy)
        for i in range(4):
            self.ball.fd(20)
            self.ball.rt(90)
      
 #       if self.ball.xcor()>120 or self.ball.xcor()<-120:
 #           self.ball.dx *= -1
 #       if self.ball.ycor()>120 or self.ball.ycor()<-120:
 #           self.ball.dy *= -1

#    def circle(self):
#        for h in range(360):
#            self.ball.fd(1)
#            self.ball.rt(1)
        
#circle()
cube = Cube()
ran = True
#win.onkey(ran=False, 'p')
while ran:
    cube.t.clear()
    cube.m.clear()
    cube.date.clear()
    cube.draw()
    win.update()
    cube.counter += 0.005
    cube.move_ball()
#    cube.move_ball.clear()
#    cube.circle()
    win.onkey(win.bye, 'p')

if __name__ == '__menu__':
      app = cube()
      app.run()


 

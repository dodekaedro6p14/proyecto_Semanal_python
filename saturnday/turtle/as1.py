import turtle
from tkinter import *
from tkinter import ttk
from math import sin,cos

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="demostracion").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

win = turtle.Screen()
win.setup(600,600)
win.tracer(0)
counter = 0

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c
 
class Cube:
    EDGES = [(0,1), (1,2), (2,3), (3,0),(4,5),(5,6), 
            (6,7), (7,4),(0,4), (1,5), (2,6), (3,7)]
    VERTICES = [(-2,-2,-2),(2,-2,-2),(2,2,-2),(-2,2,-2),
                (-2,-2, 2),(2,-2, 2),(2,2, 2),(-2,2, 2)]

    def __init__(self):
        self.counter = 0
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.color('black')

    def draw(self):
        for edge in self.EDGES:
            points = []       
            for vertex in edge:
                x,y,z = self.VERTICES[vertex]
                x,z = rotate(x,z,self.counter) # Only this one to rotate around y
                y,z = rotate(y,z,self.counter) # Only this for x
                x,y = rotate(y,x,self.counter) # This for z           
                z += 5
                if z != 0:
                    f = 400/(z)  # f gives size/distance (smaller value = smaller cube)
               
                sx, sy = x*f,y*f
                points.append(sx)
                points.append(sy)

            self.t.up()
            self.t.goto(points[0], points[1])
            self.t.down()
            self.t.goto(points[2], points[3])
            self.t.up()

    def draw2(self):
        turtle.circle(60)

cube = Cube()
while True:
    cube.t.clear()
    cube.draw()
    cube.draw2()
    win.update()
    cube.counter += 0.001   #0.005    

input('Enter para salir')
root.mainloop()

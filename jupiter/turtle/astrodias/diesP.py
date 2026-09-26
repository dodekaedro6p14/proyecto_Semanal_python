import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.pencolor("red")
t.speed()


for i in range(10):
  for i in range(2):
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(120)
    #t.forward(100)
  t.right(36)


print("Presione ENTER para salir")
input 
turtle.done()
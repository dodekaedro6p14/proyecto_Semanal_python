import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.title("espiral")
s.bgcolor("black")
t.pencolor("red")

def poligono(lado, n):
    for i in range(n):
        t.fd(lado)
        t.rt(120)

def espiral():
    for i in range (10, 200, 5):
        poligono(i, 3)
        t.rt(10)

    t.hiderturtle()
s.exitonclick()
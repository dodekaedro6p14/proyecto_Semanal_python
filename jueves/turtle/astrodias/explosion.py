import turtle 
import random
import colorsys

s = turtle.Screen()
s.bgcolor('black')
s.title('Explosion de rayos Gamma')
s.tracer(0)

num_particles = 70
particle_speed = 5
particles = []
colors = [colorsys.hsv_to_rgb(h,1,1)
         for h in [i/num_particles
                   for i in range(
                       num_particles)]]

for i in range(num_particles):
    particle = turtle.Turtle()
    particle.shape('circle')
    particle.color(colors[i])
    particle.penup()
    particle.speed(0)
    particle.goto(0,0)
    particle.setheading(random.randint(0, 260))
    particles.append(particle)

while True:
    for particle in particles:
        particle.forward(particle_speed)
        x,y = particle.xcor(), particle.ycor()

        if abs(x)>400 or abs(y)>400:
            particle.goto(0, 0)
            particle.setheading(
                    random.randint(0, 360))

    s.update()
s.onclik(t.end, 'p')
input('Enter')

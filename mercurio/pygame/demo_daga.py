import sys
import pygame as pg
import numpy as np
from math import *

WIDTH, HEIGHT = 1080, 720
pg.init()
pg.display.set_caption("FL0R 0F L0T0 3DD")
WIN = pg.display.set_mode((WIDTH, HEIGHT))
########################## PUNTOS
points = [
#points.append(np.matrix([0, 0, 0]))
    np.matrix([2, 0, 0]),           #0
    np.matrix([-2, 2, 7]),          #1
    np.matrix([0.5, 0.5, 0.5]),     #2
    np.matrix([-1.8, -1.8, -1.8])   #3
]       
projection_matrix = np.matrix([
                    [1, 0, 0],
                    [0, 1, 0],])

projected_points = [[0, 0] for _ in range(len(points))]

def connect_points(i, j, points):
    pg.draw.line(WIN, 'white',(points[i][0], points[i][1]),                                                   (points[j][0], points[j][1]))

    

def draw():
#    pg.draw.circle(WIN, 'red',(WIDTH/2, HEIGHT/2), 5)
#    pg.draw.arc(WIN, 'cyan', ((WIDTH/2, HEIGHT/2), 100, 100))
    pg.display.update()

def fondo(self):
    WIN.fill('black')          
########################## PROGRAMA
def main():
    run = True
    clock = pg.time.Clock()
    
    ESCALA = 50
    CIRCLE_POS = (WIDTH /2,  HEIGHT / 2)
    ANGLE = 0
   
    while run:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                    break

        rotation_z = np.matrix([
               [cos(ANGLE), -sin(ANGLE), 0],
               [sin(ANGLE), cos(ANGLE), 0],
               [0, 0, 1]])

        rotation_y = np.matrix([
               [cos(ANGLE), 0, sin(ANGLE)],
               [0, 1, 0],
               [-sin(ANGLE), 0, cos(ANGLE)]])

        rotation_x = np.matrix([
               [1, 0, 0],
               [0, cos(ANGLE), -sin(ANGLE)],
               [-sin(ANGLE), 0, cos(ANGLE)]])

        ANGLE += 0.01
        i = 0
        for point in points:
            rotated2d = np.dot(rotation_z, point.reshape(3, 1))
            rotated2d = np.dot(rotation_y, rotated2d)
            projected2d = np.dot(projection_matrix, rotated2d)

            x = int(projected2d[0, 0] * ESCALA) + CIRCLE_POS[0]
            y = int(projected2d[1, 0] * ESCALA) + CIRCLE_POS[1]

            projected_points[i] = [x, y]
            pg.draw.circle(WIN, 'cyan', (x,y), 10)
            i += 1
    
        connect_points(1, 2, projected_points)    
        connect_points(0, 2, projected_points)
        connect_points(3, 2, projected_points)

        draw()
        fondo(WIN)
    pg.quit()
    quit()

if __name__ == "__main__":
    main()


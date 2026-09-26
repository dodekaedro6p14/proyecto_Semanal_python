import pygame as pg
import numpy as np
from math import *

WIDTH, HEIGH = 1600, 900
WIN = pg.display.set_mode((WIDTH, HEIGH))
ESCALA = 50
CIRCLE_POS = (WIDTH /2,  HEIGH / 2)
ANGLE = 0
########################## PUNTOS
points = []
points.append(np.matrix([0, 3, 0]))
points.append(np.matrix([2.3, -1.5, -1.5]))
points.append(np.matrix([-2.3, -1.5, -1.5]))
points.append(np.matrix([0, -1.5, 2.6]))

projection_matrix = np.matrix([
                    [1, 0, 0],
                    [0, -1, 0],  
                    [0, 0, 1]])

projected_points = [[n, n] for n in range(len(points))]

def connect_points(i, j, points):
    pg.draw.line(WIN, 'white', (points[i][0], points[i][1]), 
                                    (points[j][0], points[j][1]))
########################## PROGRAMA
clock = pg.time.Clock()
run = True
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
    WIN.fill('black')
    i = 0
    for point in points:
        rotated2d = np.dot(rotation_z, point.reshape(3, 1))
        rotated2d = np.dot(rotation_y, rotated2d)
        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * ESCALA) + CIRCLE_POS[0]
        y = int(projected2d[1][0] * ESCALA) + CIRCLE_POS[1]

        projected_points[i] = [x, y]
        pg.draw.circle(WIN, 'red', (x,y), 5)
        i += 1

    connect_points(1, 2, projected_points)    
    connect_points(2, 3, projected_points)
    connect_points(3, 1, projected_points)
    connect_points(0, 1, projected_points)
    connect_points(0, 2, projected_points)
    connect_points(0, 3, projected_points)

    pg.draw.circle(WIN, 'green',(0,0), 2.5)

    pg.display.update()

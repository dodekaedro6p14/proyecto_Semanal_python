import sys
import pygame as pg
import numpy as np
from math import *

WIDTH, HEIGH = 1600, 900
ESCALA = 50
CIRCLE_POS = (WIDTH /2,  HEIGH / 2)
ANGLE = 0
pg.init()
pg.display.set_caption("PR0Y3CT3D P03S14 3D")
WIN = pg.display.set_mode((WIDTH, HEIGH))
########################## PUNTOS
points = [
    np.matrix([0, 3, 0]),
    np.matrix([2.3, -1.5, -1.5]),
    np.matrix([-2.3, -1.5, -1.5]),
    np.matrix([0, -1.5, 2.6])
]

projection_matrix = np.matrix([
                    [1, 0, 0],
                    [0, -1, 0],  
                    [0, 0, 1]])

projected_points = [[0, 0] for _ in range(len(points))]

def connect_points(i, j, points):
    p1 = (int(points[i][0]), int(points[i][1]))
    p2 = (int(points[j][0]), int(points[j][1]))
    pg.draw.line(WIN, 'white', p1, p2)
    
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

    ANGLE += 0.02
    WIN.fill('black')
    i = 0
    for i, point in enumerate(points):
        rotated3d = np.dot(rotation_z, point.reshape(3, 1))
        rotated3d = np.dot(rotation_y, rotated3d)
        rotated3d = np.dot(rotation_x, rotated3d)

        projected2d = np.dot(projection_matrix, rotated3d)

        x = int(projected2d[0, 0] * ESCALA) + CIRCLE_POS[0]
        y = int(projected2d[1, 0] * ESCALA) + CIRCLE_POS[1]

        projected_points[i] = [x, y]
        pg.draw.circle(WIN, 'red', (x,y), 5)
        

    connect_points(1, 2, projected_points)    
    connect_points(2, 3, projected_points)
    connect_points(3, 1, projected_points)
    connect_points(0, 1, projected_points)
    connect_points(0, 2, projected_points)
    connect_points(0, 3, projected_points)

    pg.draw.circle(WIN, 'green',(0,0), 2.5)

    pg.display.update()

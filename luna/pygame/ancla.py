import pygame as pg
import numpy as np
from math import *

############### VENTANA
WIDTH, HEIGH = 1080, 720
pg.display.set_caption("F3N0M3N05 3N3RG1C05 D3L UN1V3R50")
WIN = pg.display.set_mode((WIDTH, HEIGH))
ESCALA = 50
CIRCLE_POS = (WIDTH /2,  HEIGH / 2)
ANGLE = 0
########################## PUNTOS
points = []
points.append(np.matrix([0, 0, 0]))
points.append(np.matrix([-3.0, 0, 0]))
points.append(np.matrix([1.8, 1.7, 1.7]))
points.append(np.matrix([-1.8, -1.8, -1.8]))
projection_matrix = np.matrix([
                    [1, 0, 0],
                    [0, 1, 0],     ])

projected_points = [[n, n] for n in range(len(points))]

def connect_points(i, j, points):
    pg.draw.line(SCREEN, 'white', (points[i][0], points[i][1]), 
                                    (points[j][0], points[j][1]))
########################## PROGRAMA
clock = pg.time.Clock()
while True:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()

    rotation_z = np.matrix([
                [cos(ANGLE), -sin(ANGLE), 0],
                [sin(ANGLE), cos(ANGLE), 0],
                [0, 0, 1] ])

    rotation_y = np.matrix([
                [1, 0, 0],
                [0, cos(ANGLE), -sin(ANGLE)],
                [-sin(ANGLE), 0, cos(ANGLE)]        ])

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
        pg.draw.circle(WIN, 'deep pink', (x, y), 5)
        i += 1

    pg.display.update()

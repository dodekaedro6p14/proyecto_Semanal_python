import sys
import pygame as pg
import numpy as np
from math import *
######################### VENTANA
WIDTH, HEIGH = 1080, 720
ESCALA = 50
CIRCLE_POS = (WIDTH /2, HEIGH /2)
ANGLE = 0
pg.init()
pg.display.set_caption("PR0Y3CT0 P03S14 3D")
SCREEN = pg.display.set_mode((WIDTH, HEIGH))

####################### PUNTOS
ps = [
    np.matrix([-3,4,0]),
    np.matrix([-3,-4,0]),
    np.matrix([3,-4,0]),
    np.matrix([3,4,0]),

    np.matrix([-3, 0, -2]),
    np.matrix([-3, 0, 2]),
    np.matrix([3, 0, 2]),
    np.matrix([3, 0, -2]),
    np.matrix([0, 3, 1]),
    np.matrix([0, -3, 1]),
    np.matrix([0, -3, -1]),
    np.matrix([0, 3, -1])
]
projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]])

projected_points = [[0, 0] for _ in range(len(ps))]

def connect_points(i, j, ps):
    p1 = (int(ps[i][0]), int(ps[i][1]))
    p2 = (int(ps[j][0]), int(ps[j][1]))
    pg.draw.line(SCREEN, (255, 255, 255), p1, p2)


###################### PROGRAMA
clock = pg.time.Clock()
while True:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()

    rotation_x = np.matrix([
        [cos(ANGLE), 0, -sin(ANGLE)],
        [0, 1, 0],
        [-sin(ANGLE), 0, cos(ANGLE)]])
    
    rotation_z = np.matrix([
        [cos(ANGLE), -sin(ANGLE), 0],
        [sin(ANGLE), cos(ANGLE), 0],
        [0, 0, 1] ])

    rotation_y = np.matrix([
        [1, 0, 0],
        [0, cos(ANGLE), -sin(ANGLE)],
        [-sin(ANGLE), 0, cos(ANGLE)]])

    ANGLE += 0.01
    SCREEN.fill('black')
    i = 0
    for point in ps:
        rotated2d = np.dot(rotation_z, point.reshape(3, 1))
        rotated2d = np.dot(rotation_y, rotated2d)
        rotated2d = np.dot(rotation_x, rotated2d)

        projected2d = np.dot(projection_matrix, rotated2d)
        x = int(projected2d[0, 0] * ESCALA) + CIRCLE_POS[0]
        y = int(projected2d[1, 0] * ESCALA) + CIRCLE_POS[1]

        projected_points[i] = [x, y]
        pg.draw.circle(SCREEN, 'red', (x, y), 5)
        i += 1

    connect_points(9, 10, projected_points)
    connect_points(10, 11, projected_points)
    connect_points(8, 9, projected_points)
    connect_points(11, 8, projected_points)

    for p in range(4):
        connect_points(p, (p + 1) % 4, projected_points)
        connect_points(p + 4, ((p + 1) % 4) + 4, projected_points)
#        connect_points(p + 8, ((p + 1) % 8) + 8, projected_points)
    pg.display.update()


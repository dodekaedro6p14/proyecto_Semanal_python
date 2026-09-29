import sys
import pygame as pg
import numpy as np
from math import *
########### VENTANA
WIDTH, HEIGH = 800, 600
ESCALA = 80
CIRCLE_POS = (WIDTH /2,  HEIGH / 2)
ANGLE = 0
pg.init()
pg.display.set_caption("PR0Y3CT3D P03S14 3D")
SCREEN = pg.display.set_mode((WIDTH, HEIGH))


########################## PUNTOS
points = [
    np.matrix([0, 0, 0]),
    np.matrix([3, 0, 0]),
    np.matrix([0, 3, 0]),
    np.matrix([0, 0, 3])
]
projection_matrix = np.array([
                    [1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]     ])

projected_points = [[0, 0] for _ in range(len(points))]

def connect_points(i, j, points_list):
    p1 = (int(points_list[i][0]), int(points_list[i][1]))
    p2 = (int(points_list[j][0]), int(points_list[j][1]))
    pg.draw.line(SCREEN, (255, 255, 255), p1, p2)
########################## PROGRAMA
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

    rotation_z = np.array([
               [cos(ANGLE), -sin(ANGLE), 0],
               [sin(ANGLE), cos(ANGLE), 0],
               [0, 0, 1]])

    rotation_y = np.array([
               [cos(ANGLE), 0, sin(ANGLE)],
               [0, 1, 0],
               [-sin(ANGLE), 0, cos(ANGLE)]])

    rotation_x = np.array([
               [1, 0, 0],
               [0, cos(ANGLE), -sin(ANGLE)],
               [-sin(ANGLE), 0, cos(ANGLE)]])

    ANGLE += 0.02
    SCREEN.fill('black')
    i = 0
    for i, point in enumerate(points):
        rotated3d = np.dot(rotation_z, point.reshape(3, 1))
        rotated3d = np.dot(rotation_y, rotated3d)
        rotated3d = np.dot(rotation_x, rotated3d)

        projected2d = np.dot(projection_matrix, rotated3d)

        x = int(projected2d[0, 0] * ESCALA) + CIRCLE_POS[0]
        y = int(-projected2d[1, 0] * ESCALA) + CIRCLE_POS[1]

        projected_points[i] = [x, y]
        pg.draw.circle(SCREEN, 'red', (x,y), 5)
    
    
    connect_points(1, 0, projected_points)    
    connect_points(2, 0, projected_points)
    connect_points(3, 0, projected_points)

    pg.display.update()

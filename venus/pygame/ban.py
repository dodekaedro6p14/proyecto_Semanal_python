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
pg.display.set_caption("PR0Y3CT0 M3T4TR0N")
SCREEN = pg.display.set_mode((WIDTH, HEIGH))
####################### PUNTOS
points = [
######## PLANO Z
    np.matrix([-10,7,0]), #0
    np.matrix([-10,-7,0]), #1
    np.matrix([10,-7,0]), #2
    np.matrix([10,7,0]),  #3

####### PLANO X
    np.matrix([-3, -3, -2.5]), #4
    np.matrix([-3, -3, 2.5]),   #5 
    np.matrix([0, -3, 2.8]),     #6
    np.matrix([1.8, -3, 0]),     #7
    np.matrix([0, -3, -2.8]),   #8

    np.matrix([0, -4, 2]),
    np.matrix([0, -4, -2]),
    np.matrix([0, 4, -2]),

######## PUNTOS DE LA FLOR
    np.matrix([0, 3, 0]),  ###ad
    np.matrix([2.3, -1.5,-1.5]), 
    np.matrix([-2.3, -1.5, -1.2]), 
    np.matrix([0, -1.2, 2.6]), 
    np.matrix([0, -3, 0]), #####ac
    np.matrix([2.3, 1.2, 1.5]), 
    np.matrix([-2.3, 1.2, 1.5]), 
    np.matrix([0, 1.2, -2.6]),

#points.append(np.matrix([3, 0, 3]))
#points.append(np.matrix([3, 0, -3]))
#points.append(np.matrix([-3, 0, -3]))
#points.append(np.matrix([-3, 0, 3]))

    np.matrix([0, 6, 0])   ### centro de la flor
]
projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]])

projected_points = [
        [0, 0] for _ in range(len(points))]

def connect_points(i, j, points):
    p1 = (int(points[i][0]), int(points[i][1]))
    p2 = (int(points[j][0]), int(points[j][1]))
    pg.draw.line(SCREEN, (255, 255, 255), p1, p2)

###################### PROGRAMA
clock = pg.time.Clock()
while True:
    clock.tick(20)
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
        [-sin(ANGLE), 0, cos(ANGLE)]
        ])
    
    rotation_z = np.matrix([
        [cos(ANGLE), -sin(ANGLE), 0],
        [sin(ANGLE), cos(ANGLE), 0],
        [0, 0, 1]
        ])

    rotation_y = np.matrix([
        [1, 0, 0],
        [0, cos(ANGLE), -sin(ANGLE)],
        [-sin(ANGLE), 0, cos(ANGLE)]
        ])

    ANGLE += 0.01
    SCREEN.fill((0, 0, 0))
    i = 0
    for point in points:
        rotated2d = np.dot(rotation_z, point.reshape(3, 1))
        rotated2d = np.dot(rotation_y, rotated2d)
        rotated2d = np.dot(rotation_x, rotated2d)

        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0, 0] * ESCALA) + CIRCLE_POS[0]
        y = int(projected2d[1, 0] * ESCALA) + CIRCLE_POS[1]

        projected_points[i] = [x, y]
        pg.draw.circle(SCREEN, (255, 0, 0), (x, y), 5)
        i += 1

    connect_points(4, 5, projected_points)
    connect_points(5, 6, projected_points)
    connect_points(6, 7, projected_points)
    connect_points(7, 8, projected_points)
    connect_points(8, 4, projected_points)
############## TETRAEDRO   Flor	   
    connect_points(12, 13, projected_points)
    connect_points(12, 14, projected_points)
    connect_points(12, 15,projected_points)
    connect_points(13, 14,projected_points)
    connect_points(14, 15,projected_points)
    connect_points(15, 13,projected_points)
    connect_points(16, 17,projected_points)
    connect_points(16, 18,projected_points)
    connect_points(16, 19,projected_points)
    connect_points(17, 18,projected_points)
    connect_points(18, 19,projected_points)
    connect_points(19, 17,projected_points)

#    for p in range(4):
#        connect_points(p, (p + 1) % 4, projected_points)
#        connect_points(p + 4, ((p + 1) % 4) + 4, projected_points)
#        connect_points(p + 8, ((p + 1) % 8) + 8, projected_points)
    pg.display.update()


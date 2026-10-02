import sys
import pygame as pg
import numpy as np
from math import *

ALTO, ANCHO = 1080, 720
ESCALA = 50
CIRCLE_POS = (ALTO/2, ANCHO/2)
ANGLE = 0

pg.init()
pg.display.set_caption("  PORYECTO ISOCAEDRO")
SCREEN = pg.display.set_mode((ALTO, ANCHO))

# UBICACIONES DE LAS ESFERAS
punto = [
    np.matrix([0,0,0]),
    np.matrix([0, 0, -3]),
    np.matrix([2.3,1.5,1.2]),
    np.matrix([-2.3,1.5,1.2]),
    np.matrix([0,-2.6,1.2])
]

geo = [
    np.matrix([1, 1, 2 ])
]

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]])

projected_points = [
        [0, 0] for _ in range(len(punto))        ]

def connect_points(i, j, punto):
    p1 = (int(punto[i][0]), int(punto[i][1]))
    p2 = (int(punto[j][0]), int(punto[j][1]))
    pg.draw.line(SCREEN, (255, 255, 255), p1, p2)

clock = pg.time.Clock()
while True:
    clock.tick(120)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()

    rotacion_x = np.matrix([
        [cos(ANGLE), 0, -sin(ANGLE)],
        [0, 1, 0],
        [-sin(ANGLE), 0, cos(ANGLE)]])

    ANGLE += 0.01
    SCREEN.fill('black')
    i = 0
    for point in punto:
        rotated2d = np.dot(rotacion_x, point.reshape(3, 1))
        projected2d = np.dot(projection_matrix, rotated2d)
        x = int(projected2d[0, 0] * ESCALA) + CIRCLE_POS[0]
        y = int(projected2d[1, 0] * ESCALA) + CIRCLE_POS[1]
        projected_points[i] = [x, y]
        i += 1
#        pygame.draw.circle(SCREEN, CYAN, (360, 450), 30)
        pg.draw.circle(SCREEN, ('red'),(x, y), 10)
#        pygame.draw.circle(SCREEN, RED, (CIRCLE_POS), 50)
        pg.draw.circle(SCREEN, ('yellow'),(540, 360), 30)
  
    connect_points(1, 2, projected_points)
    connect_points(2, 3, projected_points)
    connect_points(3, 4, projected_points)
    connect_points(4, 1, projected_points)
    connect_points(3, 2, projected_points)
    connect_points(4, 2, projected_points)
    connect_points(1, 3, projected_points)

    pg.display.update()


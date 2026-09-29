import sys
import pygame as pg
import numpy as np
from math import *

# DISEÑANDO LA VENTANA
WIDTH, HEIGH = 1080, 720
pg.init()
pg.display.set_caption("A D N")
SCREEN = pg.display.set_mode((WIDTH, HEIGH))

ESCALA = 50
CIRCLE_POS = (WIDTH/2, HEIGH/2)
ANGLE = 0 


# PUNTOS, de abajo hacia arriba
punto = [
    np.array([-1,-2, -1]), #1
    np.array([1, -2, 1]), #1B
    np.array([-1,-1, -1]), #2
    np.array([1, -1, 1]), #2b
    np.array([0, 0, 0]), #3
    np.array([-1,1, 1]), #4B
    np.array([ 1, 1, -1]),
    np.array([-1,2, 1]),   #5
    np.array([1,2,-1])
]
projection_matrix = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]

    ])

projected_points = [
        [0, 0] for _ in range(len(punto))]

def connect_points(i, j, punto):
    pg.draw.line(SCREEN, (0,0,0), (punto[i][0], punto[i][1]), (punto[j][0], punto[j][1]))

clock = pg.time.Clock()

while True:
    clock.tick(120)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()

    rotation_y = np.array([
        [cos(ANGLE), 0, -sin(ANGLE)],
        [0, 1, 0],
        [-sin(ANGLE), 0, cos(ANGLE)]
        ])

    ANGLE += 0.02

    SCREEN.fill((255, 255, 255))
    
    
    for i, p in enumerate(punto):
        rotated3d = rotation_y @ p
        projected2d = projection_matrix @ rotated3d

        x = int(projected2d[0] * ESCALA) + CIRCLE_POS[0]
        y = int(projected2d[1] * ESCALA) + CIRCLE_POS[1]

        projected_points[i] = [x, y]
        pg.draw.circle(SCREEN, (255,0,0), (x, y), 10)
        i += 1 

    pg.display.update()

    


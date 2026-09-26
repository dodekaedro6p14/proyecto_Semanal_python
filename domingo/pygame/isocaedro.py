import pygame as pg
import numpy as np
from math import *

ALTO, ANCHO = 1080, 720
pg.display.set_caption("  PORYECTO ISOCAEDRO")
SCREEN = pg.display.set_mode((ALTO, ANCHO))
ESCALA = 50
CIRCLE_POS = (ALTO/2, ANCHO/2)
ANGLE = 0

# UBICACIONES DE LAS ESFERAS
punto = []
punto.append(np.matrix([0,0,0]))
punto.append(np.matrix([0, 0, -3]))
punto.append(np.matrix([2.3,1.5,1.2]))
punto.append(np.matrix([-2.3,1.5,1.2]))
punto.append(np.matrix([0,-2.6,1.2]))

geo = []
geo.append(np.matrix([1, 1, 2 ]))

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]])

projected_points = [
        [n, n] for n in range(len(punto))]

def connect_points(i, j, punto):
    pg.draw.line(SCREEN, ('white'), (punto[i][0], punto[i][1]), 
                                    (punto[j][0], punto[j][1]))

clock = pg.time.Clock()
while True:
    clock.tick(120)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()

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
        x = int(projected2d[0][0] * ESCALA) + CIRCLE_POS[0]
        y = int(projected2d[1][0] * ESCALA) + CIRCLE_POS[1]
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


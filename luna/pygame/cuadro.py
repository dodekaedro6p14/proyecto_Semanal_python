import sys
import pygame as pg
import numpy as np 
from math import *

# colores
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)

# DISEÑO DE LA VENTANA
WIDTH, HEIGH = 1080, 720
ESCALA = 100
CIRCLE_POS = (WIDTH/2, HEIGH/2)
ANGLE = 0
pg.init()
pg.display.set_caption("Proyecto literario")
SCREEN = pg.display.set_mode((WIDTH, HEIGH))
# PUNTOS
points = [
    np.matrix([-1,-1, 1]),#1
    np.matrix([ 1,-1, 1]),#2
    np.matrix([ 1, 1, 1]),#3
    np.matrix([-1, 1, 1]),#4
    np.matrix([-1,-1,-1]),#5
    np.matrix([ 1,-1,-1]),#6
    np.matrix([ 1, 1,-1]),#7
    np.matrix([-1, 1,-1]) #8
]
projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]])

projected_points = [[0, 0] for _ in range(len(points))]

def connect_points(i, j, points):
    p1 = (int(points[i][0]), int(points[i][1]))
    p2 = (int(points[j][0]), int(points[j][1]))
    pg.draw.line(SCREEN, WHITE, p1, p2)

clock = pg.time.Clock()
while True:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()

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
        [0, sin(ANGLE), cos(ANGLE)]])

    ANGLE += 0.02
    SCREEN.fill(WHITE)
    i = 0
    for i, point in enumerate(points):
        rotated3d = np.dot(rotation_z, point.reshape((3, 1)))
        rotated3d = np.dot(rotation_y, rotated3d)

        projected2d = np.dot(projection_matrix, rotated3d)

        x = int(projected2d[0, 0] * ESCALA) + CIRCLE_POS[0]
        y = int(projected2d[1, 0] * ESCALA) + CIRCLE_POS[1]

        projected_points[i] = [x, y]
        pg.draw.circle(SCREEN, RED, (x, y), 5)
        

    for p in range(4):
        connect_points(p, (p + 1) % 4, projected_points)
        connect_points(p + 4, ((p + 1) % 4) + 4, projected_points)
        connect_points(p, (p + 4), projected_points)

    pg.display.update()


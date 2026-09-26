import pygame
import numpy as np 
from math import *

# colores
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)

# DISEÑO DE LA VENTANA
WIDTH, HEIGH = 1080, 720
pygame.display.set_caption("Proyecto literario")
SCREEN = pygame.display.set_mode((WIDTH, HEIGH))
ESCALA = 100
CIRCLE_POS = (WIDTH/2, HEIGH/2)
ANGLE = 0

# PUNTOS
points = []
points.append(np.matrix([-1,-1, 1]))#1
points.append(np.matrix([ 1,-1, 1]))#2
points.append(np.matrix([ 1, 1, 1]))#3
points.append(np.matrix([-1, 1, 1]))#4
points.append(np.matrix([-1,-1,-1]))#5
points.append(np.matrix([ 1,-1,-1]))#6
points.append(np.matrix([ 1, 1,-1]))#7
points.append(np.matrix([-1, 1,-1]))#8

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]])

projected_points = [
        [n, n] for n in range(len(points))]

def connect_points(i, j, points):
    pygame.draw.line(SCREEN, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
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

    ANGLE += 0.01
    SCREEN.fill(WHITE)
    i = 0
    for point in points:
        rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
        rotated2d = np.dot(rotation_y, rotated2d)

        projected2d = np.dot(projection_matrix, rotated2d)
        x = int(projected2d[0][0] * ESCALA) + CIRCLE_POS[0]
        y = int(projected2d[1][0] * ESCALA) + CIRCLE_POS[1]
        projected_points[i] = [x, y]
        pygame.draw.circle(SCREEN, RED, (x, y), 5)
        i += 1

    for p in range(4):
        connect_points(p, (p + 1) % 4, projected_points)
        connect_points(p + 4, ((p + 1) % 4) + 4, projected_points)
        connect_points(p, (p + 4), projected_points)

    pygame.display.update()


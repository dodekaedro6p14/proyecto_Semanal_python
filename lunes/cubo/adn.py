import pygame
import numpy as np
from math import *

# colores

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)

# DISEÑANDO LA VENTANA

WIDTH, HEIGH = 1080, 720
pygame. display.set_caption("A D N")
SCREEN = pygame.display.set_mode((WIDTH, HEIGH))

ESCALA = 50
CIRCLE_POS = (WIDTH/2, HEIGH/2)
ANGLE = 0 


# PUNTOS, de abajo hacia arriba
punto = []
punto.append(np.matrix([-1,-2, -1])) #1
punto.append(np.matrix([1, -2, 1])) #1B

punto.append(np.matrix([-1,-1, -1])) #2
punto.append(np.matrix([1, -1, 1])) #2b

punto.append(np.matrix([0,0, 0])) #3

punto.append(np.matrix([-1,1, 1])) #4B
punto.append(np.matrix([ 1, 1, -1]))

punto.append(np.matrix([-1,2, 1]))#5
punto.append(np.matrix([1,2,-1]))

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]

    ])

projected_points = [
        [n ,n] for n in range(len(punto))
        ]

def connect_points(i, j, punto):
    pygame.draw.line(SCREEN, BLACK, (punto[i][0], punto[i][1]), (punto[j][0], punto[j][1]))

clock = pygame.time.Clock()

while True:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    rotation_x = np.matrix([
        [cos(ANGLE), 0, -sin(ANGLE)],
        [0, 1, 0],
        [-sin(ANGLE), 0, cos(ANGLE)]
        ])

    ANGLE += 0.01

    SCREEN.fill(WHITE)
    i = 0
    
    for point in punto:

        rotated2d = np.dot(rotation_x, point.reshape(3,1))

        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * ESCALA) + CIRCLE_POS[0]
        y = int(projected2d[1][0] * ESCALA) + CIRCLE_POS[1]

        projected_points[i] = [x, y]
        pygame.draw.circle(SCREEN, RED, (x, y), 10)
        i += 1 

    pygame.display.update()

    


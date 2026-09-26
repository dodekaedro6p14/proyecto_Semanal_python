import pygame
import numpy as np
from math import *

# colores 

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)

WIDTH, HEIGHT = 1080, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PROYECTO GRAVITACIONAL")
scale = 100
circle_pos =[WIDTH/2, HEIGHT/2]
angle = 0

## puntos en le plano
points = []
points.append(np.matrix([1, 1, 1]))
points.append(np.matrix([1, 1, 0]))
points.append(np.matrix([1, 1, -1]))

points.append(np.matrix([-1,-1,-1]))
points.append(np.matrix([-1,-1,0]))
points.append(np.matrix([-1,-1,1]))

points.append(np.matrix([-1, 0, 0]))
points.append(np.matrix([0,0,0]))
points.append(np.matrix([1, 0,0]))

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
    ])

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

    rotation_x = np.matrix([
        [cos(angle), 0, -sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)]
        ])

#    rotation_y = np.matrix([        rotacion en circulos de arriba hacia abajo 
#        [cos(angle), -sin(angle), 0],
#        [sin(angle), cos(angle), 0],
#        [0, 0, 1]
#        ])

    angle += 0.01

    SCREEN.fill(WHITE)

    for point in points:
        rotated2d = np.dot(rotation_x, point.reshape((3, 1)))
        projected2d = np.dot(projection_matrix, rotated2d)


        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]
        pygame.draw.circle(SCREEN, RED, (x, y), 5)
        

    pygame.display.update()



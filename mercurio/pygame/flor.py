import pygame
import numpy as np
from math import *

##########################c COLORES
WHITE  = (255, 255, 255)
BLACK  = (  0,   0,   0)
RED    = (255,   0,   0)

######################### VENTANA

WIDTH, HEIGH = 1080, 720
pygame.display.set_caption("PR0Y3CT0 M3RK4B4")
SCREEN = pygame.display.set_mode((WIDTH, HEIGH))

ESCALA = 50
CIRCLE_POS = (WIDTH /2, HEIGH /2)
ANGLE = 0

####################### PUNTOS
points = []
######## PLANO Z
points.append(np.matrix([-10,7,0]))
points.append(np.matrix([-10,-7,0]))
points.append(np.matrix([10,-7,0]))
points.append(np.matrix([10,7,0]))

####### PLANO X
points.append(np.matrix([-5, 0, -6]))
points.append(np.matrix([-5, 0, 6]))
points.append(np.matrix([5, 0, 6]))
points.append(np.matrix([5, 0, -6]))

points.append(np.matrix([0, 4, 2]))
points.append(np.matrix([0, -4, 2]))
points.append(np.matrix([0, -4, -2]))
points.append(np.matrix([0, 4, -2]))

######## PUNTOS DE LA FLOR
points.append(np.matrix([0, 3, 0]))  ###ad
points.append(np.matrix([2.3, -1.2,-1.5])) 
points.append(np.matrix([-2.3, -1.5, -1.2])) 
points.append(np.matrix([0, -1.2, 2.61])) 

points.append(np.matrix([0, -3, 0])) #####ac
points.append(np.matrix([2.3, 1.2, 1.5])) 
points.append(np.matrix([-2.3,1.2, 1.5])) 
points.append(np.matrix([0, 1.2, -2.6])) 

#points.append(np.matrix([3, 0, 3]))
#points.append(np.matrix([3, 0, -3]))
#points.append(np.matrix([-3, 0, -3]))
#points.append(np.matrix([-3, 0, 3]))

points.append(np.matrix([0, 6, 0]))   ### centro de la flor

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]

    ])

projected_points = [
        [n, n] for n in range(len(points))]

def connect_points(i, j, points):
    pygame.draw.line(SCREEN, WHITE, (points[i][0], 
                              points[i][1]), (points[j][0], points[j][1]))

###################### PROGRAMA
clock = pygame.time.Clock()
while True:

    clock.tick(20)
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
    SCREEN.fill(BLACK)
    i = 0
    for point in points:
        rotated2d = np.dot(rotation_z, point.reshape(3, 1))
        rotated2d = np.dot(rotation_y, rotated2d)

        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * ESCALA) + CIRCLE_POS[0]
        y = int(projected2d[1][0] * ESCALA) + CIRCLE_POS[1]

        projected_points[i] = [x, y]
        pygame.draw.circle(SCREEN, BLACK, (x, y), 5)
        i += 1

#    connect_points(9, 10, projected_points)
#    connect_points(10, 11, projected_points)
#    connect_points(8, 9, projected_points)
#    connect_points(11, 8, projected_points)
############## TETRAEDRO	   
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
    pygame.display.update()


import pygame
from math import *

SIZE1 = 1080  #dimenciones de la pantalla
SIZE2 = 720
ROTATE_SPEED = 0.02 # VELOCIDAD DE ROTACION 

WHITE= (255, 255, 255)
AZUL = (  0,   0, 255)
RED  = (255,   0,   0)
CYAN = (  0, 255,   0)


SCREEN = pygame.display.set_mode((SIZE1, SIZE2))
clock = pygame.time.Clock()
pygame.display.set_caption("PR0Y3CT3D P03S14 3D")

projection_matrix = [[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]]

cube_points = [n for n in range (9)]
###############Lado A
cube_points[0] = [[1], [0], [3]]
######## PUNTOS DE LA FLOR
cube_points[1] = [[0], [3], [0]]  
cube_points[2] = [[2.3], [-1.5],[-1.5]]###########3 
cube_points[3] = [[-2.3], [-1.5], [-1.5]] 
cube_points[4] = [[0], [-1.5], [2.6]] 

cube_points[5] = [[0], [-3], [0]]
cube_points[6] = [[2.3], [1.2], [1.5]] 
cube_points[7] = [[-2.3], [1.2], [1.5]] 
cube_points[8] = [[0], [1.2], [-2.6]] 


def multiply_m(a, b):
    a_rows = len(a)
    a_cols = len(a[0])

    b_rows = len(b)
    b_cols = len(b[0])
    # Dot product matrix dimentions = a_rows x b_cols
    product = [[0 for _ in range(b_cols)] for _ in range(a_rows)]

    if a_cols == b_rows:
        for i in range(a_rows):
            for j in range(b_cols):
                for k in range(b_rows):
                    product[i][j] += a[i][k] * b[k][j]

    else:
        print("INCOMPATIBLE MATRIX SIZES")

    return product

def connect_points(i, j, points):
    pygame.draw.line(SCREEN, WHITE, (points[i][0], points[i][1]), (points[j][0], points[j][1]))

# main loop
scale = 100
angle_x = angle_y = angle_z = 0
while True:
    clock.tick(60)
    SCREEN.fill((0, 0, 0))
    rotation_x = [[1, 0, 0], 
                  [0, cos(angle_x), -sin(angle_x)],
                  [0, sin(angle_x), cos(angle_x)]]

    rotation_y = [[cos(angle_y), 0, sin(angle_y)],
                  [0, 1, 0],
                  [-sin(angle_y), 0, cos(angle_y)]]

    rotation_z = [[cos(angle_z), -sin(angle_z), 0],
                  [sin(angle_z), cos(angle_z), 0],
                  [0, 0, 1]]
    
    points = [0 for _ in range(len(cube_points))]
    i = 0
    for point in cube_points:
        rotate_x = multiply_m(rotation_x, point)
        rotate_y = multiply_m(rotation_y, rotate_x)
        rotate_z = multiply_m(rotation_z, rotate_y)
        point_2d = multiply_m(projection_matrix, rotate_z)

        x = (point_2d[0][0] * scale) + SIZE1/2
        y = (point_2d[1][0] * scale) + SIZE2/2

        points[i] = (x,y)
        i += 1
        pygame.draw.circle(SCREEN, CYAN, (x, y), 1)
    	

    connect_points(1, 2, points)
    connect_points(2, 3, points)
    connect_points(3, 1, points)
    connect_points(1, 4, points)
    connect_points(4, 2, points)
    connect_points(4, 3, points)
    connect_points(5, 6, points)
    connect_points(6, 7, points)
    connect_points(7, 5, points)
    connect_points(5, 8, points)
    connect_points(6, 8, points)
    connect_points(8, 7, points)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()


        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            angle_y = angle_x = angle_z = 0
        if keys[pygame.K_a]:
            angle_y += ROTATE_SPEED
        if keys[pygame.K_d]:
            angle_y -= ROTATE_SPEED
        if keys[pygame.K_w]:
            angle_x += ROTATE_SPEED
        if keys[pygame.K_s]:
            angle_x -= ROTATE_SPEED
        if keys[pygame.K_q]:
            angle_z -= ROTATE_SPEED
        if keys[pygame.K_e]:
            angle_z += ROTATE_SPEED

#    pygame.draw.aaline(SCREEN, AZUL, (0, 360), (1080, 360), 1)
    pygame.draw.aaline(SCREEN, RED, (540, 0), (540, 720), 1)    

    pygame.display.update()



import pygame as pg
from math import *

SIZE1 = 1080  #dimenciones de la pantalla
SIZE2 = 720
ROTATE_SPEED = 0.02 # VELOCIDAD DE ROTACION 

CYAN = (  0, 255,   0)

SCREEN = pg.display.set_mode((SIZE1, SIZE2))
clock = pg.time.Clock()
pg.display.set_caption("PR0Y3CT3D P03S14 3D")

projection_matrix = [[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]]

cube_points = [n for n in range (24)]
###############cubo A
cube_points[0] = [[-2], [-2], [1]]
cube_points[1] = [[0], [-2], [1]]
cube_points[2] = [[0], [0], [1]]
cube_points[3] = [[-2], [0], [1]]
cube_points[4] = [[-2], [-2], [-1]]
cube_points[5] = [[0], [-2], [-1]]
cube_points[6] = [[0], [0], [-1]]
cube_points[7] = [[-2], [0], [-1]]
#################cubo B
cube_points[8] = [[0], [-1], [0]]
cube_points[9] = [[2], [-1], [0]]
cube_points[10]= [[2], [-1], [-2]]
cube_points[11]= [[0], [-1], [-2]]
cube_points[12]= [[0], [1], [0]]
cube_points[13]= [[2], [1], [0]]
cube_points[14]= [[2], [1], [-2]]
cube_points[15]= [[0], [1], [-2]]
####################cubo C
cube_points[16]= [[-1], [0], [0]]
cube_points[17]= [[1], [0], [0]]
cube_points[18]= [[1], [0], [2]]
cube_points[19]= [[-1], [0], [2]]
cube_points[20]= [[-1], [2], [0]]
cube_points[21]= [[1], [2], [0]]
cube_points[22]= [[-1], [2], [2]]
cube_points[23]= [[1], [2], [2]]

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

    return product

def connect_points(i, j, points):
    pg.draw.line(SCREEN, "white", (points[i][0], points[i][1]), (points[j][0], points[j][1]))

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
        pg.draw.circle(SCREEN, CYAN, (x, y), 1)
    	
    connect_points(0, 1, points)
    connect_points(0, 3, points)
    connect_points(0, 4, points)
    connect_points(1, 2, points)
    connect_points(1, 5, points)
    connect_points(2, 6, points)
    connect_points(2, 3, points)
    connect_points(3, 7, points)
    connect_points(4, 5, points)
    connect_points(4, 7, points)
    connect_points(6, 5, points)
    connect_points(6, 7, points)
    
    connect_points(8, 9, points)
    connect_points(9,10, points)
    connect_points(10,11,points)
    connect_points(11,8, points)
    connect_points(8,12, points)
    connect_points(14,10,points)
    connect_points(9,13, points)
    connect_points(11,15,points)
    connect_points(12,13,points)
    connect_points(13,14,points)
    connect_points(14,15,points)
    connect_points(15,12,points)

    connect_points(16,17,points)
    connect_points(17,18,points)
    connect_points(18,19,points)
    connect_points(19,16,points)
    connect_points(16,20,points)
    connect_points(20,21,points)
    connect_points(21,23,points)
    connect_points(23,22,points)
    connect_points(20,22,points)
    connect_points(17,21,points)
    connect_points(18,23,points)
    connect_points(19,22,points)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()

        keys = pg.key.get_pressed()
        if keys[pg.K_r]:
            angle_y = angle_x = angle_z = 0
        if keys[pg.K_a]:
            angle_y += ROTATE_SPEED
        if keys[pg.K_d]:
            angle_y -= ROTATE_SPEED
        if keys[pg.K_w]:
            angle_x += ROTATE_SPEED
        if keys[pg.K_s]:
            angle_x -= ROTATE_SPEED
        if keys[pg.K_q]:
            angle_z -= ROTATE_SPEED
        if keys[pg.K_e]:
            angle_z += ROTATE_SPEED

#    pygame.draw.aaline(SCREEN, AZUL, (0, 360), (1080, 360), 1)
#    pygame.draw.aaline(SCREEN, RED, (540, 0), (540, 720), 1)    

    pg.display.update()



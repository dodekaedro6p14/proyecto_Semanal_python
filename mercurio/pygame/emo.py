import pygame as pg
from math import *

pg.init()
SIZE1, SIZE2 = 1366, 768  
ROTATE_SPEED = 0.02 # VELOCIDAD DE ROTACION 
#BG = pg.image.load('../ima/copo_r2.jpg')
pg.display.set_caption("emo.py 'copo de nieve'")
WIN = pg.display.set_mode((SIZE1, SIZE2))
clock = pg.time.Clock()
projection_matrix = [[1, 0, 0],
                     [0, -1, 0],
                     [0, 0, 0]]

pints = [n for n in range (20)]
# cubo
pints[0] = [[-2], [-2], [2]]
pints[1] = [[2], [-2], [2]]
pints[2] = [[2], [2], [2]]
pints[3] = [[-2], [2], [2]]
pints[4] = [[-2], [-2], [-2]]
pints[5] = [[2], [-2], [-2]]
pints[6] = [[2], [2], [-2]]
pints[7] = [[-2], [2], [-2]]
#copo    
pints[8]  = [[0],[1.8], [0]]
pints[9]  = [[0], [-1.8], [0]]
pints[10] = [[-1.55], [-0.86], [0]]
pints[11] = [[-1.55], [ 0.86], [0]]
pints[12] = [[ 1.55], [ 0.86], [0]]
pints[13] = [[ 1.55], [-0.86], [0]]
#
pints[14] = [[-1.05], [-0.6], [0]]
pints[15] = [[-0.68], [-0.41], [0]]
pints[16] = [-1.55], [-0.6], [0] # A
pints[17] = [-1.05], [-0.86], [0] # B
pints[18] = [-1.55], [-0.41], [0] # C
pints[19] = [-0.68], [-0.86], [0] # D
#
#pints[16] = [[ 1.05], [ 0.6], [0]]
#pints[17] = [[ 0.68], [ 0.41], [0]]
#
#pints[18] = [[-1.05], [ 0.6], [0]]
#pints[19] = [[-0.68], [ 0.41], [0]]
#
#pints[20] = [[ 1.05], [-0.6], [0]]
#pints[21] = [[ 0.68], [-0.41], [0]]
#
#pints[22] = [0], [1.2], [0]
#pints[23] = [0], [0.8], [0]
#pints[24] = [0], [-1.2], [0]
#pints[25] = [0], [-0.8], [0]


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
    pg.draw.line(WIN, ("white"), (points[i][0], points[i][1]), (points[j][0], points[j][1]))

scale = 100
angle_x = angle_y = angle_z = 0
while True:
    clock.tick(60)
#    WIN.blit(BG, [335, 154])
    WIN.fill((0, 0, 0))
    rotation_x = [[1, 0, 0], 
                  [0, cos(angle_x), -sin(angle_x)],
                  [0, sin(angle_x), cos(angle_x)]]

    rotation_y = [[cos(angle_y), 0, sin(angle_y)],
                  [0, 1, 0],
                  [-sin(angle_y), 0, cos(angle_y)]]

    rotation_z = [[cos(angle_z), -sin(angle_z), 0],
                  [sin(angle_z), cos(angle_z), 0],
                  [0, 0, 1]]
    
    points = [0 for _ in range(len(pints))]
    i = 0
    for i, point in enumerate(points):
        rotate_x = multiply_m(rotation_x, point)
        rotate_y = multiply_m(rotation_y, rotate_x)
        rotate_z = multiply_m(rotation_z, rotate_y)
        point_2d = multiply_m(projection_matrix, rotate_z)

        x = int(point_2d[0, 0] * scale) + SIZE1/2
        y = int(point_2d[1, 0] * scale) + SIZE2/2

        points[i] = (x,y)
        i += 1
        pg.draw.circle(WIN, (255, 69, 0), (x, y), 5)

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

    for event in pg.event.get():
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

#    pg.draw.aaline(WIN, 'blue',(0, 384), (1366, 384), 1)
#    pg.draw.aaline(WIN, 'red',(683, 0), (683, 768), 1)
    pg.display.update()



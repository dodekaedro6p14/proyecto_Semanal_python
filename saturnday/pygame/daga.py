import pygame as pg
from math import *

SIZE1, SIZE2 = 1080, 720  
ROTATE_SPEED = 0.02 # VELOCIDAD DE ROTACION 
window = pg.display.set_mode((SIZE1, SIZE2))
clock = pg.time.Clock()

projection_matrix = [[1, 0, 0],
                     [0, -1, 0],
                     [0, 0, 0]]

cube_points = [n for n in range (45)]
#cubo
cube_points[0] = [[-3], [-3], [3]]; cube_points[1] = [[3], [-3], [3]];  cube_points[2] = [[3], [3], [3]];    cube_points[3] = [[-3], [3], [3]]
cube_points[4] = [[-3], [-3], [-3]];cube_points[5] = [[3], [-3], [-3]]; cube_points[6] = [[3], [3], [-3]];   cube_points[7] = [[-3], [3], [-3]]
cube_points[8] = [[0], [1.5], [0]]; cube_points[9] = [[0], [-1.5], [0]];cube_points[10] = [[-1.5], [0], [0]];cube_points[11] = [[1.5], [0], [0]]
#eje -x, y, z0
cube_points[12] = [[-1.06], [1.06], [0]]
cube_points[13] = [[-1.36], [0.6], [0]]
cube_points[14] = [[-0.6], [1.36], [0]]
cube_points[15] = [[-1.06], [-1.06], [0]]
cube_points[16] = [[-1.36], [-0.6], [0]]
cube_points[17] = [[-0.6], [-1.36], [0]]
#eje x, y, 0z
cube_points[18] = [[1.06], [1.06], [0]]
cube_points[19] = [[1.36], [0.6], [0]]
cube_points[20] = [[0.6], [1.36], [0]]
cube_points[21] = [[1.06], [-1.06], [0]]
cube_points[22] = [[1.36], [-0.6], [0]]
cube_points[23] = [[0.6], [-1.36], [0]]
#eje 0x, y, +z
cube_points[24] = [[0], [1.06], [1.06]]
cube_points[25] = [[0], [1.36], [0.6]]
cube_points[26] = [[0], [0.6], [1.36]]
cube_points[27] = [[0], [-1.06], [1.06]]
cube_points[28] = [[0], [-1.36], [0.6]]
cube_points[29] = [[0], [-0.6], [1.36]]
cube_points[30] = [[0], [0], [1.5]]
#eje 0x, y, -z
cube_points[31] = [[0], [1.36], [-0.6]]
cube_points[32] = [[0], [1.06], [-1.06]]
cube_points[33] = [[0], [0.6], [-1.36]]
cube_points[34] = [[0], [0], [-1.5]]
cube_points[35] = [[0], [-0.6], [-1.36]]
cube_points[36] = [[0], [-1.06], [-1.06]]
cube_points[37] = [[0], [-1.36], [-0.6]]
#######
cube_points[38] = [[-0.53], [1.36], [0.53]]
cube_points[39] = [[-0.6], [1.06], [1.06]]
cube_points[40] = [[-0.6], [0.6], [1.36]]
cube_points[41] = [[-1.06], [0], [1.06]]
cube_points[42] = [[-0.6], [-0.6], [1.36]]
cube_points[43] = [[-0.6], [-1.06], [1.06]]
cube_points[44] = [[-0.53], [-1.36], [0.53]]





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
    pg.draw.line(window, (0, 255, 255),[points[i][0], points[i][1]], [points[j][0], points[j][1]])

scale = 100
angle_x = angle_y = angle_z = 0
while True:
    clock.tick(60)
    window.fill((0, 0, 0))
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
        pg.draw.circle(window, (255, 0, 0), (x, y), 5)

    connect_points(8, 9, points)
#    connect_points(0, 3, points)
#    connect_points(0, 4, points)
#    connect_points(1, 2, points)
#    connect_points(1, 5, points)
#    connect_points(2, 6, points)
#    connect_points(2, 3, points)
#    connect_points(3, 7, points)
#    connect_points(4, 5, points)
#    connect_points(4, 7, points)
#    connect_points(6, 5, points)
#    connect_points(6, 7, points)

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
#    pg.draw.circle(window, (0,255,255, 55),(540,360),150)
    pg.display.update()



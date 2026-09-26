import pygame as pg
from math import *

pg.init()
WIDTH, HEIGHT = 1080, 720
pg.display.set_caption("C0R4Z0N 3D")
BG = pg.transform.scale(pg.image.load("cuadricula.avif"), (WIDTH, HEIGHT))
WIN = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pg.time.Clock()

ROTATE_SPEED = 0.02 # VELOCIDAD DE ROTACION 
projection_matrix = [[-1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]]

cube_points = [n for n in range (18)]
cube_points[0] = [[-3], [-3], [3]]
cube_points[1] = [[3], [-3], [3]]
cube_points[2] = [[3], [3], [3]]
cube_points[3] = [[-3], [3], [3]]
cube_points[4] = [[-3], [-3], [-3]]
cube_points[5] = [[3], [-3], [-3]]
cube_points[6] = [[3], [3], [-3]]
cube_points[7] = [[-3], [3], [-3]]
#   EJE X
cube_points[8] = [[0], [0], [0]]

cube_points[9]  = [[-0.5], [0.5], [-0.5]]   ##eje z +*-
cube_points[10] = [[-0.5], [0],    [0]]
cube_points[11] = [[-0.5], [-0.5], [-0.5]]
cube_points[12] = [[0],    [0.5], [0]]
cube_points[13] = [[0],   [0],    [0]]
cube_points[14] = [[0],   [-0.5], [0]]
cube_points[15] = [[0.5], [0.5], [0.5]]
cube_points[16] = [[0.5], [0],    [0]]
cube_points[17] = [[0.5], [-0.5], [0.5]] ### se cambia eje Z -*+

#cube_points[18] = [[0.5], [-1.4], [0]]
#cube_points[19] = [[1], [-1.5], [0]]
#cube_points[20] = [[1.5], [-1.3], [0]]
#cube_points[21] = [[1.8], [-1], [0]]
#cube_points[22] = [[1.9], [-0.5], [0]]
#cube_points[23] = [[1.7], [0], [0]]
#cube_points[24] = [[1.2], [0.5], [0]]
# EJE Z
#cube_points[25] = [[0], [-1.2], [0.4]]
#cube_points[26] = [[0], [-1.15], [0.8]]
#cube_points[27] = [[0], [-0.8], [1.1]]
#cube_points[28] = [[0], [-0.5], [1.2]]
#cube_points[29] = [[0], [0], [1.1]]
#cube_points[30] = [[0], [0.5], [0.8]]

#cube_points[31] = [[0], [-1.2], [-0.4]]
#cube_points[32] = [[0], [-1.15], [-0.8]]
#cube_points[33] = [[0], [-0.8], [-1.1]]
#cube_points[34] = [[0], [-0.5], [-1.2]]
#cube_points[35] = [[0], [0], [-1.1]]
#cube_points[36] = [[0], [0.5], [-0.8]]

#cube_points[37] = [[0], [0.5], [-0.8]]
#cube_points[38] = [[0], [0.5], [-0.8]]
#cube_points[39] = [[0], [0.5], [-0.8]]
#cube_points[40] = [[0], [0.5], [-0.8]]
#cube_points[41] = [[0], [0.5], [-0.8]]
#cube_points[42] = [[0], [0.5], [-0.8]]
#cube_points[37] = [[-0.5], [0.5], [-0.5]]
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
    pg.draw.line(WIN, ('white'), (points[i][0], points[i][1]),
                 (points[j][0], points[j][1]))
# main loop
scale = 100
angle_x = angle_y = angle_z = 0

while True:
    clock.tick(60)
    WIN.blit(BG, [0, 0])
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

        x = (point_2d[0][0] * scale) + WIDTH/2
        y = (point_2d[1][0] * scale) + HEIGHT/2

        points[i] = (x,y)
        i += 1
        pg.draw.rect(WIN, 'red', (x, y, 25, 25), 0)

### unir puntos del eje X
    connect_points(2, 4, points)
    connect_points(3, 5, points)
#    connect_points(12, 13, points)
#    connect_points(13, 14, points)
#    connect_points(14, 15, points)
#    connect_points(15, 16, points)
#    connect_points(16, 17, points)
#    connect_points(17, 9, points)

#    connect_points(10, 18, points)
#    connect_points(18, 19, points)
#    connect_points(19, 20, points)
#    connect_points(20, 21, points)
#    connect_points(21, 22, points)
#    connect_points(22, 23, points)
#    connect_points(23, 24, points)
#    connect_points(24, 9, points)

#    connect_points(10, 25, points)
#    connect_points(25, 26, points)
#    connect_points(26, 27, points)
#    connect_points(27, 28, points)
#    connect_points(28, 29, points)
#    connect_points(29, 30, points)
#    connect_points(30, 9, points)

#    connect_points(10, 31, points)
#    connect_points(31, 32, points)
#    connect_points(32, 33, points)
#    connect_points(33, 34, points)
#    connect_points(34, 35, points)
#    connect_points(35, 36, points)
#    connect_points(36, 9, points)
#    connect_points(29, 30, points)
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

    pg.display.update()

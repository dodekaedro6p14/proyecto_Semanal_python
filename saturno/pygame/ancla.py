import pygame as pg
from math import *

SIZE1, SIZE2  = 1080, 720 
ROTATE_SPEED = 0.02 # VELOCIDAD DE ROTACION 
WIN = pg.display.set_mode((SIZE1, SIZE2))
clock = pg.time.Clock()
pg.display.set_caption("PR0Y3CT3D F4RF4L4 3D")

espacio_3d = [[1, 0, 0],
              [0, -1, 0],
              [0, 0, 1]]

pin = [n for n in range (13)]
pin[0] = [[0], [0], [0]]
pin[1] = [[1], [1], [1]]
pin[2] = [[2.5], [1], [1]]
pin[3] = [[1.5], [0], [1]]
pin[4] = [[1], [-0.5], [-1]]    #
pin[5] = [[1.5], [-1.5], [-1]]
pin[6] = [[0.5], [-1], [-1]]
pin[7] = [[-0.5], [-1], [-1]]
pin[8] = [[-1.5], [-1.5], [-1]]
pin[9] = [[-1], [-0.5], [-1]]   #
pin[10]= [[-1.5], [0], [1]]
pin[11]= [[-2.5], [1], [1]]
pin[12]= [[-1], [1], [1]]

def multiply_m(a, b):
    a_rows = len(a)
    a_cols = len(a[0])

    b_rows = len(b)
    b_cols = len(b[0])
    product = [[0 for _ in range(b_cols)] for _ in range(a_rows)]

    if a_cols == b_rows:
        for i in range(a_rows):
            for j in range(b_cols):
                for k in range(b_rows):
                    product[i][j] += a[i][k] * b[k][j]

    return product

def connect_points(i, j, points):
    pg.draw.line(WIN, "cyan", (points[i][0], points[i][1]), (points[j][0], points[j][1]))

# main loop
scale = 100
angle_x = angle_y = angle_z = 0
while True:
    clock.tick(60)
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
    
    points = [0 for _ in range(len(pin))]
    i = 0
    for point in pin:
        rotate_x = multiply_m(rotation_x, point)
        rotate_y = multiply_m(rotation_y, rotate_x)
        rotate_z = multiply_m(rotation_z, rotate_y)
        point_2d = multiply_m(espacio_3d, rotate_z)

        x = (point_2d[0][0] * scale) + SIZE1/2
        y = (point_2d[1][0] * scale) + SIZE2/2

        points[i] = (x,y)
        i += 1
        pg.draw.circle(WIN, "red", (x, y), 1)
    	
    connect_points(0, 1, points)
    connect_points(1, 2, points)
    connect_points(2, 3, points)
    connect_points(3, 0, points)
    connect_points(0, 4, points)
    connect_points(4, 5, points)
    connect_points(5, 6, points)
    connect_points(6, 0, points)
    connect_points(0, 7, points)
    connect_points(7, 8, points)
    connect_points(8, 9, points)
    connect_points(9, 0, points)
    connect_points(0,10, points)
    connect_points(10,11,points)
    connect_points(11,12,points)
    connect_points(12, 0,points)
    
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
            angle_x = angle_y = angle_z = 0
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

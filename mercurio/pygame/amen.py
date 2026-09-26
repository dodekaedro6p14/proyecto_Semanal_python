import pygame as pg
from math import *

SIZE1, SIZE2 = 1366, 768  #dimenciones de la pantalla
ROTATE_SPEED = 0.02 # VELOCIDAD DE ROTACION 
SCREEN = pg.display.set_mode((SIZE1, SIZE2))
clock = pg.time.Clock()
projection_matrix = [[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]]

cube_points = [n for n in range (48)]
###############Lado A
cube_points[0] = [[1], [0], [2]]
cube_points[1] = [[1.5], [0], [2.5]]
cube_points[2] = [[1], [0], [-1]]
cube_points[3] = [[-1], [0], [2]]
cube_points[4] = [[-1], [0], [2.5]]
cube_points[5] = [[1.5], [-2.5], [-1.5]]
cube_points[6] = [[1.5], [0], [-1]]
cube_points[7] = [[1.5], [-2.5], [-1]]
cube_points[8] = [[1.5], [0.5], [-1.5]]
cube_points[9] = [[1.5], [0.5], [2.5]]
cube_points[10]= [[-1.5], [0.5], [2.5]]
cube_points[11]= [[1], [-2], [-1]]
cube_points[12]= [[-1], [-1.5], [2.5]]
cube_points[13]= [[-1.5], [-1.5], [2.5]]
cube_points[14]= [[-1.5], [-1.5], [-0.5]]
cube_points[15]= [[-1], [-1.5], [0]]
########## LADO B
cube_points[16]= [[2.5], [-1.5], [-0.5]]
cube_points[17]= [[2.5], [-1.5], [0]]
cube_points[18]= [[2.5], [1], [0]]
cube_points[19]= [[2.5], [1.5], [-0.5]]
cube_points[20]= [[2.5], [1.5], [1.5]]
cube_points[21]= [[2.5], [1], [1.5]]
cube_points[22]= [[0], [1], [1.5]]
cube_points[23]= [[-0.5], [1.5], [1.5]]
############## LADO C
cube_points[24]= [[-0.5], [-2.5], [1.5]]
cube_points[25]= [[-1], [-1], [2]]
cube_points[26]= [[0], [-2.5], [1.5]]
cube_points[27]= [[-1], [-1], [0]] 
cube_points[28]= [[-0.5], [-2.5], [-1.5]]
cube_points[29]= [[0], [-2.5], [-1]]
cube_points[30]= [[0], [-2], [-1]]
cube_points[31]= [[2], [-1], [0]]
cube_points[32]= [[2], [1], [0]]
cube_points[33]= [[2], [1], [1]]
cube_points[34]= [[0], [1], [1]]
cube_points[35]= [[0], [-2], [1]]

############# LADO d
cube_points[36]= [[-0.5], [-2], [1]]
cube_points[37]= [[-0.5], [-2], [-1.5]]
cube_points[38]= [[1], [-2], [-1.5]]
cube_points[39]= [[1], [0.5], [-1.5]]
cube_points[40]= [[1], [0.5], [2]]
cube_points[41]= [[-1.5], [0.5], [2]]
cube_points[42]= [[-1.5], [-1], [2]]
cube_points[43]= [[-1.5], [-1], [-0.5]]
cube_points[44]= [[2], [-1], [-0.5]]
cube_points[45]= [[2], [1.5], [-0.5]]
cube_points[46]= [[2], [1.5], [1]]
cube_points[47]= [[-0.5], [1.5], [1]]

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
    pg.draw.line(SCREEN, 'cyan', (points[i][0], points[i][1]), (points[j][0], points[j][1]))

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
        pg.draw.circle(SCREEN, 'red', (x, y), 1)
    	
    connect_points(1, 4, points)
    connect_points(0, 3, points)
    connect_points(1, 6, points)
    connect_points(0, 2, points)
    connect_points(6, 7, points)
    connect_points(7, 29, points)
    connect_points(9,10, points)
    connect_points(9, 8, points)
    connect_points(8, 5, points)
    connect_points(2,11, points)
    connect_points(4,12, points)
    connect_points(10,13,points)
    connect_points(13,14,points)
    connect_points(12,15,points)
    connect_points(14,16,points)
    connect_points(15,17,points)
    connect_points(17,18,points)
    connect_points(16,19,points)
    connect_points(18,21,points)
    connect_points(19,20,points)
    connect_points(21,22,points)
    connect_points(20,23,points)
    connect_points(23,24,points)
    connect_points( 3,25,points)
    connect_points(22,26,points)
    connect_points(25,27,points)
    connect_points(24,28,points)
    connect_points(26,29,points)
    connect_points(28,5 ,points)
    connect_points(30,11,points)
    connect_points(27,31,points)
    connect_points(31,32,points)
    connect_points(32,33,points)
    connect_points(33,34,points)
    connect_points(34,35,points)
    connect_points(35,30,points)

    connect_points(36,37,points)
    connect_points(37,38,points)
    connect_points(38,39,points)
    connect_points(39,40,points)
    connect_points(40,41,points)
    connect_points(41,42,points)
    connect_points(42,43,points)
    connect_points(43,44,points)
    connect_points(44,45,points)
    connect_points(45,46,points)
    connect_points(46,47,points)
    connect_points(47,36,points)

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

#    pygame.draw.aaline(SCREEN, AZUL, (0, 384), (1366, 384), 1)
#    pygame.draw.aaline(SCREEN, RED, (683, 0), (683, 768), 1)    

    pg.display.update()



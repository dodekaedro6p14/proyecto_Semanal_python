import sys
import pygame as pg
import numpy as np
from math import *

pg.init()
pg.mixer.init()
WIDTH, HEIGH = 1600, 900
WIN = pg.display.set_mode((WIDTH, HEIGH))
ESCALA = 50
CIRCLE_POS = (WIDTH /2,  HEIGH / 2)
ANGLE = 0
############### musica
fuente = pg.font.SysFont('arial', 30)
tex = fuente.render("demostracion", True, 'cyan')
pg.mixer.music.load("../../mus/viento.mp3")
########################## PUNTOS 1
px = [
#px.append(np.matrix([0, 0, 0]))
    np.matrix([0, 3, 0]),
    np.matrix([2.3, -1.5, -1.5]),
    np.matrix([-2.3, -1.5, -1.5]),
    np.matrix([0, -1.5, 2.6])
]
pro_matrixX = np.matrix([[1, 0, 0],
                         [0, 1, 0],
                         [0, 0, 1]])

pro_pointsX = [[0, 0] for _ in range(len(px))]

def con_pointsX(i, j, px):
    p1 = (int(px[i][0]), int(px[i][1]))
    p2 = (int(px[j][0]), int(px[j][1]))
    pg.draw.line(WIN, 'deep pink', p1, p2)
   

#def texto(WIN, fuente, texto, color, dimencion, x, y):
#    letra = pg.font.Font(arial, dimencion)
#    surface = letra.render(texto, True, color)
#    rect = surface.get_rect()
#    rect.center(x, y)
#    WIN.blit(surface, rect)
    
################################### PUNTOS 2
py = [
    np.matrix([0,-3,0]),
    np.matrix([-2.3,1.5,1.5]),
    np.matrix([2.3,1.5,1.5]),
    np.matrix([0,1.5,-2.6])
]

pro_pointsY = [[0, 0] for _ in range(len(py))]

def con_pointsY(u, k, py):
    pg.draw.line(WIN, 'green',(py[u][0], py[u][1]),
                                    (py[k][0], py[k][1]))
#################### blue
pz = [
    np.matrix([0,-4,0]),
    np.matrix([3.3,-2.5,-2.5]),
    np.matrix([-3.3,-2.5,-2.5]),
    np.matrix([0,-2.5, 2.6])
]
pro_pointsZ = [[0, 0] for _ in range(len(pz))]

def con_pointsZ(o, q, pz):
    pg.draw.line(WIN, 'white',(pz[o][1], pz[o][0]),
                                (pz[q][1], pz[q][0]))
########################## PROGRAMA
clock = pg.time.Clock()
while True:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()

    pg.mixer.music.play(loops=-1)
    pg.mixer.music.set_volume(0.1)

    rotation_z = np.matrix([[cos(ANGLE), -sin(ANGLE), 0],
                            [sin(ANGLE), cos(ANGLE), 0],
                            [0, 0, 1] ])

    rotation_y = np.matrix([[cos(ANGLE), 0, sin(ANGLE)],
                           [0, 1, 0],
                           [-sin(ANGLE), 0, cos(ANGLE)]])

    rotation_x = np.matrix([[1, 0, 0],
                            [0, cos(ANGLE), -sin(ANGLE)],
                            [-sin(ANGLE), 0, cos(ANGLE)] ])

    ANGLE += 0.01
    WIN.fill('black')
    i = 0
    u = 0
    a = 0
    for point in px:
        rotated2d = np.dot(rotation_z, point.reshape(3, 1))
        rotated2d = np.dot(rotation_y, rotated2d)
        rotated2d = np.dot(rotation_x, rotated2d)

        projected2d = np.dot(pro_matrixX, rotated2d)
        projected3d = np.dot(pro_matrixX, rotated2d)
        
        x = int(projected2d[0, 0] * ESCALA) + CIRCLE_POS[0]
        y = int(projected2d[1, 0] * ESCALA) + CIRCLE_POS[1]
  
        b = int(projected3d[1, 0] * ESCALA) + CIRCLE_POS[0]
        c = int(projected3d[0, 0] * ESCALA) + CIRCLE_POS[1]

        d = int(projected2d[0, 0] * ESCALA) + CIRCLE_POS[0]
        e = int(projected2d[1, 0] * ESCALA) + CIRCLE_POS[1]
        pro_pointsX[i] = [x, y]
        pg.draw.circle(WIN, 'deep pink', (x, y), 5)
        i += 1

        pro_pointsY[u] = [b, c]
        pg.draw.circle(WIN, 'red', (b, c), 5)
        u -= 1
        WIN.blit(tex, [120, 80])
#        pro_pointsZ[a] = [d, e]#x,c
#        pg.draw.circle(WIN, 'blue',(d, e), 5) ##x,c
#        a -= 1 
        
#        pg.draw.circle(WIN, 'yellow',(b, y), 5)##b, y
    con_pointsX(1, 2, pro_pointsX) 
    con_pointsX(1, 3, pro_pointsX)
    con_pointsX(2, 3, pro_pointsX)
    con_pointsX(0, 3, pro_pointsX)
    con_pointsX(0, 2, pro_pointsX)
    con_pointsX(0, 1, pro_pointsX)
    
    con_pointsY(1, 2, pro_pointsY)
    con_pointsY(1, 3, pro_pointsY)
    con_pointsY(2, 3, pro_pointsY)
    con_pointsY(0, 3, pro_pointsY)
    con_pointsY(0, 2, pro_pointsY)
    con_pointsY(0, 1, pro_pointsY)
    
#    texto(WIN, arial, str("demostracion"), 'cyan', 40, 100, 100)
    pg.display.update()

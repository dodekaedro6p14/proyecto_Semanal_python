import pygame as pg
pg.init()

SIZE = (1080, 720)
##### CREACION DE LA VENTANA #############
pg.display.set_caption("    Mi TRASTORNO CARDIVASCULAR; transtorno.py   ")
SCREEN = pg.display.set_mode(SIZE)
IMAGE  = pg.image.load("cardio_sanginio.jpg").convert()
IMAGEN_LIBRO = pg.image.load("libro_cardio.png").convert()
clock  = pg.time.Clock()

########## DIMENCIONES  ################
DERECHO_1 = 50  ## manipulando dimenciones
CHO_1A    = 25
CHO_1B    = 10

DERECHO_2 = 20
DERECHO_UP1 = 45
DERECHO_UP2 = 35
DERECHO_UP3 = 35
DERECHO_UP4 = 20
MEDIO_DW1 = 15
MEDIO_DW2 = 50
MEDIO_DW3 = 35

IZQUIERDO_GRA = 35
GRA1          = 35


IZQUIERDO_MIN = 5

############ VELOCIDAD DEL LATIDO

SPEED_DER1 = 3
SPEED_DER2 = 3
SPEED_CHO_1A = 3
SPEED_CHO_1B = 3
SPEED_UP1 = 3
SPEED_UP2 = 3
SPEED_UP3 = 3
SPEED_UP4 = 3
SPEED_DW1 = 3
SPEED_DW2 = 3
SPEED_DW3 = 3
SPEED_IZQ = 3
SPEED_GRA1 = 3

while True:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()

    if (DERECHO_1 > 70 or DERECHO_1 < 30):
        SPEED_DER1 *= -1

    if (DERECHO_2 > 35 or DERECHO_2 < 17):
        SPEED_DER2 *= -1
        
    if (DERECHO_UP1 > 60 or DERECHO_UP1 < 30):
        SPEED_UP1 *= -1

    if (DERECHO_UP2 > 50 or DERECHO_UP2 < 30):
        SPEED_UP2 *= -1

    if (DERECHO_UP3 > 50 or DERECHO_UP3 < 30):
        SPEED_UP3 *= -1

    if (DERECHO_UP4 > 35 or DERECHO_UP4 < 17):
        SPEED_UP4 *= -1

    if (MEDIO_DW1 > 20 or MEDIO_DW1 < 10):
        SPEED_DW1 *= -1

    if (MEDIO_DW2 > 70 or MEDIO_DW2 < 40):
        SPEED_DW2 *= -1

    if (MEDIO_DW3 < 30 or MEDIO_DW3 > 45):
        SPEED_DW3 *= -1

    if (IZQUIERDO_GRA < 30 or IZQUIERDO_GRA > 45):
        SPEED_IZQ *= -1

    if (GRA1 < 30 or GRA1 > 45):
        SPEED_GRA1 *= -1

    if (CHO_1A > 50 or CHO_1A < 30):
        SPEED_CHO_1A *= -1

    if (CHO_1B > 50 or CHO_1B < 30):
        SPEED_CHO_1B *= -1

    DERECHO_1 += SPEED_DER1
    DERECHO_2 += SPEED_DER2
    DERECHO_UP1 += SPEED_UP1
    DERECHO_UP2 += SPEED_UP2
    DERECHO_UP3 += SPEED_UP3
    DERECHO_UP4 += SPEED_UP4
    MEDIO_DW1 += SPEED_DW1
    MEDIO_DW2 += SPEED_DW2
    MEDIO_DW3 -= SPEED_DW3
    IZQUIERDO_GRA -= SPEED_IZQ
    GRA1 += SPEED_GRA1
    CHO_1A += SPEED_CHO_1A
    CHO_1B += SPEED_CHO_1B

############### BACKGRAUND ##############
    MOUSE_POS = pg.mouse.get_pos()
    print(MOUSE_POS)
    SCREEN.fill('black')
    SCREEN.blit(IMAGE, [-187, 0])
############### UBICACIONES DEL CORAZON
    pg.draw.circle(SCREEN, 'red', (639, 539), DERECHO_UP4)
    pg.draw.circle(SCREEN, 'blue', (518, 348), IZQUIERDO_GRA)
    pg.draw.circle(SCREEN, 'green', (547, 358), GRA1)
#    pg.draw.circle(SCREEN, 'red', (504, 366), MEDIO_DW3)
    
#    pg.draw.circle(SCREEN, 'red', (593, 294), DERECHO_2)
#    pg.draw.circle(SCREEN, 'red', (550, 460), DERECHO_1)
#    pg.draw.circle(SCREEN, 'blue', (581, 413), CHO_1A)
#    pg.draw.circle(SCREEN, 'gree', (628, 419), CHO_1B)
#    pg.draw.circle(SCREEN, 'red', (598, 457), DERECHO_UP1)
#    pg.draw.circle(SCREEN, 'red', (580, 500), DERECHO_UP2)

#    pg.draw.circle(SCREEN, 'red', (708, 447), DERECHO_UP3)
#    pg.draw.circle(SCREEN, 'red', (650, 568), MEDIO_DW1)
#    pg.draw.circle(SCREEN, 'red', (720, 530), MEDIO_DW2)

#    SCREEN.blit(IMAGEN_LIBRO, [50, 200])

    pg.draw.aaline(SCREEN, 'blue', (0, 360), (1080, 360), 1)
    pg.draw.aaline(SCREEN, 'red', (540, 0), (540, 720), 1)

    pg.display.flip()
    clock.tick(30)

import pygame, sys
pygame.init()

SIZE = (1080, 720)
##### CREACION DE LA VENTANA #############
pygame.display.set_caption("    Mi TRASTORNO CARDIVASCULAR; transtorno.py   ")
SCREEN = pygame.display.set_mode(SIZE)
#IMAGE  = pygame.image.load("cardio_sanginio.jpg").convert()
#IMAGEN_LIBRO = pygame.image.load("libro_cardio.png").convert()
clock  = pygame.time.Clock()

########## DIMENCIONES  ################
DERECHO_1 = 50  ## manipulando dimenciones
CHO_1A    = 35
CHO_1B    = 35
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
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
    MOUSE_POS = pygame.mouse.get_pos()
    print(MOUSE_POS)
    SCREEN.fill('white')
#    SCREEN.blit(IMAGE, [0, 0])
############### UBICACIONES DEL CORAZON
    pygame.draw.circle(SCREEN, 'red', (630, 343), DERECHO_UP4)
    pygame.draw.circle(SCREEN, 'red', (518, 348), IZQUIERDO_GRA)
    pygame.draw.circle(SCREEN, 'red', (547, 358), GRA1)
    pygame.draw.circle(SCREEN, 'red', (504, 366), MEDIO_DW3)
    
    pygame.draw.circle(SCREEN, 'red', (593, 294), DERECHO_2)
    pygame.draw.circle(SCREEN, 'red', (550, 460), DERECHO_1)
    pygame.draw.circle(SCREEN, 'red', (581, 413), CHO_1A)
    pygame.draw.circle(SCREEN, 'red', (628, 419), CHO_1B)
    pygame.draw.circle(SCREEN, 'red', (598, 457), DERECHO_UP1)
    pygame.draw.circle(SCREEN, 'red', (580, 500), DERECHO_UP2)

    pygame.draw.circle(SCREEN, 'red', (708, 447), DERECHO_UP3)
    pygame.draw.circle(SCREEN, 'red', (650, 568), MEDIO_DW1)
    pygame.draw.circle(SCREEN, 'red', (720, 530), MEDIO_DW2)

#    SCREEN.blit(IMAGEN_LIBRO, [50, 200])
    pygame.display.flip()
    clock.tick(30)

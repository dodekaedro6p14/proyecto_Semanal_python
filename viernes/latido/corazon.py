import pygame as pg
pg.init()

size    =  (1080, 720)
#### Crear Ventana
pg.display.set_caption("MI TRASTORNO CARDIOVASCULAR") 
screen = pg.display.set_mode(size)
clock  = pg.time.Clock()
IMAGE = pg.image.load("corazon.jpg").convert()
############## coordenadas
coord_x = 400
coord_y = 200
######## velocidad del cuadrado
speed_x = 3
speed_y = 3
run = True
while run:    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
                break

    if (coord_x > 1000 or coord_x < 0):
        speed_x *= -1

    coord_x += speed_x
    screen.blit(IMAGE, [0, 0])
    #### ZONA DE DIBUJO
    pg.draw.rect(screen, 'red', (coord_x, coord_y, 80, 80))

    pg.display.flip()
    clock.tick(30)

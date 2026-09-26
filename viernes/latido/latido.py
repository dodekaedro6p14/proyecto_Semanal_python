import pygame as pg 

pg.init()
pg.display.set_caption("LATIDOS DEL CORAZON")
WIDTH, HEIGHT = 1080, 720
WIN = pg.display.set_mode((WIDTH, HEIGHT))
#BG = pygame.transform.scale(pygame.image.load(""), (WIDTH, HEIGHT))
clock  = pg.time.Clock()
derecho_up = 100 
izquierdo_dn = 80 
########### velocidad del circulo
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

    if (derecho_up > 120 or derecho_up < 90):
        speed_x *= -1
    
    if (izquierdo_dn < 70 or izquierdo_dn > 100):
        speed_y *= -1
  
    derecho_up += speed_x
    izquierdo_dn -= speed_y
    WIN.fill("black")

    pg.draw.circle(WIN, "blue", (500, 250), derecho_up)
    pg.draw.circle(WIN, "red", (400, 400), izquierdo_dn)
    pg.display.flip()
    clock.tick(30)

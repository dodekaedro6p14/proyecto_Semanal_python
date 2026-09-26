import pygame as pg
import numpy as ns
import math

#DISEÑO DE LA VENTANA
WIDTH, HEIGHT = 1080, 720
pg.display.set_caption("C0R4Z0N D3 D14 V13RN35")
WIN = pg.display.set_mode((WIDTH, HEIGHT))
BG = pg.transform.scale(pg.image.load("image_dorso.jpg"), (WIDTH, HEIGHT))
surface = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
FPS = 60
timer = pg.time.Clock()

MONO_W = 40
MONO_H = 80
# DISEÑANDO OBJETO
def draw_screen():
    pg.draw.rect(surface, (255, 0, 0, 55), [540, 360, 50, 50])
    pg.display.update()

def draw(player):
    WIN.blit(BG, (0, 0))
    pg.draw.rect(WIN, "red", player)
    pg.display.update()

# DESARROLLO DEL JUEGO
def main():
    run = True
    player = pg.Rect(200, HEIGHT - MONO_H, MONO_W, MONO_H)
    while run:
        timer.tick(FPS)
        WIN.blit(surface, (0, 0))
        draw_screen()
       
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                    break

            draw(player)
            pg.draw.circle(WIN, 'yellow',(540, 360),150, width = 5)
            pg.draw.arc(WIN, 'cyan', ((40, 160), (360,360)), 0, math.pi/2, width = 10)
            pg.draw.arc(WIN, 'black', ((0,540), (180, 180)), 0, math.pi/2, width=10 )
#            draw(player)
        pg.display.flip()
    pg.quit()


#    pointslist = ((0,0), (100, 100),(0, 100))
#    p1 = ((540,0),(540, 720))
#    p2 = ((0,360),(1080, 360))
#    p3 = (540, 0)
#    p4 = (540, 720)
#    START_ANGLE = (90)     
#    STOP_ANGLE = 180
#    MEDIO = ((540, 360), (100,100))
#    TRIAGULO = ((540, 600), (300, 250), (800, 250))

#    pygame.draw.circle(SCREEN, CYAN, (540, 360),150, width = 5)
#    pygame.draw.ellipse(SCREEN, YELLO, ((350, 360),(200, 100)),  width = 5)
#    pygame.draw.polygon(SCREEN, VERDE, TRIAGULO, width = 5)
#    pg.draw.arc(WIN, 'black', 120, 0, 90, width = 1)
#        pg.draw.aalines(WIN, ('blue'), (p1), (p2), blend = 1)
#    pygame.draw.aaline(SCREEN, RED, p3, p4, blend = 1)

if __name__ == "__main__":
    main()


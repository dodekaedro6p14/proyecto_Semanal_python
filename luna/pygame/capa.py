import pygame as pg
import random  

pg.init()
WIDTH, HEIGHT = 1080, 720
pg.display.set_caption("F3N0M3N05 3N3RG1C05 D3L UN1V3R50")
#BG = pg.transform.scale(pg.image.load("ima/fondo_demo.jpg"), (WIDTH, HEIGHT))
WIN = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 60
MOVE = 5
def draw():   
    WIN.blit(BG, [0, 0])
    pg.display.update()

def main():
    clock = pg.time.Clock()
   
    run = True
    while run:

        clock.tick(FPS)	
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                    break

            draw()

    pg.quit()
    quit()

if __name__ == "__main__":
    main()

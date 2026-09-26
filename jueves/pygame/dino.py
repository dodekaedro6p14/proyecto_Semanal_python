import pygame as pg 

pg.init()
WIDTH, HEIGHT  = 1080, 720
pg.display.set_caption("3J3CU74ND0 L'  PR0GR4M4")
BG = pg.transform.scale(pg.image.load("ima/geometria.png"), (WIDTH, HEIGHT))
WIN = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 60
a_punto = 50
b_punto = 50
class Objeto():
    def __init__(self, x, y ,width, height):
        self.rect = pg.Rect(x, y, width, height)
        
def draw(objeto):
    pg.draw.rect(WIN, 'red', objeto)
    pg.display.update()   
       
def fondo(self, objeto):
    WIN.blit(BG, [0, 0])

def main():
    run  = True
    clock = pg.time.Clock()

    objeto = Objeto(a_punto, b_punto, 50, 50) 
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

            draw(objeto)
            fondo(objeto, WIN)
    
    pg.quit()
    quit()

if __name__ == "__main__":
    main()

import pygame as pg

pg.init()
pg.mixer.init()
WIDTH, HEIGHT= 1080, 720
pg.display.set_caption("3RUPC10N VOLC4N1C4")
#BG = pg.transform.scale(pg.image.load("fondo_volcan.jpg"), (WIDTH, HEIGHT))
WIN = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 60    

class Objeto():
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(x, y, width, height)

def draw(objeto):
    pg.draw.rect(WIN, "red", objeto)
    pg.display.update()

def fondo(self, objeto):
    WIN.fill((0,0,0))

def main():
    run = True
    clock = pg.time.Clock()
    objeto = Objeto(WIDTH/2, HEIGHT/2, 20, 20)
    
    der_up = 540
    izq_dw = 320
    speed_x = 5
    speed_y = 3
    while run:
        clock.tick(FPS) 
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                    break
    
            if (der_up < 0  or der_up > 1080):
                speed_x *= -1

            if (izq_dw < 0 or izq_dw > 720):
                speed_y *= -1
            
            izq_dw += speed_y
            der_up -= speed_x # valores eje [+=]

            fondo(objeto, WIN)
            pg.draw.circle(WIN, 'yellow', (der_up, izq_dw), 20)
      #      draw(objeto)
      #      pg.display.update()

if __name__ == "__main__":
    main()   

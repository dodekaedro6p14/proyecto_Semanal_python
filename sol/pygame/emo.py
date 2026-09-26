##  pygame/ima=cuadricula.avif; sond=space.mp3; (vertices, lineas == emo.py/domingo/pygame)

import pygame as pg

pg.init()
WIDTH, HEIGHT  = 1600,900 
#pg.display.set_caption("3J3CU74ND0 L'  PR0GR4M4")
BG = pg.transform.scale(pg.image.load("domingo.avif"), (WIDTH, HEIGHT))
WIN = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 60

class Objeto():
    def __init__(self, x, y ,w, h):
        self.rect = pg.Rect(x, y, w, h)
        
def draw(objeto1, objeto2):
    pg.draw.rect(WIN, 'red', objeto1)
    pg.draw.rect(WIN, 'blue', objeto2)
    pg.display.update()   
       
def fondo(self, objeto1, objeto2):
    WIN.blit(BG, [-7, 10])

def main():
    run  = True
    clock = pg.time.Clock()
    w = 50
    h = 50
    
    der_up = 400
    izq_dw = 200
    speed_x = 0.5
    speed_y = 0.5

    objeto1 = Objeto(WIDTH/4, HEIGHT/4, 25, 25)# tamano del cubo 
    objeto2 = Objeto(WIDTH/3, HEIGHT/3, 25, 25)
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False                    
                    break 

        if (der_up > 1340 or der_up < 0):
            speed_x *= -1

        if (izq_dw < 45 or izq_dw > 785):
            speed_y *= -1
        
        der_up += speed_x
        izq_dw -= speed_y

        fondo(objeto1, objeto2, WIN)
#        pg.draw.rect(WIN, 'green', (der_up, izq_dw, 25, 25))
        pg.draw.rect(WIN, 'green', (der_up, izq_dw, 25, 25))

        pun = pg.draw.circle
        pun(WIN, 'red', (800, 450), 5)
        pun(WIN, 'red', (800, 50), 5)
        pun(WIN, 'red', (800, 800), 5)


        pun(WIN, 'cyan', (120, 450), 5)
        pun(WIN, 'cyan', (1480, 450), 5)
        draw(objeto1, objeto2)
## ubicaciones de los puntos
#        pun = pg.draw.circle
#        pun(WIN, 'red', (683, 384), 5)




if __name__ == "__main__":
    main()

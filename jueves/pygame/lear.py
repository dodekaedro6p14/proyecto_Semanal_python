import pygame as pg

pg.init()
pg.mixer.init()
WIDTH, HEIGHT= 1080, 720
pg.display.set_caption('P0S1BL3 LSYST3M')
#BG = pg.transform.scale(pg.image.load("geometria.png"), (WIDTH, HEIGHT))
WIN = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 60
a_punto = 100
b_punto = 100
class Objeto():
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(x, y, width, height)
 
    def draw(objeto):
        pg.draw.rect(WIN, "blue", objeto)
        pg.display.update()

    def fondo(self, objeto):
        WIN.fill('black')

class App:
    def __init__(self) -> None:
        self.in_run = False
        self.clock = pg.time.Clock()
        
        objeto = Objeto(a_punto, b_punto, 50, 50)

    def main():
        in_run = True
        clock = pg.time.Clock()

        objto = Objeto(a_punto, b_punto, 50, 50)

        while in_run:
            clock.tick(FPS)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_run = False
                    quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        in_run = False
                        break


                draw(objeto)
                fondo(objeto, WIN)
#    def draw(self, WIN):
#        self.WIN.fill("black")
#        self.WIN.blit(BG, [0, 0])
        self.Objeto
#            WIN.fill(0, 0, 0)
#    x_lado += 10
#    y_lado += 25
    
 
if __name__ == "__main__":
    app = App()
#    app.in_run()


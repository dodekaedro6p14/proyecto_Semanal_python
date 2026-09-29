import pygame as pg
import random as rn

pg.mixer.init()
WIDTH, HEIGHT= 1080, 720
pg.display.set_caption("3RUPC10N VOLC4N1C4")
#BG = pg.transform.scale(pg.image.load("fondo_volcan.jpg"), (WIDTH, HEIGHT))
WIN = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 60    

#### agregamos el humo

class Humo(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = pg.image.load("ima/luz_roja_c.jpg").convert()
        #self.image.set_colorkey([255,255,255])
        #self.rect = self.image.get_rect()


pg.init()
clock = pg.time.Clock()
done = False

humo_list = pg.sprite.Group()
all_sprite_list = pg.sprite.Group()

for i in range(50): ##cantidad de humo
    humo = Humo()
    #humo.rect.x = rn.randrange(0, 610)
    #humo.rect.y = rn.randrange(200, 310)

    humo_list.add(humo)
    all_sprite_list.add(humo)

while not done:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                done = False
                pg.quit(); exit()

    WIN.fill((0,0,0))
    #all_sprite_list.draw(WIN)

    pg.display.flip()
    clock.tick(FPS)



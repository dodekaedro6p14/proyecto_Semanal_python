import pygame, random
pygame.init()

################################## Crear Ventana
WHITE  = (255, 255, 255)
BLACK  = (  0,   0,   0)


pygame.display.set_caption("         OBSERVAR LOS COPOS DE NIEVE ")
done = False

######################################## clase
class Copos_nieve(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #self.image = pygame.image.load("copos_nieve.jpg").convert()
        self.image = pygame.Surface([10, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1

        if self.rect.y > 720:
            self.rect.y = -15
            self.rect.x = random.randrange(1080)

SCREEN = pygame.display.set_mode([1080, 720])
#IMAGEN_FONDO = pygame.image.load("fondo_4.jpg").convert()
#IMAGEN_LIBRO = pygame.image.load("noche.jpg").convert()
clock = pygame.time.Clock()

##############################
copos_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(20):
    copos = Copos_nieve()
    copos.rect.x = random.randrange(1080)
    copos.rect.y = random.randrange(720)

    copos_list.add(copos)
    all_sprite_list.add(copos)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprite_list.update()
################################## bacKground

    SCREEN.fill(WHITE)
    #SCREEN.blit(IMAGEN_FONDO, [0, 0])
    all_sprite_list.draw(SCREEN)
    #SCREEN.blit(IMAGEN_LIBRO, [100, 200])
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

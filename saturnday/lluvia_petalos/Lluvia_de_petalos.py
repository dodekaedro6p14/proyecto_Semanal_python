import pygame, random
pygame.init()
#################### CREANDO VENTANA
WHITE  = (255, 255, 255)
BLACK  = (  0,   0,   0)
DEEPPINK=(255,  20, 147)
GREEN  = (  0, 255,   0)

pygame.display.set_caption("     LLUVIA DE PETALOS")
done = False
############################## CLASE    
class Petalos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("petaloslilatamañosTRE.jpg")
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1

        if self.rect.y > 720:
            self.rect.y = -15
            self.rect.x = random.randrange(1080)


SCREEN = pygame.display.set_mode([1080, 720])
IMAGEN_FONDO = pygame.image.load("sahuraagua3.jpg").convert()
IMAGEN_NOCHE = pygame.image.load("noche.jpg").convert()
clock = pygame.time.Clock()

################################ movimientos
petalos_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(10):
    petalo = Petalos()
    petalo.rect.x = random.randrange(1080)
    petalo.rect.y = random.randrange(720)

    petalos_list.add(petalo)
    all_sprite_list.add(petalo)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprite_list.update()
########################## background 
    
    SCREEN.fill(WHITE)
    SCREEN.blit(IMAGEN_FONDO, [0, 0])
    all_sprite_list.draw(SCREEN)
    SCREEN.blit(IMAGEN_NOCHE, [100, 200])
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

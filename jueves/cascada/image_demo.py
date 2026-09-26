import pygame

pygame.init()
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)

WIDTH, HEIGHT = 1080, 720
FPS = 60

pygame.display.set_caption("P03S14 1N PR0GR4M1NG")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
#FONDO = pygame.image.load("image.jpg").convert()

def imagen():
#    SCREEN.blit(FONDO, [0, 0])
    pygame.display.update()
    pass

def main(SCREEN):
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
	
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    break

        imagen()
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(SCREEN)
	

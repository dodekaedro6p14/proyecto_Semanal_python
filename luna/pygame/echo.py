import sys
import random
import typing
import pygame as pg

pg.init()
pg.mixer.init()
SCREEN_SIZE = (1080, 720)
PARTICLE_COUNT = 20
pg.mixer.music.load("../../mus/viento.mp3")
pg.mixer.music.play(-1)
pg.display.set_caption("C0M0 CR30 QU3 3S 3L UN1V3RS00")
#BG = pg.image.load("ima/fondo_demo.jpg")
cam_x = 0
cam_y = 0
class Particle:
    def __init__(self, pos: typing.List[int], radius: int, speed: int) -> None:
        self.pos = pos
        self.radius = radius
        self.speed = speed

    def update(self, dt):
        self.pos[0] -= self.speed * dt
        if self.pos[0] < -100:
            self.pos[0] = SCREEN_SIZE[0] + 100

    def draw(self, screen):
        pg.draw.circle(screen, "white", self.pos, self.radius)

class ParticleManager:
    def __init__(self) -> None:
        self.particles: typing.List[Particle] = []

    def update(self, dt):
        for particle in self.particles:
            particle.update(dt)

    def add_particles(self):
        for _ in range(PARTICLE_COUNT):
            particle = Particle(
                pos=[random.randint(-400, SCREEN_SIZE[0] + 100),
                     random.randint(-100, SCREEN_SIZE[1] + 100),],
                radius=random.randint(1, 3),
                speed=random.randint(2, 4),)  ###(4, 8)
            self.particles.append(particle)

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)

class App:
    def __init__(self) -> None:
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.is_running = False
        self.dt = 0
        self.events = []
        self.particle_manager = ParticleManager()
        
    def run(self):
        self.is_running = True
        self.particle_manager.add_particles()
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()
            pg.display.update()
            self.dt = self.clock.tick(60) /90  ##18

    def handle_events(self):
        self.events = pg.event.get()
        for event in self.events:
            if event.type == pg.QUIT:
                self.is_running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.is_running = False
                    break
                        
    def update(self):
        self.particle_manager.update(self.dt)

    def draw(self):
        global cam_x
        global cam_y
        self.screen.fill("black")
        # self.screen.blit(BG, (cam_x, cam_y))
        cam_x -= 0.05
        cam_y -= 0.05

        self.particle_manager.draw(self.screen)

if __name__ == "__main__":

    app = App()
    app.run()

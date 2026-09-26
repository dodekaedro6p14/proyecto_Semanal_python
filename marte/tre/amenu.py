from diso_3d import *
from camara import *
from projection import *
import pygame as pg

class Objeto:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 600, 400
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.is_running = False
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [0.5, 0.5, -9])      #default [0.5, 1, -4]
        self.projection = Projection(self)
        self.object = Demo_3D(self)
        self.object.translate([0.2, 0.4, 0.2])
        self.object.rotate_y(math.pi / 6)

    def draw(self):
        self.screen.fill(pg.Color('black'))
        self.object.draw()

    def run(self):
        self.is_running = True
        while self.is_running:
            self.end_game()
            self.draw()
            self.camera.control()
            
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

    def end_game(self):
        self.events = pg.event.get()
        for event in self.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.is_running = False
                    break

if __name__ == '__main__':
    app = Objeto()
    app.run()

import pygame as pg
from vars import *
"""
This file handle the process of a whole level.
It handle how hard it is, the differents animations, etc.
"""

class Button(pg.sprite.Sprite):

    def __init__(self, rect, action, image = None):
        "docstring du module init"

        pg.sprite.Sprite.__init__(self)             # Superclass

        if not isinstance(rect, pg.Rect):
            rect = pg.Rect(rect)
        if image:
            self.image = pg.image.load(image)
            self.image = pg.transform.scale(self.image, (rect.width, rect.height))
        else:
            self.image = pg.Surface((rect.width, rect.height))

        self.rect = self.image.get_rect()
        self.rect.move_ip(rect.x, rect.y)


class Accueil():

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.bg = pg.Color(42, 135, 32)

        self.buttons = pg.sprite.Group()

        self.buttons.add(Button([10,20,100,200], cry))

    def run(self):

        running = True

        while running:

            self.draw()
            self.update()
            self.keys()

            CLOCK.tick(FRAMERATE)

    def draw(self):
        "Dessine le contenu de l'ecran"
        self.screen.fill(self.bg)

        self.buttons.draw(self.screen)

        pg.display.flip()

    def update(self):
        pass

    def keys(self):
        pass


def cry():
    print("it worked !")


if __name__ == '__main__':

    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    page = Accueil(screen, CLOCK)

    page.run()

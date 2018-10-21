#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from vars import *
"""
This file handle the process of a whole level.
It handle how hard it is, the differents animations, etc.
"""

class Button(pg.sprite.Sprite):

    def __init__(self, rect, action, args, text=None, image=None):
        "docstring du module init"

        pg.sprite.Sprite.__init__(self)             # Superclass

        if not isinstance(rect, pg.Rect):
            rect = pg.Rect(rect)
        if image:
            self.image = pg.image.load(image).convert_alpha()
            self.image = pg.transform.scale(self.image, (rect.width, rect.height))
        else:
            self.image = pg.Surface((rect.width, rect.height))

        self.rect = self.image.get_rect()
        self.rect.move_ip(rect.x, rect.y)

        self.action = action
        self.args = args

    def update(self):

        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.image.fill(pg.Color(100,150,100))
        else:
            self.image.fill(pg.Color(110,159,200))


class Page():

    def __init__(self, screen, sprite_list, clock, bg_color = (0,0,0)):
        self.screen = screen
        self.clock = clock
        self.bg = bg_color

        self.sprite_list = sprite_list


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

        self.sprite_list.draw(self.screen)

        pg.display.flip()

    def update(self):
        self.sprite_list.update()

    def keys(self, event_list = None):
        if not event_list:
            event_list = pg.event.get()

        for event in event_list:

            if event.type == pg.MOUSEBUTTONDOWN:
                for b in (b for b in self.sprite_list if isinstance(b, Button)):
                    if b.rect.collidepoint(pg.mouse.get_pos()):
                        b.action(*b.args)

def switch_page(current, new):
    "Éteind la page `current' et lance la page `new'."
    current.running = False
    new.run()

if __name__ == '__main__':

    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    accueil = Page(screen, pg.sprite.Group(), CLOCK, (255,255,255))
    tuto = Page(screen, pg.sprite.Group(), CLOCK)

    Button([SCREEN_WIDTH // 4,
                SCREEN_HEIGHT // 2,
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 8 - 10], switch_page, (accueil, tuto)).add(accueil.sprite_list)

    Button([SCREEN_WIDTH // 4,
                5 * SCREEN_HEIGHT // 8,
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 8 - 10], switch_page, (accueil, tuto)).add(accueil.sprite_list)

    Button([SCREEN_WIDTH // 4,
                5 * SCREEN_HEIGHT // 8,
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 8 - 10], switch_page, (tuto, accueil)).add(tuto.sprite_list)

    current_page = accueil
    current_page.run()

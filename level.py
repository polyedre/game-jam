#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
import random
import aliments as al
import sound
from vars import *

"""
This file handles the process of a whole level.
It handles how hard it is, the differents animations, etc.
"""

def home_page_action():
    liste = []
    r = random.randint(0,1000)
    if r > 800:
        aliment = al.create_new_aliment()
        liste.append(aliment)
    return liste

class Button(pg.sprite.Sprite):

    def __init__(self, rect, action, args, text=None, image=None):
        "Docstring du module init"

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

        self.text_surface = FONT.render(text, True, (0,0,0))
        self.text_surface_rect = self.text_surface.get_rect()
        self.text_surface_rect.center = (self.rect.width // 2,
                                    self.rect.height // 2)

        self.image.blit(self.text_surface, (10,10))

        self.action = action
        self.args = args

    def update(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.image.fill(pg.Color(100,150,100))
        else:
            self.image.fill(pg.Color(110,159,200))
        self.image.blit(self.text_surface, self.text_surface_rect)


class Text(pg.sprite.Sprite):

    def __init__(self, text, pos, font=None, color=(255,255,255), centered=True):
        "Docstring du module init"

        pg.sprite.Sprite.__init__(self)             # Superclass

        if not font:
            self.font = FONT

        self.image = FONT.render(text, True, color, (20,20,20))
        self.rect = self.image.get_rect()
        if centered:
            self.rect.center = pos
        else:
            self.rect.move_ip(*pos)


class Page():

    def __init__(self, screen, sprite_list, clock, bg_color = (0,0,0), function=None, music=None):
        self.function = function
        self.screen = screen
        self.clock = clock
        self.bg = bg_color

        self.hooked_function = lambda : None
        self.hooked_args = None
        self.sprite_list = sprite_list
        if music:
            self.music = music

    def run(self, is_first=False):

        running = True

        if is_first:
           self.music.play(-1)
        
        while running:

            self.update()
            if self.function:
                liste = self.function()
                for elem in liste:
                    elem.add(self.sprite_list)
            if self.bg:
                self.draw()
            if self.hooked_args:
                self.hooked_function(*self.hooked_args)
            else:
                self.hooked_function()
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
            if event.type == pg.QUIT:
                pg.quit()
                exit(0)
            if event.type == pg.MOUSEBUTTONDOWN:
                for b in (b for b in self.sprite_list if isinstance(b, Button)):
                    if b.rect.collidepoint(pg.mouse.get_pos()):
                        if b.args:
                            b.action(*b.args)
                        else:
                            b.action()


def switch_page(current, new):
    "Éteind la page `current' et lance la page `new'."
    if current.music != new.music:
        current.music.fadeout(100)
        new.music.play(-1)
    current.running = False
    new.run()

def init(screen):

    pages = {}

    accueil = Page(screen, pg.sprite.Group(), CLOCK, (255,255,255),
                   function=home_page_action, music=sound.intro_music)
    tuto = Page(screen, pg.sprite.Group(), CLOCK,(0,0,0),function=home_page_action, music=sound.intro_music)
    victory = Page(screen, pg.sprite.Group(), CLOCK, (110,200,100),function=home_page_action, music=sound.intro_music)
    defeat = Page(screen, pg.sprite.Group(), CLOCK, (250,100,100),function=home_page_action, music=sound.intro_music)
    play = Page(screen, pg.sprite.Group(), CLOCK, bg_color = None, music=sound.run_music)

    Button([SCREEN_WIDTH // 4, 5 * SCREEN_HEIGHT // 8,
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8 - 10],
           switch_page, (accueil, tuto),
           text="Tutoriel").add(accueil.sprite_list)

    Button([SCREEN_WIDTH // 4, 6 * SCREEN_HEIGHT // 8,
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8 - 10],
           exit, None,
           text="Quitter").add(accueil.sprite_list)

    Button([SCREEN_WIDTH // 4, 5 * SCREEN_HEIGHT // 8,
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8 - 10],
           switch_page, (tuto, accueil),
           text="Retour").add(tuto.sprite_list)

    texts = ['Vous êtes Martine, ', 'la voix dans la tête de Jean-Paul.', 'Votre mission, si vous l\'acceptez,', 'est d\'empêcher Jean-Paul d\'aller faire du sport.', 'Pour cela, gavez le d\'Hamburgers !' ]

    for i, line in enumerate(texts):
        Text(line, (SCREEN_WIDTH // 2, SCREEN_WIDTH // 6 + i * 40)).add(tuto.sprite_list)

    Text("Vous avez gagné !", (SCREEN_WIDTH // 2, 2 * SCREEN_HEIGHT // 8)).add(victory.sprite_list)
    Text("Jean-Paul n'a pas pu aller faire du sport", (SCREEN_HEIGHT // 2, 3 * SCREEN_WIDTH // 8)).add(victory.sprite_list)
    Text("il est mort d'obesité. Bravo", (SCREEN_WIDTH // 2, 4 * SCREEN_HEIGHT // 8)).add(victory.sprite_list)

    Text("Vous avez perdu !", (SCREEN_WIDTH // 2, 2 * SCREEN_HEIGHT // 8)).add(defeat.sprite_list)
    Text("Jean-Paul a pu aller faire du sport", (SCREEN_WIDTH // 2, 3 * SCREEN_HEIGHT // 8)).add(defeat.sprite_list)
    Text("il est toujours vivant. Je ne vous félicite pas.", (SCREEN_WIDTH // 2, 4 * SCREEN_HEIGHT // 8)).add(defeat.sprite_list)

    Button([SCREEN_WIDTH // 4, 5 * SCREEN_HEIGHT // 8,
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8 - 10],
           switch_page, (victory, accueil),
           text="Accueil").add(victory.sprite_list)

    Button([SCREEN_WIDTH // 4, 5 * SCREEN_HEIGHT // 8,
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8 - 10],
           switch_page, (defeat, accueil),
           text="Accueil").add(defeat.sprite_list)

    Button([SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2,
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8 - 10],
           switch_page, (accueil, play),
           text="Jouer").add(accueil.sprite_list)

    pages['accueil'] = accueil
    pages['tuto'] = tuto
    pages['victoire'] = victory
    pages['defeat'] = defeat
    pages['play'] = play

    return pages


if __name__ == '__main__':

    pg.init()
    pg.font.init()

    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    pages = init()

    pages["accueil"].run(True)

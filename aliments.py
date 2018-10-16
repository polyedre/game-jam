#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
import random

from main import GAME_NAME, SCREEN_HEIGHT, SCREEN_WIDTH

FOOD_LIST = pg.sprite.Group()
GRAVITY = pg.math.Vector2(0,0)

class Aliment(pg.sprite.Sprite):
    """
    Classe aliment d'un jeu. Chaque aliment est un objet qui se déplace suivant une vitesse.
    L'aliment peut être 'Healthy' ou non.
    """

    def __init__(self, _position, _vitesse, _healthy, _size):

        pg.sprite.Sprite.__init__(self)             # Superclass
        self.is_healthy = _healthy
        self.vitesse = pg.math.Vector2(_vitesse)
        self.acceleration = pg.math.Vector2(0, 0)

        self.image = pg.Surface([_size,_size])
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = _position


    def update(self):
        "Met à jour les positions et vitesses de l'objet"
        self.remove_if_out()

        self.acceleration += GRAVITY
        self.vitesse += self.acceleration
        self.rect.move_ip(*self.vitesse)
        self.acceleration *= 0


    def draw(self, screen):
        "Dessine l'aliment sur l'écran 'screen'"
        color = ((100, 255, 100) if self.is_healthy else (255, 100, 100))
        pg.draw.ellipse(screen, color, self.rect)

    def remove_if_out(self):

        if self.rect.x < -100 or self.rect.x > SCREEN_WIDTH + 100\
           or self.rect.y > SCREEN_HEIGHT + 100:
            FOOD_LIST.remove(self)



def create_new_aliment(pos=None, vitesse=None,
                       healthy=None, size=None):
    """
    Créé un nouvel aliment et l'ajoute à la liste des aliements.
    Si aucun argument n'est passé en paramètre, la fonction se charge
    de les créer de façon aléatoire.
    """
    if not pos:
        pos_x = random.choice([-100, SCREEN_WIDTH + 100])
        pos_y = random.randint(100, 600)
        pos = (pos_x, pos_y)

    if not vitesse:
        vitesse_y = random.randint(-3, 0)
        vitesse_x = (10 if pos[0] < 0 else -10)
        vitesse = (vitesse_x, vitesse_y)

    if not healthy:
        healthy = random.choice([True, False])

    if not size:
        size = random.randint(50, 100)

    aliment = Aliment(pos, vitesse, healthy, size)

    FOOD_LIST.add(aliment)

if __name__ == '__main__':
    pass

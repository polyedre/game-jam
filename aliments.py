#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame as pg
import random

from main import GAME_NAME, SCREEN_HEIGHT, SCREEN_WIDTH

food_list = pg.sprite.Group()

class Aliment(pg.sprite.Sprite):
    """
    Classe aliment d'un jeu. Chaque aliment est un objet qui se déplace suivant une vitesse.
    L'aliment peut être 'Healthy' ou non.
    """

    def __init__(self, _position, _vitesse, _healthy, _size):

        pg.sprite.Sprite.__init__(self)             # Superclass
        self.is_healthy = random.choice([True, False])
        self.vitesse = pg.math.Vector2(10,10)
        self.position = pg.math.Vector2(10,300)

        self.image = pg.Surface([50,50])
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()


    def update(self):
        "Met à jour les positions et vitesses de l'objet"
        self.rect.move_ip(*self.vitesse)


    def draw(self, screen):
        "Dessine l'aliment sur l'écran 'screen'"
        color = ((100, 255, 100) if self.is_healthy else (255, 100, 100))
        pg.draw.ellipse(screen, color, self.rect)


def create_new_aliment(pos=None, vitesse=None,
                       healthy=None, size=None):
    """
    Créé un nouvel aliment et l'ajoute à la liste des aliements.
    Si aucun argument n'est passé en paramètre, la fonction se charge
    de les créer de façon aléatoire.
    """
    if not pos:
        pos_y = random.randint(10, SCREEN_HEIGHT * 0.75)
        pos_x = random.choice([-100, SCREEN_WIDTH + 100])

    if not vitesse:
        vitesse_y = random.randint(-3, 3)
        vitesse_x = (10 if pos_x < 0 else -10)

    if not healthy:
        healthy = random.choice([True, False])

    if not size:
        size = random.randint(50, 100)

    aliment = Aliment((pos_x, pos_y), (vitesse_x, vitesse_y), healthy, size)

    food_list.add(aliment)

#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
import random
from vars import *


mouse_history = [(0, 0), (0, 0)]

class Aliment(pg.sprite.Sprite):
    """
    Classe aliment d'un jeu. Chaque aliment est un objet qui se déplace suivant une vitesse.
    L'aliment peut être 'Healthy' ou non.
    """

    def __init__(self, _position, _vitesse, _healthy, _size):

        pg.sprite.Sprite.__init__(self)             # Superclass

        self.is_healthy = _healthy
        img_name = ("./imgs/hamburger.png" if _healthy else "./imgs/salade.png")

        self.vitesse = pg.math.Vector2(_vitesse)
        self.acceleration = pg.math.Vector2(0, 0)

        self.rect = pg.Rect(*_position, _size, _size)
        self.image_visible = pg.transform.scale(pg.image.load(img_name), (50, 50))
        self.image_invisible = pg.Surface((50, 50)).convert_alpha()
        self.image_invisible.fill(pg.Color(100,100,100,0))
        self.image = self.image_visible

        self.grabbed = False

    def update(self):
        "Met à jour les positions et vitesses de l'objet"
        self.remove_if_out()

        if self.grabbed:
            self.rect.center = pg.mouse.get_pos()
        else:
            self.acceleration += GRAVITY
            self.vitesse += self.acceleration
            self.rect.move_ip(*self.vitesse)
            self.acceleration *= 0

    def remove_if_out(self):
        "Supprime l'aliment si il sort de l'écran."
        if self.rect.x < -100 or self.rect.x > SCREEN_WIDTH + 100\
           or self.rect.y > SCREEN_HEIGHT + 100:
            FOOD_LIST.remove(self)


def create_new_aliment(pos=None, vitesse=None,
                       healthy=None, size=None):
    """
    Créé un nouvel aliment et l'ajoute à la liste des aliments.
    Si aucun argument n'est passé en paramètre, la fonction se charge
    de les créer de façon aléatoire.
    """
    if not pos:
        pos_x = random.choice([-100, SCREEN_WIDTH + 100])
        pos_y = random.randint(50, SCREEN_HEIGHT / 2)
        pos = (pos_x, pos_y)

    if not vitesse:
        vitesse_y = random.randint(-12, -7)
        vitesse_x = (15 if pos[0] < 0 else -15)
        vitesse = (vitesse_x, vitesse_y)

    if not healthy:
        healthy = random.choice([True, False])

    if not size:
        size = random.randint(50, 100)

    aliment = Aliment(pos, vitesse, healthy, size)

    FOOD_LIST.add(aliment)


def updateMouseHistory():
    mouse_history[1] = mouse_history[0]
    mouse_history[0] = pg.mouse.get_pos()


def handleGrab():
    "Update food that are grabbed."
    mouse = pg.math.Vector2(pg.mouse.get_pos())
    for food in FOOD_LIST:
        center = pg.math.Vector2(food.rect.center)
        if (center - mouse).length() < GRAB_DISTANCE:
            food.grabbed = True
            food.vitesse *= 0
            food.image = food.image_invisible


def handleUngrab():
    for food in [f for f in FOOD_LIST if f.grabbed]:
        food.grabbed = False
        speed = pg.Vector2(mouse_history[0]) - pg.Vector2(mouse_history[1])
        food.vitesse = speed / MEM_MOUSE_EVENT_TIME * 30
        food.image = food.image_visible


if __name__ == '__main__':
    pass

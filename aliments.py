#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
import random
import sound
from gui import MouseHand
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
        img_name = ("./imgs/salade.png" if _healthy else "./imgs/hamburger.png")

        self.vitesse = pg.math.Vector2(_vitesse)
        self.acceleration = pg.math.Vector2(0, 0)

        x, y = _position
        self.rect = pg.Rect(x, y, _size, _size)
        self.radius = FOOD_RADIUS
        self.image_visible = pg.transform.scale(pg.image.load(img_name).convert_alpha(), (_size, _size))
        self.image_invisible = pg.Surface((_size, _size)).convert_alpha()
        self.image_invisible.fill(pg.Color(100,100,100,0))
        self.image = self.image_visible

        self.grabbed = False # by the user
        self.caught = False # by the computer
        self.master = None # Sprite to follow

        self.size = _size

    def update(self):
        "Met à jour les positions et vitesses de l'objet"
        self.remove_if_out()

        if self.grabbed:
            self.rect.center = pg.mouse.get_pos()
        elif self.caught:
            self.rect.center = self.master.rect.center
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

    def be_eaten(self):
        global SCORE
        if self.is_healthy:
            sound.salad_sound.play()
            SCORE[0] -= self.size // 2 #pour moduler la difficulte
            if SCORE[0] < 0: #pour ne pas avoir un score négatif
                SCORE[0] = 0
        else:
            sound.hamburger_sound.play()
            SCORE[0] += self.size
        if self.caught:
            self.caught = False
            self.master.target = None
            self.master.mode = HUNTING
            self.master = None
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

    return aliment


def updateMouseHistory():
    mouse_history[1] = mouse_history[0]
    mouse_history[0] = pg.mouse.get_pos()


def handleGrab():
    "Update food that is grabbed."
    # UNCOMMENT the following section for harder grabbing
    # ---------------------------------------------------
    mouse = pg.math.Vector2(pg.mouse.get_pos())
    for food in FOOD_LIST:
        center = pg.math.Vector2(food.rect.center)
        if not food.caught and (center - mouse).length() < GRAB_DISTANCE:
             food.grabbed = True
             food.vitesse *= 0
             food.image = food.image_invisible
    # UNCOMMENT the following section for easier grabbing
    # ---------------------------------------------------
    # for food in FOOD_LIST:
    #     for elem in GUI_LIST_FOREGROUND:
    #         if isinstance(elem, MouseHand) and elem.rect.colliderect(food.rect):
    #             food.grabbed = True
    #             food.vitesse *= 0
    #             food.image = food.image_invisible


def handleUngrab():
    for food in [f for f in FOOD_LIST if f.grabbed]:
        food.grabbed = False
        speed = pg.Vector2(mouse_history[0]) - pg.Vector2(mouse_history[1])
        food.vitesse = speed / MEM_MOUSE_EVENT_TIME * 30
        food.image = food.image_visible


if __name__ == '__main__':
    pass

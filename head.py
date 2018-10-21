import pygame as pg
from vars import *

class Head(pg.sprite.Sprite):

    def __init__(self, _position, _size, _radius):
        pg.sprite.Sprite.__init__(self)

        self.rect = pg.Rect(*_position, _size, _size)
        self.radius = _radius
        #        self.image = pg.transform.scale(pg.image.load("./imgs/circle.png"), (50, 50))
        self.image = pg.image.load("./imgs/body_slim_mouth_open.png")

    def update(self):
        list = pg.sprite.spritecollide(self, FOOD_LIST, False, pg.sprite.collide_circle)
        if list != []:
            for food in list:
                if food.grabbed or food.caught:
                    food.be_eaten()
                    self.eat()

    def eat(self):
        print("Miam !")

import pygame as pg
from vars import *

SLIM, MEDIUM, FAT = 1, 2, 3

class Head(pg.sprite.Sprite):

    def __init__(self, _position, _size, _radius):
        pg.sprite.Sprite.__init__(self)

        self.radius = _radius

        # Load image files
        self.images = list(list())
        for i in range(3):
            self.images.append([])
            for j in range(2):
                image = pg.image.load("./imgs/perso_{}_{}.png".format(i,j))
                self.images[i].append(pg.transform.scale(image, (SCREEN_HEIGHT // 2 , SCREEN_HEIGHT // 2)))

        self.image = self.images[0][0]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (SCREEN_WIDTH // 2, SCREEN_HEIGHT)

        self.mouth = 0
        self.obesity_level = 0

        self.counter = 0
        # Real position of the head of the character (not the body)
        self.head_pos = pg.Vector2(_position)
        self.head_rect = pg.rect.Rect(self.head_pos - (20, 20),(20, 20))
        self.head_sprite = pg.sprite.Sprite()
        self.head_sprite.rect = self.head_rect

    def update(self):
        global SCORE
        self.obesity_level = SCORE[0] // 250
        if self.obesity_level >= 2:
            self.obesity_level = 2
        list = pg.sprite.spritecollide(self.head_sprite, FOOD_LIST, False, None)
        for food in list:
            if food.grabbed or food.caught:
                food.be_eaten()
                self.mouth = 1
        self.image = self.images[self.obesity_level][self.mouth]
        if self.mouth == 1: # closed
            if self.counter <= MAX_TIME:
                self.counter += 1
            else:
                self.counter = 0
                self.mouth = 0

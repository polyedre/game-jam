import pygame as pg
from vars import *

SLIM, MEDIUM, FAT = 1, 2, 3

class Head(pg.sprite.Sprite):
    
    def __init__(self, _position, _size, _radius):
        pg.sprite.Sprite.__init__(self)

        self.rect = pg.Rect(*_position, _size, _size)
        self.radius = _radius

        # Load image files
        self.image_open = pg.transform.scale(pg.image.load("./imgs/body_slim_mouth_open.png"), (BODY_WIDTH, BODY_HEIGHT))
        self.image_closed = pg.transform.scale(pg.image.load("./imgs/body_slim_mouth_closed.png"), (BODY_WIDTH, BODY_HEIGHT))
        self.level = SLIM

        self.image = self.image_open
        self.rect.height = self.image.get_height()
        self.rect.width = self.image.get_width()


    def become_medium(self):
        self.image_open = pg.image.load("./imgs/body_medium_mouth_open.png")
        self.image_closed = pg.image.load("./imgs/body_medium_mouth_closed.png")
        self.level = MEDIUM

    def become_fat(self):
        self.image_open = pg.image.load("./imgs/body_fat_mouth_open.png")
        self.image_closed = pg.image.load("./imgs/body_fat_mouth_closed.png")
        self.level = FAT
        
    def update(self):
        list = pg.sprite.spritecollide(self, FOOD_LIST, False, pg.sprite.collide_circle)
        for food in list:
            if food.grabbed or food.caught:
                food.be_eaten()
                self.close_mouth()
        
        if self.image == self.image_closed:
            if self.closed_time <= MAX_TIME:
                self.closed_time += 1
            else:
                self.closed_time = 0
                self.open_mouth()
                    
    def open_mouth(self):
        self.image = self.image_open
        
    def close_mouth(self):
        print("CROUNCH")
        self.image = self.image_closed
        self.closed_time = 0



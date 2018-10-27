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
                # TODO: UNCOMMENT FOLLOWING LINE
                #image = pg.image.load("./imgs/perso_{}_{}.png".format(i,j))
                # TEMPORARY
                image = pg.image.load("./imgs/mouse_hand_open.png")
                self.images[i].append(pg.transform.scale(image, (SCREEN_WIDTH // 6 , SCREEN_HEIGHT // 2)))

        self.image = self.images[0][0]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (SCREEN_WIDTH // 2, SCREEN_HEIGHT)

        self.mouth = 0
        self.obesity_level = 0

        self.counter = 0
        # Real position of the head of the character (not the body)
        self.head_pos = pg.Vector2(_position)
        self.head_rect = pg.rect.Rect(self.head_pos - (20, 20), self.head_pos + (20, 20))

    def update(self):
        # list = pg.sprite.spritecollide(self, FOOD_LIST, False, pg.sprite.collide_circle)
        # for food in FOOD_LIST:
        #     if (self.head_pos.distance_to(pg.Vector2(food.rect.center)) < self.radius):
        #         food.be_eaten()
        #         self.mouth = 1
        
        self.image = self.images[self.obesity_level][self.mouth]
        if self.mouth == 1: # closed
            if self.counter <= MAX_TIME:
                self.counter += 1
            else:
                self.counter = 0
                self.mouth = 0

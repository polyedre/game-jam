import pygame as pg
from math import hypot

HUNTING, FOLLOWING, EATING = 1, 2, 3

class Hand(pg.sprite.Sprite):

    def __init__(self, _position, _area, _velocity):
        pg.sprite.Sprite.__init__(self)

        self.position = _position
        self.area = _area
        self.velocity = _velocity
        self.image = pg.transform.scale(pg.image.load("./imgs/circle.png"), (50, 50))
        self.rect = pg.Rect(*_position, 50, 50)
        self.mode = HUNTING
        self.target = None

    def move_towards_target(self):
        dx = self.target.rect.x - self.rect.x
        dy = self.target.rect.y - self.rect.y
        dist = hypot(dx, dy)
        if dist == 0:
            coeff = 0
        else:
            coeff = self.velocity / dist
        dx *= coeff
        dy *= coeff
        print("dx", dx, "dy", dy)
        self.rect.move_ip(dx, dy) 

    def update(self):
        if self.mode == FOLLOWING:
            self.move_towards_target()
            pass
        elif self.mode == EATING:
            pass
        else:
            pass


import pygame as pg

class Head(pg.sprite.Sprite):

    def __init__(self, _position, _size, _radius):
        pg.sprite.Sprite.__init__(self)

        self.rect = pg.Rect(*_position, _size, _size)
        self.radius = _radius

        self.image = pg.transform.scale(pg.image.load("./imgs/circle.png"), (_size, _size))

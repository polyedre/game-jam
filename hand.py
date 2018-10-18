import pygame as pg

class Hand(pg.sprite.Sprite):

    def __init__(self, _position, _area):
        pg.sprite.Sprite.__init__(self)

        self.position = _position
        self.area = _area
        self.image = pg.transform.scale(pg.image.load("./imgs/circle.png"), (50, 50))
        self.rect = pg.Rect(*_position, 50, 50)

    def update(self):
        pass

    def draw(self):
        pg.sprite.Sprite.draw()


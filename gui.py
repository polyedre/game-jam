import pygame as pg
from vars import *

class LoadingBar(pg.sprite.Sprite):

    def __init__(self, percentage, color, rect, offset_left=0, offset_right=0):

        pg.sprite.Sprite.__init__(self)             # Superclass

        self.offset_right = offset_right
        self.offset_left = offset_left

        self.exterieur = pg.image.load("./imgs/load_ext.png").convert_alpha()
        self.interieur = pg.image.load("./imgs/load_int.png").convert_alpha()
        self.percentage = percentage
        self.color = color
        self.rect = pg.Rect(rect)


    def draw(self, screen):

        screen.blit(self.exterieur, self.rect)
        largeur = (self.exterieur.get_rect().width - (self.offset_right + self.offset_left)) * self.percentage
        screen.blit(self.interieur, self.rect.move(self.offset_left, 0), area=[0,0,largeur,12] )


    def update(self):

        if self.percentage < 0.99:
            self.percentage += 0.01


class MouseHand(pg.sprite.Sprite):

    def __init__(self, _rect, img_open, img_close):

        pg.sprite.Sprite.__init__(self)             # Superclass

        self.rect = pg.Rect(_rect)
        self.img_hand_open = pg.image.load(img_open).convert_alpha()
        self.img_hand_open = pg.transform.scale(self.img_hand_open, (self.rect.width, self.rect.height))

        self.img_hand_close = pg.image.load(img_close).convert_alpha()
        self.img_hand_close = pg.transform.scale(self.img_hand_close, (self.rect.width, self.rect.height))

        self.mouse_open = True


    def draw(self, screen):

        if self.mouse_open:
            screen.blit(self.img_hand_open, self.rect)
        else:
            screen.blit(self.img_hand_close, self.rect)


    def update(self):
        self.rect.center = pg.mouse.get_pos()


class Background(pg.sprite.Sprite):

    def __init__(self, file_name):
        pg.sprite.Sprite.__init__(self)             # Superclass

        self.offset = 0
        self.image = pg.image.load(file_name)

        self.interval = 3 * SCREEN_WIDTH / (60 * FRAMERATE)


    def update(self):
        self.offset += self.interval


    def draw(self, screen):
        screen.blit(self.image, [0,0, SCREEN_WIDTH, SCREEN_HEIGHT], area=[self.offset, 0, SCREEN_WIDTH, SCREEN_HEIGHT])


def init():
    """
    Créé les éléments GUI du jeu :
     - Une barre de vie
     - Une barre d'appétence
     - La souris
    """
    health = LoadingBar(0.1, (255,0,0), [10, 10, 400, 20])
    GUI_LIST_FOREGROUND.add(health)

    health_deux = LoadingBar(0.5, (100,40,60), [10, 40, 400, 20])
    GUI_LIST_FOREGROUND.add(health_deux)

    souris = MouseHand([0,0,40,40], "./imgs/mouse_open.png", "./imgs/mouse_close.png")
    GUI_LIST_FOREGROUND.add(souris)

    background = Background("./imgs/background.png")
    GUI_LIST_BACKGROUND.add(background)


def handleGrab():
    for elem in GUI_LIST_FOREGROUND:
        if isinstance(elem, MouseHand):
            elem.mouse_open = False


def handleUngrab():
    for elem in GUI_LIST_FOREGROUND:
        if isinstance(elem, MouseHand):
            elem.mouse_open = True

if __name__ == '__main__':
    pass

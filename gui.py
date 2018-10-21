import pygame as pg
from vars import *

class LoadingBar(pg.sprite.Sprite):

    def __init__(self, rect, int_img, ext_img, offset_left=0,offset_right=0):

        pg.sprite.Sprite.__init__(self)             # Superclass

        self.offset_right = offset_right
        self.offset_left = offset_left
        self.exterieur = pg.image.load(ext_img).convert_alpha()
        self.rect = self.exterieur.get_rect()
        self.rect.move_ip(*rect[:2])
        self.interieur = pg.image.load(int_img).convert_alpha()
        self.image = pg.surface.Surface((self.rect.width, self.rect.height))
        self.percentage = 0

    def update(self):
        self.percentage = SCORE // 1000
        self.image.blit(self.exterieur, self.rect)
        largeur = (self.exterieur.get_rect().width - (self.offset_right + self.offset_left)) * self.percentage
        self.image.blit(self.interieur, self.rect.move(self.offset_left, 0), area=[0,0, largeur, 12])


class MouseHand(pg.sprite.Sprite):

    def __init__(self, _rect, img_open, img_close):

        pg.sprite.Sprite.__init__(self)             # Superclass

        self.rect = pg.Rect(_rect)
        self.img_hand_open = pg.image.load(img_open).convert_alpha()
        self.img_hand_open = pg.transform.scale(self.img_hand_open, (self.rect.width, self.rect.height))

        self.img_hand_close = pg.image.load(img_close).convert_alpha()
        self.img_hand_close = pg.transform.scale(self.img_hand_close, (self.rect.width, self.rect.height))

        self.mouse_open = True

    def update(self):
        self.rect.center = pg.mouse.get_pos()

        if self.mouse_open:
            self.image = self.img_hand_open
        else:
            self.image = self.img_hand_close


class Background(pg.sprite.Sprite):

    def __init__(self, file_name):
        pg.sprite.Sprite.__init__(self)             # Superclass

        self.offset = 0
        self.image = pg.image.load(file_name).convert()
        self.image = pg.transform.scale(self.image, (SCREEN_WIDTH * 3, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.interval = 3 * SCREEN_WIDTH / (SCROLL_TIME * FRAMERATE)


    def update(self):
        self.offset += self.interval
        self.rect.topleft = (-self.offset, 0)
        SCROLL_AVANCEMENT =  self.offset / (3 * SCREEN_WIDTH)


def init():
    """
    Crée les éléments GUI du jeu :
     - Une barre de vie
     - Une barre d'appétence
     - La souris
    """
    LoadingBar([SCREEN_WIDTH // 10, SCREEN_HEIGHT // 10,
                8 * SCREEN_WIDTH // 10, SCREEN_HEIGHT // 10],
               "./imgs/load_int.png", "./imgs/load_ext.png").add(GUI_LIST_FOREGROUND)

    MouseHand([0, 0, 120, 120],
              "./imgs/mouse_open.png", "./imgs/mouse_close.png").add(GUI_LIST_FOREGROUND)

    Background("./imgs/background.png").add(GUI_LIST_BACKGROUND)

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

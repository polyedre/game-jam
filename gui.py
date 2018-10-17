import pygame as pg

GUI_LIST = pg.sprite.Group()

class LoadingBar(pg.sprite.Sprite):

    def __init__(self, percentage, color, rect):

        pg.sprite.Sprite.__init__(self)             # Superclass

        self.exterieur = pg.image.load("./imgs/load_ext.png").convert_alpha()
        self.interieur = pg.image.load("./imgs/load_int.png").convert_alpha()
        self.percentage = percentage
        self.color = color
        self.rect = pg.Rect(rect)

    def draw(self, screen):

        screen.blit(self.exterieur, self.rect)
        largeur = (self.exterieur.get_rect().width - 4) * self.percentage
        screen.blit(self.interieur, self.rect, area=[0,0,largeur,12] )

        # (r, v, b) = self.color
        # background_color = (0,0,0)
        # largeur = 5 # Nombre de pixels de largeur des mini-barres
        # pg.draw.rect(screen, background_color, self.rect)
        # nombre_minibars = int(self.rect.width * self.percentage // (largeur + 1))
        # for i in range(nombre_minibars):
        #     pg.draw.rect(screen, self.color, [self.rect.x + i * (largeur + 1), self.rect.y,
        #                                       largeur, self.rect.height])


def init():


    health = LoadingBar(0.1, (255,0,0), [10, 10, 400, 20])
    GUI_LIST.add(health)

    health_deux = LoadingBar(0.5, (100,40,60), [10, 40, 400, 20])
    GUI_LIST.add(health_deux)
if __name__ == '__main__':
    pass

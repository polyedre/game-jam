import pygame as pg

GAME_NAME = "test"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

## SETUP ##
pg.init()
SCREEN = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pg.display.set_caption(GAME_NAME)

RUNNING = True

while RUNNING:

    SCREEN.fill((255, 255, 255))

    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit()

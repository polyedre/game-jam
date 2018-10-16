import pygame as pg
import time

GAME_NAME = "Eat and never run"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pg.init()

sc = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pg.display.set_caption(GAME_NAME)

RUNNING = True

while RUNNING:

    sc.fill((255, 255, 255))

    # Update and draw aliments

    # Update and draw bras

    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit()

import pygame as pg
import aliments as al
import gui
from vars import *

pg.init()

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

gui.init()

def main():

    CLOCK = pg.time.Clock()

    # Ajout des aliments
    pg.time.set_timer(pg.USEREVENT, 1000)
    pg.time.set_timer(MEM_MOUSE_EVENT, MEM_MOUSE_EVENT_TIME)

    running = True

    while running:

        screen.fill((255, 255, 255))

        for element in GUI_LIST_BACKGROUND:
            element.update()
            element.draw(screen)

        al.FOOD_LIST.draw(screen)
        al.FOOD_LIST.update()
        al.updateMouseHistory()

        # GUI

        for element in GUI_LIST_FOREGROUND:
            element.update()
            element.draw(screen)

        # Update and draw bras

        pg.display.flip()
        CLOCK.tick(FRAMERATE)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.USEREVENT:
                al.create_new_aliment()

            if event.type == pg.MOUSEBUTTONDOWN:
                al.handleGrab()
                gui.handleGrab()

            if event.type == pg.MOUSEBUTTONUP:
                al.handleUngrab()
                gui.handleUngrab()

            if event.type == MEM_MOUSE_EVENT:
                al.updateMouseHistory()

    pg.quit()

if __name__ == '__main__':
    main()

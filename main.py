import pygame as pg
import aliments as al
import gui
import level
from vars import *


def main():

    pg.init()
    pg.font.init()

    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    gui.init()
    pages = level.init()

    pages['accueil'].run()

def play():

    pg.time.set_timer(pg.USEREVENT, 1000)
    pg.time.set_timer(MEM_MOUSE_EVENT, MEM_MOUSE_EVENT_TIME)

    while RUNNING:
        run()

def run():
    screen.fill((255, 255, 255))

    handleBackground()
    handleForeground()
    handleKeys(pg.event.get())

    pg.display.flip()
    CLOCK.tick(FRAMERATE)

def handleKeys(event_list):
    for event in event_list:
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)

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

def handleForeground():
    # Food
    al.FOOD_LIST.draw(screen)
    al.FOOD_LIST.update()
    al.updateMouseHistory()

    # GUI
    for element in GUI_LIST_FOREGROUND:
        element.update()
        element.draw(screen)


def handleBackground():
    for element in GUI_LIST_BACKGROUND:
        element.update()
        element.draw(screen)

if __name__ == '__main__':
    main()

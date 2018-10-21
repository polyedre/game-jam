import pygame as pg
import aliments as al
import gui
from vars import *

pg.init()

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

gui.init()

def main():

    # Ajout des aliments
    pg.time.set_timer(pg.USEREVENT, 1000)
    pg.time.set_timer(MEM_MOUSE_EVENT, MEM_MOUSE_EVENT_TIME)

    while RUNNING:
        run()

def run():
    screen.fill((255, 255, 255))

    handleBackground()
    handleForeground()
    handleKeys()

    pg.display.flip()
    CLOCK.tick(FRAMERATE)

def handleKeys():
    for event in pg.event.get():
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

        if event.type == FINISHED_RUN:
            finished_run_animation()


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
    ""
    for element in GUI_LIST_BACKGROUND:
        element.update()
        element.draw(screen)

def finished_run_animation():
    print("Vous avez gagné ou perdu on sait par encore")
    print("On est sensé passé au niveau suivant")
if __name__ == '__main__':
    main()

import pygame as pg
import aliments as al
import hand as ha
import head as he
import gui
import level
from vars import *


def main():

    pg.init()
    pg.font.init()

def main():

    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    gui.init()
    pages = level.init(screen)

    pages['accueil'].run()

def play(screen):

    head = he.Head((300, 100), HEAD_SIZE, HEAD_RADIUS)
    BODY_PARTS_LIST.add(head)
    left_hand = ha.Hand((200,200), 0, HAND_SPEED, HAND_SIZE, head, True)
    BODY_PARTS_LIST.add(left_hand)
    right_hand = ha.Hand((400,200), 0, HAND_SPEED, HAND_SIZE, head, False)
    BODY_PARTS_LIST.add(right_hand)
    pg.time.set_timer(pg.USEREVENT, 1000)
    pg.time.set_timer(MEM_MOUSE_EVENT, MEM_MOUSE_EVENT_TIME)

    while RUNNING:
        run(screen)


def run(screen):
    screen.fill((255, 255, 255))

    handleBackground(screen)
    handleForeground(screen)
    handleKeys(pg.event.get())

    # Update and draw bras
    BODY_PARTS_LIST.draw(screen)
    BODY_PARTS_LIST.update()

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

        if event.type == FINISHED_RUN:
            finished_run_animation()

def handleForeground(screen):
    # Food
    al.FOOD_LIST.draw(screen)
    al.FOOD_LIST.update()
    al.updateMouseHistory()

    # GUI
    for element in GUI_LIST_FOREGROUND:
        element.update()
        element.draw(screen)


def handleBackground(screen):
    ""
    for element in GUI_LIST_BACKGROUND:
        element.update()
        element.draw(screen)

def finished_run_animation():
    print("Vous avez gagné ou perdu on sait par encore")
    print("On est sensé passé au niveau suivant")

if __name__ == '__main__':
    main()

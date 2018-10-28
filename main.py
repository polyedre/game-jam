# -*- coding: utf-8 -*-
import pygame as pg

pg.init()
pg.font.init()

import aliments as al
import hand as ha
import head as he
import gui
import level
from vars import *

def play(screen):

    pages['accueil'].running = False
    gui.init()

    head = he.Head((488, 320), HEAD_SIZE, HEAD_RADIUS)
    head.add(BODY_PARTS_LIST)
    ha.Hand((SCREEN_WIDTH // 4, 3 * SCREEN_HEIGHT // 4), 0, HAND_SPEED, HAND_SIZE, head, True).add(BODY_PARTS_LIST)
    ha.Hand((400,200), 0, HAND_SPEED, HAND_SIZE, head, False).add(BODY_PARTS_LIST)

    pg.time.set_timer(pg.USEREVENT, 1000)
    pg.time.set_timer(MEM_MOUSE_EVENT, MEM_MOUSE_EVENT_TIME)

    while RUNNING:
        run(screen)


def run(screen):
    screen.fill((255, 255, 255))

    handleBackground(screen)
    handleForeground(screen)
    handleKeys(pg.event.get())

    pg.display.flip()
    CLOCK.tick(FRAMERATE)

def handleKeys(event_list):
    for event in event_list:
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)

        if event.type == pg.USEREVENT:
            al.create_new_aliment(FOOD_LIST)

        if event.type == pg.MOUSEBUTTONDOWN:
            al.handleGrab()
            gui.handleGrab()
            print(pg.mouse.get_pos())

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

    # Update and draw bras
    BODY_PARTS_LIST.update()
    BODY_PARTS_LIST.draw(screen)

    # GUI
    GUI_LIST_FOREGROUND.update()
    GUI_LIST_FOREGROUND.draw(screen)


def handleBackground(screen):
    ""
    GUI_LIST_BACKGROUND.update()
    GUI_LIST_BACKGROUND.draw(screen)

def finished_run_animation():
    print("Vous avez gagné ou perdu on sait par encore")
    print("On est sensé passer au niveau suivant")

if __name__ == '__main__':
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    pages = level.init(screen)
    level.Button([SCREEN_WIDTH // 4,
            SCREEN_HEIGHT // 2,
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 8 - 10], play, [screen],
           text="Jouer").add(pages["accueil"].sprite_list)
    pages['accueil'].run()

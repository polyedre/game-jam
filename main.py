# -*- coding: utf-8 -*-
import pygame as pg

pg.init()
pg.font.init()
pg.mixer.init()

import aliments as al
import hand as ha
import head as he
import gui
import level
from vars import *

def run(screen):
    screen.fill((255, 255, 255))

    handleBackground(screen)
    handleForeground(screen)
    handleKeys(pg.event.get())

    pg.display.flip()

def handleKeys(event_list):
    for event in event_list:
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)

        if event.type == pg.USEREVENT:
            FOOD_LIST.add(al.create_new_aliment())

        if event.type == pg.MOUSEBUTTONDOWN:
            al.handleGrab()
            gui.handleGrab()

        if event.type == pg.MOUSEBUTTONUP:
            al.handleUngrab()
            gui.handleUngrab()

        if event.type == MEM_MOUSE_EVENT:
            al.updateMouseHistory()

        if event.type == FINISHED_RUN:
            finished_run_animation(screen)

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

def finished_run_animation(screen):
    global SCORE
    mem = SCORE[0]

    load_game()

    if mem > 750:
        level.switch_page(pages["play"], pages["victoire"])
    else:
        level.switch_page(pages["play"], pages["defeat"])


def load_game():

    # LISTS
    # global GUI_LIST_BACKGROUND
    # global GUI_LIST_FOREGROUND
    # global FOOD_LIST
    # global BODY_PARTS_LIST

    GUI_LIST_FOREGROUND.empty()
    GUI_LIST_BACKGROUND.empty()
    FOOD_LIST.empty()
    BODY_PARTS_LIST.empty()

    gui.init()

    global SCROLL_AVANCEMENT
    SCROLL_AVANCEMENT = 0

    global SCORE
    SCORE[0] = 0

    head = he.Head((488, 320), HEAD_SIZE, HEAD_RADIUS)
    head.add(BODY_PARTS_LIST)
    ha.Hand((SCREEN_WIDTH // 4, 3 * SCREEN_HEIGHT // 4), 0, HAND_SPEED, HAND_SIZE, head, True).add(BODY_PARTS_LIST)
    ha.Hand((400,200), 0, HAND_SPEED, HAND_SIZE, head, False).add(BODY_PARTS_LIST)
    pg.time.set_timer(pg.USEREVENT, 1000)
    pg.time.set_timer(MEM_MOUSE_EVENT, MEM_MOUSE_EVENT_TIME)

if __name__ == '__main__':
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    pages = level.init(screen)

    pages['play'].hooked_function = run
    pages['play'].hooked_args = [screen]

    load_game()

    pages["accueil"].music.play()
    pages['accueil'].run()

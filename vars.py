import pygame as pg

# WINDOW

GAME_NAME = "Eat and never run"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAMERATE = 30


# LISTS

GUI_LIST_FOREGROUND = pg.sprite.Group()
GUI_LIST_BACKGROUND = pg.sprite.Group()
FOOD_LIST = pg.sprite.Group()


# EVENTS

MEM_MOUSE_EVENT = pg.USEREVENT + 1
MEM_MOUSE_EVENT_TIME = 100


# DYNAMIC
GRAVITY = pg.math.Vector2(0, 0.3)
GRAB_DISTANCE = 50

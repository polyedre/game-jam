import pygame as pg

# WINDOW

GAME_NAME = "Eat and never run"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAMERATE = 20


# LISTS

GUI_LIST_FOREGROUND = pg.sprite.Group()
GUI_LIST_BACKGROUND = pg.sprite.Group()
FOOD_LIST = pg.sprite.Group()
BODY_PARTS_LIST = pg.sprite.Group()

# EVENTS

MEM_MOUSE_EVENT = pg.USEREVENT + 1
MEM_MOUSE_EVENT_TIME = 100


# DYNAMIC
GRAVITY = pg.math.Vector2(0, 0.3)
GRAB_DISTANCE = 100
HAND_SPEED = 10

# GEOMETRICAL
HEAD_SIZE = 60
HEAD_RADIUS = 10
HAND_SIZE = 30
HAND_RADIUS = 10
#ARM_LENGTH = 80
FOOD_SIZE = 50
FOOD_RADIUS = 10

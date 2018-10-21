import pygame as pg

# WINDOW

GAME_NAME = "Eat and never run"
SCREEN_WIDTH = 1920 // 2
SCREEN_HEIGHT = 1080 // 2
FRAMERATE = 60
RUNNING = True


# LISTS

GUI_LIST_FOREGROUND = pg.sprite.Group()
GUI_LIST_BACKGROUND = pg.sprite.Group()
FOOD_LIST = pg.sprite.Group()


# EVENTS

MEM_MOUSE_EVENT = pg.USEREVENT + 1
MEM_MOUSE_EVENT_TIME = 100
FINISHED_RUN = pg.USEREVENT + 2
CLOCK = pg.time.Clock()


# DYNAMIC

GRAVITY = pg.math.Vector2(0, 0.3)
GRAB_DISTANCE = 50
SCROLL_TIME = 60 # seconds
SCROLL_AVANCEMENT = 0

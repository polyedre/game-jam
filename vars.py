import pygame as pg

# WINDOW
GAME_NAME = "Eat and never run"
SCREEN_WIDTH = 1920 // 2
SCREEN_HEIGHT = 1080 // 2
FRAMERATE = 30
RUNNING = True
FONT = pg.font.Font(None, 40)

# LISTS
GUI_LIST_FOREGROUND = pg.sprite.Group()
GUI_LIST_BACKGROUND = pg.sprite.Group()
FOOD_LIST = pg.sprite.Group()
BODY_PARTS_LIST = pg.sprite.Group()

# EVENTS
MEM_MOUSE_EVENT = pg.USEREVENT + 1
MEM_MOUSE_EVENT_TIME = 100
FINISHED_RUN = pg.USEREVENT + 2
CLOCK = pg.time.Clock()

# DYNAMIC
GRAVITY = pg.math.Vector2(0, 0.3)
GRAB_DISTANCE = 50
SCROLL_TIME = 120 # seconds
SCROLL_AVANCEMENT = 0
HAND_SPEED = 10
SCORE = [0]
MAX_TIME = FRAMERATE * 1

HUNTING, FOLLOWING, EATING = 1, 2, 3

# GEOMETRICAL
HEAD_SIZE = 60
HEAD_RADIUS = 10
HAND_SIZE = SCREEN_HEIGHT//8
HAND_RADIUS = HAND_SIZE
#ARM_LENGTH = 80
FOOD_SIZE = 50
FOOD_RADIUS = 10

BODY_WIDTH = 175
BODY_HEIGHT = 500

# SOUNDS

# EAT_SOUND = pg.mixer.Sound("./sounds/eat.wav")
# INTRO_SOUND = pg.mixer.Sound("./sounds/intro.mp3")
# RUN_SOUND = pg.mixer.Sound("./sounds/run.wav")

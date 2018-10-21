import pygame as pg
from math import hypot, sqrt
from vars import *

HUNTING, FOLLOWING, EATING = 1, 2, 3

class Hand(pg.sprite.Sprite):

    def __init__(self, _position, _area, _velocity, _head):
        pg.sprite.Sprite.__init__(self)

        self.area = _area
        self.velocity = _velocity
        self.rect = pg.Rect(*_position, 50, 50)
        self.radius = 25
        
        self.image = pg.transform.scale(pg.image.load("./imgs/circle.png"), (50, 50))

        self.head = _head
        self.mode = HUNTING
        self.target = None

    def distance(self, sprite):
        return sqrt(sprite.rect.x**2 + sprite.rect.y**2) 
        
    def choose_target(self):
        """
        Finds closest healthy food and sets it as target
        """
        min_food = None
        min_dist = None
        for food in FOOD_LIST:
            if food.is_healthy:
                new_dist = self.distance(food)
                if min_dist == None or new_dist < min_dist:
                    min_dist = new_dist
                    min_food = food
        self.target = min_food
        
    def move_towards(self, sprite):
        """
        Move towards self.target using self.velocity
        """
        dx = sprite.rect.x - self.rect.x
        dy = sprite.rect.y - self.rect.y
        dist = hypot(dx, dy)
        if dist == 0:
            coeff = 0
        else:
            coeff = self.velocity / dist
        dx *= coeff
        dy *= coeff
        self.rect.move_ip(dx, dy) 

    def update(self):
        if self.mode == FOLLOWING:
            if self.target.alive(): # condition to keep following this target
                # TODO: stop following if target gets out of hunting area
                if pg.sprite.collide_circle(self, self.target):
                    FOOD_LIST.remove(self.target) #TODO : replace by eating
                else:
                    self.move_towards(self.target)
            else:
                self.mode = HUNTING
        elif self.mode == EATING:
            self.move_towards(self.head)
        else:
            self.choose_target()
            if self.target != None:
                self.mode = FOLLOWING


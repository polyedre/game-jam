import pygame as pg
from math import hypot, sqrt
from vars import *

HUNTING, FOLLOWING, EATING = 1, 2, 3

class Hand(pg.sprite.Sprite):

    def __init__(self, _position, _zone, _velocity, _size, _head, _is_left):
        pg.sprite.Sprite.__init__(self)

        self.zone = _zone
        self.velocity = _velocity
        self.rect = pg.Rect(*_position, _size, _size)
        self.radius = HAND_RADIUS
        
        self.image = pg.transform.scale(pg.image.load("./imgs/circle.png"), (50, 50))

        self.head = _head
        self.is_left = _is_left
        self.mode = HUNTING
        self.target = None
        self.set_boundaries()

    def distance(self, sprite):
        return sqrt(sprite.rect.centerx**2 + sprite.rect.centery**2) 
        
    def choose_target(self):
        """
        Finds closest healthy food and sets it as target
        """
        min_food = None
        min_dist = None
        for food in FOOD_LIST:
            if food.is_healthy and not food.grabbed and not food.caught:
                new_dist = self.distance(food)
                if min_dist == None or new_dist < min_dist:
                    min_dist = new_dist
                    min_food = food
        self.target = min_food

    def set_boundaries(self):
        self.top_boundary = self.head.rect.centery - 100
        self.bottom_boundary = self.head.rect.centery + 100
        if self.is_left:
            self.right_boundary = self.head.rect.centerx
            self.left_boundary = self.right_boundary - 100
        else:
            self.left_boundary = self.head.rect.centerx
            self.right_boundary = self.left_boundary + 100
        
    def move_by(self, dx, dy):
        new_x = self.rect.centerx + dx
        new_y = self.rect.centery + dy
        new_dx = dx
        new_dy = dy
        # Correct if wants to go too far
        if new_x < self.left_boundary:
            new_dx = self.left_boundary - self.rect.centerx
        if new_x > self.right_boundary:
            new_dx = self.right_boundary - self.rect.centerx
        if new_y > self.bottom_boundary:
            new_dy = self.bottom_boundary - self.rect.centery
        if new_y < self.top_boundary:
            new_dy = self.top_boundary - self.rect.centery
        # Apply movement
        self.rect.move_ip(new_dx, new_dy)

    def move_towards(self, sprite):
        """
        Move towards sprite using self.velocity
        """
        dx = sprite.rect.centerx - self.rect.centerx
        dy = sprite.rect.centery - self.rect.centery
        dist = hypot(dx, dy)
        if dist == 0:
            coeff = 0
        else:
            coeff = self.velocity / dist
        dx *= coeff
        dy *= coeff
        self.move_by(dx, dy)

    def default_position(self):
        if self.is_left:
            def_x = self.head.rect.centerx - 50
        else:
            def_x = self.head.rect.centerx + 50
        def_y = self.head.rect.centery + 150
        ret = pg.sprite.Sprite()
        ret.rect = pg.rect.Rect(def_x, def_y, 1, 1)
        return ret            

    def update(self):
        if self.mode == FOLLOWING:
            if self.target.alive() and self.distance(target) < APPETITE: # condition to keep following this target
                if pg.sprite.collide_circle(self, self.target):
                    self.target.caught = True
                    self.target.master = self
                    self.mode = EATING
                else:
                    self.move_towards(self.target)
            else:
                self.mode = HUNTING
        elif self.mode == EATING:
            if pg.sprite.collide_circle(self, self.head):
                FOOD_LIST.remove(self.target)
                self.target = None
                self.mode = HUNTING
            else:
                self.move_towards(self.head)
        else:
            self.choose_target()
            if self.target == None:
                self.move_towards(self.default_position())
            else:
                self.mode = FOLLOWING


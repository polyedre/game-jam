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
        self.is_left = _is_left

        if self.is_left:
            self.path_open = "./imgs/left_hand_open.png"
            self.path_closed = "./imgs/left_hand_closed.png"
            self.side_rect = pg.Rect(10, 10, SCREEN_WIDTH // 2 - 10, SCREEN_HEIGHT - 10)
        else:
            self.path_open = "./imgs/right_hand_open.png"
            self.path_closed = "./imgs/right_hand_closed.png"
            self.side_rect = pg.Rect(SCREEN_WIDTH // 2 + 10, 10, SCREEN_WIDTH - 10, SCREEN_HEIGHT - 10)

        self.image_open = pg.transform.scale(pg.image.load(self.path_open), (_size, _size))
        self.image_closed = pg.transform.scale(pg.image.load(self.path_closed), (_size, _size))
        self.image = self.image_open

        self.head = _head
        self.mode = HUNTING
        self.target = None

    def default_position(self):
        if self.is_left:
            def_x = self.head.rect.centerx - SCREEN_WIDTH//8
        else:
            def_x = self.head.rect.centerx + SCREEN_WIDTH//8
        def_y = self.head.rect.centery + 10
        return pg.Vector2(def_x, def_y)

    def min_couple(self, couple_list):
        min_dist = 0
        min_food = None
        for couple in couple_list:
            if min_dist == 0 or couple[0] < min_dist:
                min_dist = couple[0]
                min_food = couple[1]
        return (min_dist, min_food)

    def choose_target(self):
        """
        Finds closest healthy food and sets it as target
        """
        couple_lists = [ (pg.Vector2(food.rect.center).distance_squared_to(self.head.rect.center), food) for food in FOOD_LIST]

        sided_couple_list = [(dist, food) for dist, food in couple_lists if self.side_rect.colliderect(food.rect)]

        if sided_couple_list:
            #self.target = min(sided_couple_list)[1] ne fonctionnait pas
            self.target = self.min_couple(sided_couple_list)[1]
            self.mode = FOLLOWING
        else:
            self.target = None

    # def move_by(self, dx, dy):
    #     new_x = self.rect.centerx + dx
    #     new_y = self.rect.centery + dy
    #     new_dx = dx
    #     new_dy = dy
    #     # Correct if wants to go too far
    #     if new_x < self.left_boundary:
    #         new_dx = self.left_boundary - self.rect.centerx
    #     if new_x > self.right_boundary:
    #         new_dx = self.right_boundary - self.rect.centerx
    #     if new_y > self.bottom_boundary:
    #         new_dy = self.bottom_boundary - self.rect.centery
    #     if new_y < self.top_boundary:
    #         new_dy = self.top_boundary - self.rect.centery
    #     # Apply movement
    #     self.rect.move_ip(new_dx, new_dy)

    # def move_towards(self, sprite):
    #     """
    #     Move towards sprite using self.velocity
    #     """
    #     dx = sprite.rect.centerx - self.rect.centerx
    #     dy = sprite.rect.centery - self.rect.centery
    #     dist = hypot(dx, dy)
    #     if dist == 0:
    #         coeff = 0
    #     else:
    #         coeff = self.velocity / dist
    #     dx *= coeff
    #     dy *= coeff
    #     self.move_by(dx, dy)

    def update(self):
        if self.mode == HUNTING:
            """
            This mode is when Hand has no target
            But is looking for one
            If none is in its hunting zone, it will move to its default position
            """
            self.choose_target()
            if self.target == None:
                direction = self.default_position() - pg.Vector2(self.rect.center)
                if direction.length() > 0:
                    self.rect.move_ip(direction.normalize() * self.velocity)
            else:
                self.mode = FOLLOWING
        elif self.mode == FOLLOWING:
            """
            This mode is when Hand has a Sprite of type Aliment
            as target.
            It keeps following it until:
                * Hand catches target
                * Target gets too far
            """
            if self.target.alive() \
               and self.side_rect.colliderect(self.target.rect):
                if self.rect.colliderect(self.target.rect):
                    self.target.caught = True
                    self.target.master = self
                    self.mode = EATING
                else:
                    direction = pg.Vector2(self.target.rect.center) - pg.Vector2(self.rect.center)
                    if (direction.length() > 0):
                        self.rect.move_ip(direction.normalize() * self.velocity)
            else:
                self.mode = HUNTING
                self.target = None
        elif self.mode == EATING:
            """
            This if for when the target is caught
            The target is set to follow Hand
            and Hand moves to Head
            When Hand and Head collide, the food can be eaten
            and Hand goes back to hunting
            """
            if self.rect.colliderect(self.head.head_rect):
                self.target.caught = False
                self.target.master = None
                self.target.be_eaten()
                self.head.mouth = 1
                self.target = None
                self.mode = HUNTING
            else:
                direction = self.head.head_pos - pg.Vector2(self.rect.center)
                if direction.length != 0:
                    self.rect.move_ip(direction.normalize() * self.velocity)
        else:
            """
            This should never happen
            """
            print("Error: what the heck is this mode ?")
            self.mode = HUNTING

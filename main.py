import pygame
import time

GAME_NAME = "test"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

sc = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(GAME_NAME)

sprite_list = pygame.sprite.Group()

sc.fill((255,255,255))

pygame.draw.rect(sc, (100, 100, 255), [350, 450, 100, 200])
pygame.draw.circle(sc, (100, 100, 255), [400, 500], 100)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse = pygame.math.Vector2(pygame.mouse.get_pos())

    center_player = pygame.math.Vector2(400,500)

    dir_arm = (mouse - center_player).normalize() * 100

    pygame.draw.line(sc, (0, 0, 0), (400,500), (center_player + dir_arm))

    pygame.display.flip()

    time.sleep(0.1)

pygame.quit()

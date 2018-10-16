import pygame as pg
import aliments as al

GAME_NAME = "Eat and never run"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

GRAB_DISTANCE = 50

pg.init()

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def main():

    CLOCK = pg.time.Clock()

    # Ajout des aliments
    pg.time.set_timer(pg.USEREVENT, 1000)

    running = True

    while running:

        screen.fill((255, 255, 255))

        al.FOOD_LIST.draw(screen)
        al.FOOD_LIST.update()

        # Update and draw bras

        pg.display.flip()
        CLOCK.tick(30)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.USEREVENT:
                al.create_new_aliment()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse = pg.math.Vector2(pg.mouse.get_pos())
                for food in al.FOOD_LIST:
                    center = pg.math.Vector2(food.rect.center)
                    if (center - mouse).length() < GRAB_DISTANCE:
                        food.grabbed = True
            if event.type == pg.MOUSEBUTTONUP:
                pass
    pg.quit()

if __name__ == '__main__':
    main()

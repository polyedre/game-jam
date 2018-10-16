import pygame as pg
import aliments as al

GAME_NAME = "Eat and never run"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pg.init()

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pg.display.flip()

def main():

    CLOCK = pg.time.Clock()

    # Ajout des aliments
    pg.time.set_timer(pg.USEREVENT, 1000)

    running = True

    while running:

        screen.fill((255, 255, 255))

        # Update and draw aliments
        for food in al.FOOD_LIST:
            food.draw(screen)
        al.FOOD_LIST.update()

        # Update and draw bras

        pg.display.flip()
        CLOCK.tick(30)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.USEREVENT:
                al.create_new_aliment()

    pg.quit()

if __name__ == '__main__':
    main()

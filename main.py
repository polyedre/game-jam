import pygame as pg
import aliments as al

import gui

GAME_NAME = "Eat and never run"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

<<<<<<< HEAD
pg.init()

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pg.display.flip()
=======
MEM_MOUSE_EVENT = pg.USEREVENT + 1
MEM_MOUSE_EVENT_TIME = 100

pg.init()

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
>>>>>>> aliments

gui.init()

def main():

    CLOCK = pg.time.Clock()

    # Ajout des aliments
    pg.time.set_timer(pg.USEREVENT, 1000)
<<<<<<< HEAD
=======
    pg.time.set_timer(MEM_MOUSE_EVENT, MEM_MOUSE_EVENT_TIME)
>>>>>>> aliments

    running = True

    while running:

        screen.fill((255, 255, 255))

<<<<<<< HEAD
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

=======
        al.FOOD_LIST.draw(screen)
        al.FOOD_LIST.update()
        al.updateMouseHistory()

        # GUI

        for element in gui.GUI_LIST:
            element.update()
            element.draw(screen)

        # Update and draw bras

        pg.display.flip()
        CLOCK.tick(30)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.USEREVENT:
                al.create_new_aliment()

            if event.type == pg.MOUSEBUTTONDOWN:
                al.handleGrab()
                gui.handleGrab()

            if event.type == pg.MOUSEBUTTONUP:
                al.handleUngrab()
                gui.handleUngrab()

            if event.type == MEM_MOUSE_EVENT:
                al.updateMouseHistory()

    pg.quit()

>>>>>>> aliments
if __name__ == '__main__':
    main()

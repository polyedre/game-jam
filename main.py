import pygame as pg
import aliments as al

GAME_NAME = "Eat and never run"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MEM_MOUSE_EVENT = pg.USEREVENT + 1
MEM_MOUSE_EVENT_TIME = 100

pg.init()

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def main():

    CLOCK = pg.time.Clock()

    # Ajout des aliments
    pg.time.set_timer(pg.USEREVENT, 1000)
    pg.time.set_timer(MEM_MOUSE_EVENT, MEM_MOUSE_EVENT_TIME)

    running = True

    while running:

        screen.fill((255, 255, 255))

        al.FOOD_LIST.draw(screen)
        al.FOOD_LIST.update()
        al.updateMouseHistory()
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

            if event.type == pg.MOUSEBUTTONUP:
                al.handleUngrab()

            if event.type == MEM_MOUSE_EVENT:
                al.updateMouseHistory()

    pg.quit()

if __name__ == '__main__':
    main()


# Pygame Boilerplate
# Author: Tyler Bradley
# 2021 Version

import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
BGCOLOUR = (100, 100, 255)

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "<<DVD Screen Saver>>"


class Dvdimage:
    """Represents a dvdimage on screen

    Attributes:
        x, y: coordinates of top-left corner
        width: width of our rectangle in px
        height: height of our rectangle in px
        colour: 3-tuple of (r, g, b)
    """
    def __init__(self):
        self.x, self.y = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.width = 150
        self.height = 90
        self.colour = BLACK

    def rect(self) -> pygame.rect:
        """Returns a pygame.rect that represents the dvdimage"""
        return[self.x, self.y, self.width, self.height]


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    dvd_image = Dvdimage()

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT

        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)      # fill with bgcolor

        # TODO: Draw our dvdimage
        pygame.draw.rect(screen, dvd_image.colour, dvd_image.rect()) # TODO: method

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()
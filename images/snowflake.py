# Snowfall
# Author: Ubial
# 2021 Version

import random
import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
BGCOLOUR = BLACK

SCREEN_WIDTH  = 999
SCREEN_HEIGHT = 666
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "<<Snowfall>>"

class Snowflake:
    """Represents a snowflake on screen

    Attributes:
        size: radius of sowfalke in px
        coords: {x: int, y:int}
        y-vel: falling velocity in px/sec
        colour: (r, g, b)
    """

    def __init__(self):
        self.size = 2
        self.coords = [
            random.randrange(0, SCREEN_WIDTH),
            random.randrange(0, SCREEN_HEIGHT)
        ]
        self.y_vel = 2
        self.colour = WHITE

    def update(self):
        """Update the location of the snow """
        self.coords[1] += self.y_vel

        if self.coords[1] > SCREEN_HEIGHT:
            self.coords = [
                random.randrange(0, SCREEN_WIDTH),
                random.randrange(-25, 0)
            ]

def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_snowflakes = 250

    snowflakes = []

    for i in range(num_snowflakes):
        close_snowflake = Snowflake
        close_snowflake.size = 6
        close_snowflake.y_vel = 2
        snowflakes.append(close_snowflake)


    for i in range(num_snowflakes):
        snowflakes.append(Snowflake())

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        for snow in snowflakes:
            snow.update()
        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)      # fill with bgcolor

        for snow in snowflakes:
            pygame.draw.circle(screen, snow.colour, snow.coords, snow.size)
        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()


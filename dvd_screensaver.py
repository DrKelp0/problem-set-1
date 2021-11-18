
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
# 800
# 600
SCREEN_WIDTH  = 814
SCREEN_HEIGHT = 590
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "<<DVD Screen Saver>>"


class Dvdimage:
    """Represents a dvdimage on screen

    Attributes:
        x, y: coordinates of top-left corner
        width: width of our rectangle in px
        height: height of our rectangle in px
        img: visual representation of our Dvdimage
        colour: 3-tuple of (r, g, b)
        x-vel: velocity in px/sec
        y-vel: velocity in px/sec
    """
    def __init__(self):
        self.x, self.y = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.width = 80
        self.height = 80
        self.colour = BLACK
        self.img = pygame.image.load("./images/dvdimage.png")
        self.x_vel = 5
        self.y_vel = 0


    def rect(self) -> pygame.rect:
        """Returns a pygame.rect that represents the dvdimage"""
        return[self.x, self.y, self.width, self.height]

    def update(self) -> None:
        """Updates the Dvdimage with every tick"""
        # Update the x coordinate
        self.x += self.x_vel
        # if Dvdimage is too far to the left
        if self.x < 0:
            # Keep the object inside the canvas
            self.x = 0
            # Set the velocity to negative
            self.x_vel = -self.x_vel

        # if Dvdimage is too far to the right
        if self.x + self.width > SCREEN_WIDTH:
            # Keep the object inside the canvas
            self.x = SCREEN_WIDTH - self.width
            # Set the velocity to negative
            self.x_vel = -self.x_vel

        # Update the y coordinate
        # If Dvdimage is too low
        self.y += self.y_vel
        if self.y + self.height > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.height
            self.y_vel = -self.y_vel

        # If Dvdimage is too high
        if self.y < 0:
            # Keep the object inside the canvas
            self.y = 0
            # Set the velocity to negative
            self.y_vel = -self.y_vel


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    dvd_image = Dvdimage()
    bg_image = pygame.image.load("./images/Jimmy.png")
    # Transform the size of the bg_image
    bg_image = pygame.transform.scale(bg_image, (814, 590))

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        dvd_image.update()
        print(f"x: {dvd_image.x}, y: {dvd_image.y}")

        # ----------- DRAW THE ENVIRONMENT
        # Draw the background image
        screen.blit(bg_image, (0, 0))
        # .blit(<surface/image>, coords)
        screen.blit(dvd_image.img, (dvd_image.x, dvd_image.y))


        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()
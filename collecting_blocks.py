# Pygame Boilerplate
# Author: Tyler


import random
import time
import pygame
import pygame.sprite

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (0,   0, 255)
BGCOLOUR = (100, 100, 255)

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "<<Collecting Blocks>>"

class Player(pygame.sprite.Sprite):
    """Describes a player object
    A subclass of pygame.sprite.Sprite

    Attributes:
        image: Surface that is the visual
            representation of or Block
        rect: numerical representation of
            our Block [x, y, width, height]
    """
    def __init__(self) -> None:
        # Call the superclass constructor
        super().__init__()

        # Create the image of the block
        self.image = pygame.image.load("./images/charizard.png")

        # Resize the image (scale)
        self.image = pygame.transform.scale(self.image, (42, 42))

        self.rect = self.image.get_rect()

class Block (pygame.sprite.Sprite):
    """Describes a block object
    A subclass of pygame.sprite.Sprite

    Attributes:
        image: Surface that is the visual
            representation of or Block
        rect: numerical representation of
            our Block [x, y, width, height]
    """
    def __init__(self, colour: tuple, width: int, height: int) -> None:
        """
        Arguments
        :param colour: 3-tuple (r, g, b)
        :param width: width in pixels
        :param height: height in pixels
        """
        # Call the superclass constructor
        super().__init__()


        # Create the image of the block
        self.image = pygame.image.load("./images/sprite_cranberry.png")
        # Resize the image (scale)
        self.image = pygame.transform.scale(self.image, (24, 39))

        self.rect = self.image.get_rect()

class Enemy(pygame.sprite.Sprite):
    """The enemy sprites

    Attributes:
        image: Surface that is the visual representation
        rect: Rect (x, y, width, height)
    """
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/bowser.png")
        # Resize the image (scale)
        self.image = pygame.transform.scale(self.image, (41, 48))

        self.rect = self.image.get_rect()
        # Define the initial location
        self.rect.x, self.rect.y = (
            random.randrange(SCREEN_WIDTH),
            random.randrange(SCREEN_HEIGHT)
        )

        # Define the initial velocity
        self.x_vel = random.choice([-4, -3, 3, -4])
        self.y_vel = random.choice([-4, -3, 3, -4])

    def update(self) -> None:
        """Calculate movement"""
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        # Constrain movement
        # X -
        if self.rect.left < 0:
            self.rect.x = 0
            self.x_vel = -self.x_vel    # bounce

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right > SCREEN_WIDTH
            self.x_vel = -self.x_vel    # bounce
        # y -
        if self.rect.y < 0:
            self.rect.y = 0
            self.y_vel = -self.y_vel    # bounce
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom > SCREEN_HEIGHT
            self.y_vel = -self.y_vel    # bounce

def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_blocks = 50
    score = 0
    num_enemies = 10
    time_start = time.time()
    time_invincible = 5

    font = pygame.font.SysFont("Georgia", 25)

    pygame.mouse.set_visible(False)

    # Create groups to hold sprites
    all_sprites = pygame.sprite.Group()
    blocks_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()

    # Create all the block sprites and add to block_sprites
    for i in range(num_blocks):

        # Create a block (set its parameters)
        block = Block(BLACK, 20, 15)

    # Set a  random location for the block inside the screen
        block.rect.x = random.randrange(SCREEN_WIDTH - block.rect.width)
        block.rect.y = random.randrange(SCREEN_HEIGHT - block.rect.height)

    # Add the block to the block_sprites Group
    # Add the block to the all_sprites Group
        blocks_sprites.add(block)
        all_sprites.add(block)

    # Create enemy sprites
    for i in range(num_enemies):
        enemy = Enemy()

    # Set a  random location for the enemy inside the screen
        enemy.rect.x = random.randrange(SCREEN_WIDTH - enemy.rect.width)
        enemy.rect.y = random.randrange(SCREEN_HEIGHT - enemy.rect.height)

    # Add the enemy to the enemy_sprites Group
    # Add the enemy to the all_sprites Group
        enemy_sprites.add(enemy)
        all_sprites.add(enemy)

    # Create the Player block
    player = Player()
    # Add the player to all sprites group
    all_sprites.add(player)

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        # Process player movement based on mouse pos
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x, player.rect.y = mouse_pos

        # Update the location of all the sprites
        all_sprites.update()

        # Check all collisions between player and blocks
        blocks_collided = pygame.sprite.spritecollide(player, blocks_sprites, True)

        for block in blocks_collided:
            score += 1
            print(f"Score: {score}")

        # Check all collisions between player and enemies
        enemy_collided = pygame.sprite.spritecollide(player, enemy_sprites, True)

        # Set a time for invincibility at start of game
        if time.time() - time_start > time_invincible:
            for enemy in enemy_collided:
                done = True
                print("GAME OVER")

        # Make win screen
        if score >= 50:
            done = True
            print(f"You got {score} points!")
            print(f"YOU WIN!")


        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)      # fill with bgcolor

        # Draw all sprites
        all_sprites.draw(screen)

        # Draw the score on the screen
        screen.blit(
            font.render(f"Score: {score}", True, BLACK),
            (5, 5)
        )

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()
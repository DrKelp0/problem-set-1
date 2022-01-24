"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

From:
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py

Explanation video: http://youtu.be/QplXBw_NK5Y

Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/

"""

import pygame
import time

# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


class Player(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the player controls.
    """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Create an image of the player
        self.image = pygame.image.load("./Player.png")
        # Resize the image (scale)
        self.image = pygame.transform.scale(self.image, (40, 40))


        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.level = None

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35


    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0


class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()


        self.image = pygame.image.load("./Platform.png")
        # Resize the image (scale)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()


class Npc(pygame.sprite.Sprite):
    """NPC that talks to you when you get near it"""

    def __init__(self):
        super().__init__()


        self.image = pygame.image.load("./Npc.png")
        # Resize the image (scale)
        self.image = pygame.transform.scale(self.image, (75, 100))

        self.rect = self.image.get_rect()
        # Define the initial location
        self.rect.x, self.rect.y = (650, 700)

class Npcc(pygame.sprite.Sprite):
    """NPC that talks to you when you get near it"""

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./Npcc.png")
        # Resize the image (scale)
        self.image = pygame.transform.scale(self.image, (75, 75))

        self.rect = self.image.get_rect()
        # Define the initial location
        self.rect.x, self.rect.y = (400, -2250)

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player, npc, npcc):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.npc_list = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.player_group.add(player)
        self.player = player
        self.npc_list.add(npc)
        self.npc_list.add(npcc)


        # How far this world has been scrolled up/down
        self.world_shift = 0

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        self.npc_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """


        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.npc_list.draw(screen)
        self.player_group.draw(screen)

    def shift_world(self, shift_y):
        """ When the user moves up/down and we need to scroll
        everything: """

        # Keep track of the shift amount
        self.world_shift += shift_y

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.y += shift_y

        for enemy in self.enemy_list:
            enemy.rect.y += shift_y

        for npc in self.npc_list:
            npc.rect.y += shift_y

        for npcc in self.npc_list:
            npcc.rect.y += shift_y



# Create objects for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player, npc, npcc):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player, npc, npcc)

        self.level_limit = -1000

        # Array with width, height, x, and y of platform
        level = [
                 [50, 15, 200, 700],    # Beginning platforms
                 [50, 15, 425, 550],
                 [50, 15, 625, 400],
                 [30, 15, 800, 350],

                 [50, 15, 950, 200],    # Side platforms
                 [70, 15, 930, 50],
                 [100, 15, 900, -100],

                 [15, 25, 900, -85],    # Mini blockade

                 [45, 15, 475, -35],
                 [35, 15, 475, 75],
                 [20, 125, 510, -35],   # Curved shape

                 [200, 15, 100, 75],
                 [200, 15, 100, -35],
                 [20, 100, 280, 75],    # Bottom L
                 [20, 190, 280, -225],  # Top L

                 [30, 15, 15, -35],     # Mini blockade

                 [20, 15, 260, -150],   # Wall platform

                 [20, 15, 600, -275],   # Small platforms
                 [20, 15, 600, -425],
                 [20, 15, 300, -500],
                 [75, 15, 425, -640],
                 [35, 15, 865, -640],
                 [35, 15, 925, -785],
                 [35, 15, 675, -900],

                 [200, 15, 300, -1000],     # Landmark


                 # Walls and floor
                 [1000, 100, 0, 800],
                 [10, 2000, -10, -1000],
                 [10, 2000, 1000, -1000],

                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

# # Create platforms for the level
# class Level_02(Level):
#     """ Definition for level 2. """
#
#     def __init__(self, player):
#         """ Create level 1. """
#
#         # Call the parent constructor
#         Level.__init__(self, player)
#
#         self.level_limit = -1000
#
#         # Array with type of platform, and x, y location of the platform.
#         level = [[210, 30, 450, 570],
#                  [210, 30, 850, 420],
#                  [210, 30, 1000, 520],
#                  [210, 30, 1120, 280],
#                  ]
#
#         # Go through the array above and add platforms
#         for platform in level:
#             block = Platform(platform[0], platform[1])
#             block.rect.x = platform[2]
#             block.rect.y = platform[3]
#             block.player = self.player
#             self.platform_list.add(block)


def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Fodian-Platformer")

    # Create the player and npcs
    player = Player()
    npc = Npc()
    npcc = Npcc()


    # Create all the levels
    level_list = []
    level_list.append(Level_01(player, npc, npcc))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height

    # active_sprite_list.add(npc)
    # active_sprite_list.add(npcc)
    active_sprite_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Create groups to hold sprites
    npc_sprites = pygame.sprite.Group()
    npcc_sprites = pygame.sprite.Group()


    # Add the Npc to the enemy_sprites Group
    # Add the Npc to the all_sprites Group
    npc_sprites.add(npc)
    npcc_sprites.add(npcc)

    numb_collided = 0
    numbc_collided = 0
    time_start = time.time()
    time_cooldown = 1




    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update the player and npcs
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        npc_collided = pygame.sprite.spritecollide(player, npc_sprites, False)
        npcc_collided = pygame.sprite.spritecollide(player, npcc_sprites, False)


        if time.time() - time_start < time_cooldown:
            for npc in npc_collided:
                False
        elif time.time() - time_start > time_cooldown:
            for npc in npc_collided:
                if numb_collided == 0:
                    print("What are you doing here?")
                    numb_collided += 1
                    time_cooldown += 3

                elif numb_collided == 1:
                    print("You want to go up?")
                    numb_collided += 1
                    time_cooldown += 3


                elif numb_collided == 2:
                    print("Impossible, you will never reach the top")
                    numb_collided += 1
                    time_cooldown += 3


                elif numb_collided == 3:
                    print("There is nothing for you here")
                    numb_collided += 1
                    time_cooldown += 10


                elif numb_collided == 4:
                    print("Back again?\n"
                          "Looks like it's about time to give up")
                    numb_collided += 1
                    time_cooldown += 3

        if time.time() - time_start < time_cooldown:

            for npcc in npcc_collided:
                False
        elif time.time() - time_start > time_cooldown:
            for npcc in npcc_collided:
                if numbc_collided == 0:
                    print("hello")
                    numbc_collided += 1
                    time_cooldown += 3


        # If the player gets near the right side, shift the world up (-y)
        if player.rect.top <= 100:
            diff = player.rect.top - 100
            player.rect.top = 100
            current_level.shift_world(-diff)


        # If the player gets near the bottom, shift the world down (y)
        if player.rect.bottom > SCREEN_HEIGHT:
            diff = 800 - player.rect.bottom
            player.rect.bottom = 800
            current_level.shift_world(diff)


        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list) - 1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        bg_image = pygame.image.load("Wallpaper.jpg")
        # Transform the size of the bg_image
        bg_image = pygame.transform.scale(bg_image, (1000, 800))
        # Draw the background image
        screen.blit(bg_image, (0, 0))



        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        # all_sprites.draw(screen)
        # active_sprite_list.draw(screen)


        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()
# Pygame Boilerplate
# Author: Tyler


import random
import time
import pygame
import pygame.sprite

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BGCOLOUR = (100, 100, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "<<Collecting Blocks>>"


class Player(pygame.sprite.Sprite):
    """Describes a player object
    A subclass of pygame.sprite.Sprite

    Attributes:
        image: Surface that is the visual
            representation of or Block
        rect: numerical representation of
            our Block [x, y, width, height]
        hp: describe how much health our
        player has
    """

    def __init__(self) -> None:
        # Call the superclass constructor
        super().__init__()

        # Create the image of the block
        self.image = pygame.image.load("./images/charizard.png")

        # Resize the image (scale)
        self.image = pygame.transform.scale(self.image, (42, 42))

        self.rect = self.image.get_rect()

        # Initial health points
        self.hp = 100

    def hp_remaining(self) -> int:
        """Return the percent of health remaining"""
        return self.hp / 100


class Enemy(pygame.sprite.Sprite):
    """The enemy sprites

    Attributes:
        image: Surface that is the visual representation
        rect: Rect (x, y, width, height)
    """

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/spaceinvaders.png")
        # Resize the image (scale)
        self.image = pygame.transform.scale(self.image, (56, 40))

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
            self.x_vel = -self.x_vel  # bounce

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right > SCREEN_WIDTH
            self.x_vel = -self.x_vel  # bounce
        # y -
        if self.rect.y < 0:
            self.rect.y = 0
            self.y_vel = -self.y_vel  # bounce
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom > SCREEN_HEIGHT
            self.y_vel = -self.y_vel  # bounce


class Bullet(pygame.sprite.Sprite):
    """Bullet

    Attributes:
        image: visual representation
        rect: mathematical representation
        vel_y: y velocity in px/sec
        """

    def __init__(self, coords: tuple):
        """

        Arguments:
             coords: tuple of (x, y) to represent initial location
        """
        super().__init__()

        self.image = pygame.Surface((5, 10))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

        # Set the middle of the bullet to be at coords
        self.rect.center = coords

        self.vel_y = 5

    def update(self):
        self.rect.y -= self.vel_y

class Superbullet(pygame.sprite.Sprite):
    """Superbullet

    Attributes:
        image: visual representation
        rect: mathematical representation
        vel_y: y velocity in px/sec
        """

    def __init__(self, coords: tuple):
        """

        Arguments:
             coords: tuple of (x, y) to represent initial location
        """
        super().__init__()

        self.image = pygame.Surface((8, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        # Set the middle of the bullet to be at coords
        self.rect.center = coords

        self.vel_y = 4

    def update(self):
        self.rect.y -= self.vel_y


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    score = 0
    num_enemies = 15
    time_start = time.time()
    time_invincible = 3
    game_state = "running"
    time_ended = time.time()
    time_cooldown = 4
    super_bulletnumber = 1

    # Check for high score
    with open("./data/shootemup_highscore.txt") as f:
        high_score = int(f.readline().strip())

    endgame_messages = {
        "win": "Congratulations, you won!",
        "lose": "Sorry, they got you. Play again!"
    }

    font = pygame.font.SysFont("Georgia", 25)

    pygame.mouse.set_visible(False)

    # Create groups to hold sprites
    all_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()

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
            if event.type == pygame.MOUSEBUTTONUP:
                if len(bullet_sprites) < 3 and time.time() - time_start > time_invincible:
                    bullet = Bullet(player.rect.midtop)
                    # Add it to the allsprites group
                    all_sprites.add(bullet)
                    bullet_sprites.add(bullet)

        if pygame.key.get_pressed([pygame.K_SPACE]):
            # Do something for the keyboard
            if len(super_bullet) < 1 and time.time() - time.start > time_invincible:
                super_bullet = Superbullet(player.rect.midtop)
                all_sprites.add(bullet)
                super_bullet.add(bullet)
            pass

        # LOSE CONDITION - Player hp goes below 0
        if player.hp_remaining() <= 0:
            done = True
        # ----------- CHANGE ENVIRONMENT
        # Process player movement based on mouse pos
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x, player.rect.y = mouse_pos

        # Check nu,ber of enemies currently on the screen
        if len(enemy_sprites) < 1:
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

            num_enemies += 5
            if player.hp <= 80:
                player.hp += 20
            super_bulletnumber += 1

        # Update the location of all the sprites (blocks, player)
        if game_state == 'running':
            enemy_sprites.update()
            bullet_sprites.update()
        player.update()

        # Check all collisions between player and enemies
        enemy_collided = pygame.sprite.spritecollide(player, enemy_sprites, False)

        # Set a time for invincibility at start of game
        if time.time() - time_start > time_invincible:
            if game_state == "running":
                for enemy in enemy_collided:
                    player.hp -= 1
                    print(player.hp)  # debugging

        elif game_state == "won":
            for enemy in enemy_collided:
                player.hp - 0

        # Check bullet collisions with enemies
        # Kill the bullets when they've left the screen
        for bullet in bullet_sprites:
            enemies_bullet_collided = pygame.sprite.spritecollide(
                bullet,
                enemy_sprites,
                True
            )

            # If the bullet has struck some enemy
            if len(enemies_bullet_collided) > 0:
                bullet.kill()
                score += 1

            if bullet.rect.y < 0:
                bullet.kill()

        for super_bullet in bullet_sprites:
            enemies_bullet_collided = pygame.sprite.spritecollide(
                super_bullet,
                enemy_sprites,
                True
            )

            # If the bullet has struck some enemy
            if enemies_bullet_collided:
                score += 1

            if bullet.rect.y < 0:
                bullet.kill()

        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)  # fill with bgcolor

        # Draw all sprites
        all_sprites.draw(screen)

        # Draw the score on the screen
        screen.blit(
            font.render(f"Score: {score}", True, BLACK),
            (5, 5)
        )
        # Draw the high score on the screen
        screen.blit(
            font.render(f"High Score: {high_score}", True, BLACK),
            (5, 30)
        )

        # Draw a health bar
        # Draw the background rectangle
        pygame.draw.rect(screen, GREEN, [580, 5, 215, 20])
        # Draw the foreground rectangle which represents the remaining health
        life_remaining = 215 - int(215 * player.hp_remaining())
        pygame.draw.rect(screen, BLACK, [580, 5, life_remaining, 20])

        # If we've won, draw the text on the screen
        if game_state == "won":
            screen.blit(
                font.render(endgame_messages["win"], True, BLACK),
                (SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2)
            )
        if game_state == "lose":
            screen.blit(
                font.render(endgame_messages["lose"], True, BLACK),
                (SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2)
            )

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)

    # Clean-up

    # Update the high score if the current score is the highest
    with open("./data/shootemup_highscore.txt", "w") as f:
        if score > high_score:
            f.write(str(score))
        else:
            f.write(str(high_score))


if __name__ == "__main__":
    main()

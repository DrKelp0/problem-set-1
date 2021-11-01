# Midnight Rider

import random
import sys
import textwrap
import time
import midnight_rider_text


# A text-based game of intrigue and illusion
MAX_FUEL = 50
MAX_TOFU = 3

class Game:
    """Represent our game engine

    Attribute:
        done: describes the game is
            finished or not - bool
        distance_travelled: describe the distance
            that we've travelled so far this game,
            in km
        amount_tofu: how much tofu we have
            left in our inventory
        agents_distance: describes the distance
            between the player and the agents
            fuel: describes amount of fuel remaining
                starts off at 50
    """
    def __init__(self):
        self.done = False
        self.distance_travelled = 0
        self.amount_tofu = MAX_TOFU
        self.agents_distance = -20
        self.fuel = MAX_FUEL

    def introduction(self) -> None:
        """Print the introduction text"""
        self.typewriter_effect(midnight_rider_text.INTRODUCTION)

    def typewriter_effect(self, text: str) -> None:
        """Print out to console with a typewriter effect"""
        for char in textwrap.dedent(text):
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    def show_choices(self) -> None:
        """Show the user their choices"""
        time.sleep(1)
        print(midnight_rider_text.CHOICES)
        time.sleep(1)

    def get_choice(self) -> None:
        """Gets the user's choice and changes
        the environment"""
        # Get the user's response
        user_choice = input().strip(",.?!").lower()

        # Based on their choice, change the attribute
        # of the class
        # TODO: Impliment eating/hunger
        agents_distance_now = random.randrange(7, 15)

        if user_choice == "c":
            # Move the player
            player_distance_now = random.randrange(10, 16)
            self.distance_travelled += player_distance_now

            # Move the agents
            self.agents_distance += agents_distance_now

            # Burn fuel
            self.fuel -= random.randrange(5,11)

            # Give the player some feedback
            print(f"\n-------ZOOOOOOOOM!")
            print(f"-------You travelled {player_distance_now} kms.\n")

        if user_choice == "b":
            # Move the player
            player_distance_now = random.randrange(3, 8)
            self.distance_travelled += player_distance_now

            # Move the agents
            self.agents_distance += agents_distance_now

            # Burn fuel
            self.fuel -= random.randrange(4, 9)
            # Give the player some feedback
            print(f"\n-------You drive conservatively")
            print(f"-------You travelled {player_distance_now} kms.\n")

        elif user_choice == "d":
            self.fuel = MAX_FUEL
            # Decide how far the agents go
            self.agents_distance += agents_distance_now
            # Give the user feedback
            print(midnight_rider_text.REFUEL)
            time.sleep(2)
        elif user_choice == "e":
            print("---Status Check---")
            print(f"Distance Travelled: {self.distance_travelled} kms")
            print(f"Fuel remaining: {self.fuel} L")
            print(f"Tofu Pieces Left: {self.amount_tofu}")
            print(f"Agent's Distance: {abs(self.agents_distance)} km behind")
            print("------")
            time.sleep(2)
        elif user_choice == "q":
            self.done = True

def main() -> None:
    game = Game() # starting a new game
    # game.introduction()

    while not game.done:
        game.show_choices()
        game.get_choice()
        # TODO: Check win/lose conditions


if __name__ == "__main__":
    main()
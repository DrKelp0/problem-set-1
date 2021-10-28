# Midnight Rider

import sys
import textwrap
import time
import midnight_rider_text
# A text-based game of intrigue and illusion


class Game:
    """Represent our game engine

    """
    def introduction(self) -> None:
        """Print the introduction text"""
        self.typewriter_effect(midnight_rider_text.INTRODUCTION)

    def typewriter_effect(self, text: str) -> None:
        """Print out to console with a typewriter effect"""
        for char in textwrap.dedent(text):
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

def main() -> None:
    game = Game() # starting a new game
    game.introduction()


if __name__ == "__main__":
    main()
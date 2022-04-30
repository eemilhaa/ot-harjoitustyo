# TODO split and refactor this file
import pygame
from game_loop import GameLoop
from level import Level
from sprites.player import Player
from sprites.background import BackGround1
from maps import map_1, map_2, map_3
from renderer import Renderer

from database import DataBase

from ui.ui import UI

import config


DISPLAY_HEIGHT = config.DISPLAY_HEIGHT    # This can change
DISPLAY_WIDTH = DISPLAY_HEIGHT / 0.75   # keep 4:3 aspect ratio
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE)
CLOCK = pygame.time.Clock()
DATABASE = DataBase()


# Define on_click functions for menu buttons
def start_game():
    """A function for constructing the levels and starting the game

    Returns whatever the game loop returns. This makes it possible for a
    client using a button with this function to know how the game loop
    ended (i.e. did the player win or lose)
    """

    game_renderer = Renderer(
        display=DISPLAY
    )

    level_1 = Level(
        player=Player(5, 160),
        game_map=map_1,
        background=BackGround1()
    )
    level_2 = Level(
        player=Player(230, 160),
        game_map=map_2,
        background=BackGround1()
    )
    level_3 = Level(
        player=Player(2, 160),
        game_map=map_3,
        background=BackGround1()
    )
    game_loop = GameLoop(
        levels=[
            level_1,
            level_2,
            level_3,
        ],
        clock=CLOCK,
        renderer=game_renderer,
        database=DATABASE,
    )
    return game_loop.run()


UI = UI(
    display=DISPLAY,
    clock=CLOCK,
    database=DATABASE,
    start_function=start_game
)


def main():
    pygame.init()
    UI.menu_loop.run()


if __name__ == "__main__":
    main()

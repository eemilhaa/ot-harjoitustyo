import pygame
from game.game_loop import GameLoop
from game.level import Level
from game.sprites.player import Player
from game.sprites.background import BackGround
from game.maps import map_1, map_2, map_3
from game.renderer import Renderer
from game.clock import Clock
from game.event_queue import EventQueue
from database import DataBase
from ui.ui import UI
import config


# Always keep 4:3 aspect ratio
DISPLAY = pygame.display.set_mode((
    config.DISPLAY_SIZE
))
CLOCK = Clock()
EVENT_QUEUE = EventQueue()
DATABASE = DataBase()
RENDERER = Renderer(display=DISPLAY)


def start_game():
    """A function for constructing the levels and starting the game.

    This function is how the game loop can be started from the UI. In the UI
    it is assigned as an on_click function to all buttons that should start the
    game.

    Returns:
        The function Returns whatever the game_loop.run() returns. This makes
        it possible for a client (the menu loop) using a button with this
        function to know how the game loop ended (i.e. to what level the player
        got)
    """

    level_1 = Level(
        player=Player(5, 160),
        game_map=map_1,
        background=BackGround()
    )
    level_2 = Level(
        player=Player(230, 160),
        game_map=map_2,
        background=BackGround()
    )
    level_3 = Level(
        player=Player(2, 160),
        game_map=map_3,
        background=BackGround()
    )
    game_loop = GameLoop(
        levels=[
            level_1,
            level_2,
            level_3,
        ],
        clock=CLOCK,
        renderer=RENDERER,
        event_queue=EVENT_QUEUE,
        database=DATABASE,
    )
    return game_loop.run()


UI = UI(
    display=DISPLAY,
    database=DATABASE,
    game_start_function=start_game
)


def main():
    """Inits pygame and starts the menu loop"""

    pygame.init()
    UI.menu_loop.run()


if __name__ == "__main__":
    main()

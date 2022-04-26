# TODO split and refactor this file
import sys
import pygame
from game_loop import GameLoop
from level import Level
from sprites.player import Player
from sprites.background import BackGround1
from maps import map_1, map_2, map_3
from renderer import Renderer

from database import DataBase

from ui.menu import Menu
from ui.button import Button
from ui.menu_loop import MenuLoop

import config


DISPLAY_HEIGHT = config.DISPLAY_HEIGHT    # This can change

# Define some constants based on display size
DISPLAY_WIDTH = DISPLAY_HEIGHT / 0.75   # keep 4:3 aspect ratio
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
BUTTON_WIDTH = DISPLAY_WIDTH / 4        # dynamic button size
BUTTON_HEIGHT = BUTTON_WIDTH / 2

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


def to_start_menu():
    """Returns the dict key of the start menu"""

    return "start"


def to_controls_menu():
    """Returns the dict key of the controls menu"""

    return "controls"


def to_stats_menu():
    """Returns the dict key of the stats menu"""

    return "stats"


def main():

    # Create buttons
    start_button = Button(
        # TODO location setting could be cleaner
        x_location=DISPLAY_WIDTH-BUTTON_WIDTH*1.5,
        y_location=DISPLAY_HEIGHT-BUTTON_HEIGHT*1.5,
        color=(100, 200, 100),
        text="START",
        width=BUTTON_WIDTH,
        on_click=start_game,
    )
    retry_button = Button(
        x_location=DISPLAY_WIDTH-BUTTON_WIDTH*1.5,
        y_location=DISPLAY_HEIGHT-BUTTON_HEIGHT*1.5,
        color=(100, 200, 100),
        text="RETRY",
        width=BUTTON_WIDTH,
        on_click=start_game,
    )
    quit_button = Button(
        x_location=BUTTON_WIDTH-BUTTON_WIDTH*0.5,
        y_location=DISPLAY_HEIGHT-BUTTON_HEIGHT*1.5,
        color=(255, 100, 100),
        text="QUIT",
        width=BUTTON_WIDTH,
        on_click=sys.exit,
    )
    controls_button = Button(
        x_location=DISPLAY_WIDTH-BUTTON_WIDTH*1.5,
        y_location=DISPLAY_HEIGHT-BUTTON_HEIGHT*1.5*2,
        color=(255, 150, 100),
        text="CONTROLS",
        width=BUTTON_WIDTH,
        on_click=to_controls_menu,
    )
    back_button = Button(
        x_location=BUTTON_WIDTH-BUTTON_WIDTH*0.5,
        y_location=DISPLAY_HEIGHT-BUTTON_HEIGHT*1.5*2,
        color=(255, 150, 100),
        text="BACK",
        width=BUTTON_WIDTH,
        on_click=to_start_menu,
    )
    stats_button = Button(
        x_location=BUTTON_WIDTH-BUTTON_WIDTH*0.5,
        y_location=DISPLAY_HEIGHT-BUTTON_HEIGHT*1.5*2,
        color=(255, 150, 100),
        text="STATS",
        width=BUTTON_WIDTH,
        on_click=to_stats_menu,
    )

    # Create menus
    start_menu = Menu(
        background=(54, 54, 70),
        buttons=[
            start_button,
            quit_button,
            controls_button,
            stats_button,
        ],
        text=[
            "START MENU",
            "",
            "click the buttons to advance"
        ],
    )
    controls_menu = Menu(
        background=(70, 70, 70),
        buttons=[
            back_button
        ],
        text=[
            "CONTROLS",
            "",
            "LEFT ARROW --- LEFT",
            "RIGHT ARROW -- RIGHT",
            "SPACE -------- JUMP",
        ]
    )
    game_over_menu = Menu(
        background=(100, 50, 50),
        buttons=[
            retry_button,
            quit_button,
            back_button,
        ],
        text=[]     # This is set in the menu loop based on game outcome
    )
    stats_menu = Menu(
        background=(70, 70, 70),
        buttons=[
            back_button,
        ],
        text=[]
    )

    # All menus are stored in a dict so that navigation between them in the
    # menu loop can be done with dict keys rather than list indices
    menus = {
        "start": start_menu,
        "controls": controls_menu,
        "game_over": game_over_menu,
        "stats": stats_menu,
    }

    # The menu loop
    menu_loop = MenuLoop(
        menus=menus,
        clock=CLOCK,
        display=DISPLAY,
        database=DATABASE,
    )

    # Start from the menu
    pygame.init()
    menu_loop.run()


if __name__ == "__main__":
    main()

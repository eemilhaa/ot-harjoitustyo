import sys
import pygame
from game_loop import GameLoop
from level import Level
from sprites.player import Player
from sprites.background import BackGround1
from maps import map_1, map_2, map_3
from renderer import Renderer

from ui.menu import Menu
from ui.button import Button
from ui.menu_loop import MenuLoop


# TODO read this from conf file?
display_height = 900    # This can change


def main():

    # Define some constants based on display size
    display_width = display_height / 0.75   # keep 4:3 aspect ratio
    display_size = (display_width, display_height)
    button_width = display_width / 4        # dynamic button size
    button_height = button_width / 2

    # Use two surfaces for displaying the game to scale up the pixels
    drawing_surface_size = (240, 180)       # This is always the same
    drawing_surface = pygame.Surface(drawing_surface_size)
    scaled_surface = pygame.Surface(display_size)

    display = pygame.display.set_mode(display_size)
    clock = pygame.time.Clock()

    game_renderer = Renderer(
        display=display,
        drawing_surface=drawing_surface,
        scaled_surface=scaled_surface,
    )

    # Define on_click functions for menu buttons
    def start_game():
        """A function for constructing the levels and starting the game

        Returns whatever the game loop returns. This makes it possible for a
        client using a button with this function to know how the game loop
        ended (i.e. did the player win or lose)
        """

        level_1 = Level(
            player=Player(5, 160),
            game_map=map_1,
            background=BackGround1()
        )
        level_2 = Level(
            player=Player(230, 130),
            game_map=map_2,
            background=BackGround1()
        )
        level_3 = Level(
            player=Player(2, 130),
            game_map=map_3,
            background=BackGround1()
        )
        game_loop = GameLoop(
            levels=[
                level_1,
                level_2,
                level_3,
            ],
            clock=clock,
            renderer=game_renderer,
        )
        return game_loop.run()

    def to_start_menu():
        """Returns the dict key of the start menu"""

        return "start"

    def to_controls_menu():
        """Returns the dict key of the controls menu"""

        return "controls"

    # Create the buttons
    start_button = Button(
        # TODO location setting could be cleaner
        x_location=display_width-button_width*1.5,
        y_location=display_height-button_height*1.5,
        color=(100, 200, 100),
        text="START",
        width=button_width,
        on_click=start_game,
    )
    retry_button = Button(
        x_location=display_width-button_width*1.5,
        y_location=display_height-button_height*1.5,
        color=(100, 200, 100),
        text="RETRY",
        width=button_width,
        on_click=start_game,
    )
    quit_button = Button(
        x_location=button_width-button_width*0.5,
        y_location=display_height-button_height*1.5,
        color=(255, 100, 100),
        text="QUIT",
        width=button_width,
        on_click=sys.exit,
    )
    controls_button = Button(
        x_location=display_width-button_width*1.5,
        y_location=display_height-button_height*1.5*2,
        color=(255, 150, 100),
        text="CONTROLS",
        width=button_width,
        on_click=to_controls_menu,
    )
    back_button = Button(
        x_location=button_width-button_width*0.5,
        y_location=display_height-button_height*1.5*2,
        color=(255, 150, 100),
        text="BACK",
        width=button_width,
        on_click=to_start_menu,
    )

    # Create menus
    start_menu = Menu(
        background=(54, 54, 70),
        buttons=[
            start_button,
            quit_button,
            controls_button,
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
            "CONTROLS:",
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

    # All menus are stored in a dict so that navigation between them in the
    # menu loop can be done with dict keys rather than list indices
    menus = {
        "start": start_menu,
        "controls": controls_menu,
        "game_over": game_over_menu,
    }

    # The menu loop
    menu_loop = MenuLoop(
        menus=menus,
        clock=clock,
        display=display,
    )

    # Start from the menu
    pygame.init()
    menu_loop.run()


if __name__ == "__main__":
    main()

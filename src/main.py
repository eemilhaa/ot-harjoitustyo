# This file is a mess currently
import sys
import pygame
from game_loop import GameLoop
from level import Level
from sprites.player import Player
from sprites.background import BackGround1
from sprites.button import ButtonBackGround
from maps import map_1, map_2, map_3
from renderer import Renderer

from ui.menu import Menu
from ui.button import Button
from ui.rectbutton import RButton
from ui.menu_loop import MenuLoop


pygame.init()
display_width = 1200    # This can change
display_height = display_width * 0.75   # keep 4:3 aspect ratio
display_size = (display_width, display_height)
drawing_surface_size = (240, 180)   # This is constant

button_width = display_width * 0.25
button_height = button_width * 0.5

drawing_surface = pygame.Surface(drawing_surface_size)
scaled_surface = pygame.Surface(display_size)

display = pygame.display.set_mode(display_size)
clock = pygame.time.Clock()


game_renderer = Renderer(
    display=display,
    display_size=display_size,
    drawing_surface=drawing_surface,
    scaled_surface=scaled_surface,
)


def reset_game():
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
    game_loop.run()


# start_button = Button(
#     sprite=ButtonBackGround,
#     x_location=140,
#     y_location=120,
#     on_click=reset_game,
#     text="START",
# )
# quit_button = Button(
#     sprite=ButtonBackGround,
#     x_location=40,
#     y_location=120,
#     on_click=sys.exit,
#     text="QUIT",
# )
start_button = RButton(
    x_location=display_width-button_width*2,
    y_location=display_height-button_height*2,
    color=(0, 0, 0),
    text="START",
    width=button_width,
    on_click=reset_game,
)
quit_button = RButton(
    x_location=100,
    y_location=500,
    color=(255, 0, 0),
    text="QUIT",
    width=button_width,
    on_click=sys.exit,
)
start_menu = Menu(
    background=(54, 54, 70),
    buttons=[
        start_button,
        quit_button,
    ],
    text="START MENU",
)
# menu_renderer = Renderer(
#     content=start_menu,
#     display=display,
#     display_size=display_size,
#     drawing_surface=drawing_surface,
#     scaled_surface=scaled_surface,
# )
menu_loop = MenuLoop(
    menu=start_menu,
    clock=clock,
    display_size=display_size
)


# TODO make all this into a main loop?
class MainLoop:
    def __init__(self):
        pass


# Start from menu_loop
if __name__ == "__main__":
    menu_loop.run()

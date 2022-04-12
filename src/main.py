import sys
import pygame
from game_loop import GameLoop
from level import Level
from sprites.player import Player
from sprites.background import BackGround1
from sprites.background import MenuBackGround
from sprites.button import ButtonBackGround
from maps import map_1
from renderer import Renderer

from ui.menu import Menu
from ui.button import Button
from ui.menu_loop import MenuLoop


pygame.init()

display_size = (1200, 900)
drawing_surface_size = (240, 180)

drawing_surface = pygame.Surface(drawing_surface_size)
scaled_surface = pygame.Surface(display_size)

display = pygame.display.set_mode(display_size)
clock = pygame.time.Clock()

level_1 = Level(
    player=Player(5, 160),
    game_map=map_1,
    background=BackGround1()
)
game_renderer = Renderer(
    content=level_1,
    display=display,
    display_size=display_size,
    drawing_surface=drawing_surface,
    scaled_surface=scaled_surface,
)
game_loop = GameLoop(
    level=level_1,
    clock=clock,
    renderer=game_renderer,
)

start_button = Button(
    sprite=ButtonBackGround,
    x_location=140,
    y_location=120,
    on_click=game_loop.run,
    text="START",
)
quit_button = Button(
    sprite=ButtonBackGround,
    x_location=40,
    y_location=120,
    on_click=sys.exit,
    text="QUIT",
)
start_menu = Menu(
    background=MenuBackGround(),
    buttons=[start_button, quit_button],
    text="START MENU",
)

menu_renderer = Renderer(
    content=start_menu,
    display=display,
    display_size=display_size,
    drawing_surface=drawing_surface,
    scaled_surface=scaled_surface,
)
menu_loop = MenuLoop(
    menu=start_menu,
    clock=clock,
    renderer=menu_renderer,
)

menu_loop.run()
# game_loop.run()


# TODO make all this into a main loop?
class MainLoop:
    def __init__(self, start_menu, game_loop, game_renderer, menu_renderer):
        pass

import sys
import pygame
from game_loop import GameLoop
from level import Level
from sprites.player import Player
from sprites.ground import GroundTop
from sprites.background import BackGround1
from maps import map_1
from renderer import Renderer

from ui.menu import Menu
# TODO
from ui.button import Button
from ui.menu_loop import MenuLoop


display_size = (1200, 900)
drawing_surface_size = (240, 180)
drawing_surface = pygame.Surface(drawing_surface_size)
clock = pygame.time.Clock()
display = pygame.display.set_mode(display_size)
scaled_surface = pygame.Surface(display_size)

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
    sprite=GroundTop,
    x_location=10,
    y_location=10,
    on_click=game_loop.run
)
quit_button = Button(
    sprite=GroundTop,
    x_location=100,
    y_location=10,
    on_click=sys.exit
)
start_menu = Menu(
    background=BackGround1(),
    buttons=[start_button, quit_button],
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

pygame.init()
menu_loop.run()
# game_loop.run()


# TODO make all this into a main loop?
class MainLoop:
    def __init__(self, start_menu, game_loop, game_renderer, menu_renderer):
        pass

import pygame
from game_loop import GameLoop
from level import Level
from sprites.player import Player
from sprites.background import BackGround1
from maps import map_1
from renderer import Renderer


display_size = (1200, 900)

level_1 = Level(
    player=Player(5, 160),
    game_map=map_1,
    background=BackGround1()
)
clock = pygame.time.Clock()
display = pygame.display.set_mode(display_size)
drawing_surface = pygame.Surface((240, 180))
scaled_surface = pygame.Surface(display_size)

renderer = Renderer(
    content=level_1,
    display=display,
    display_size=display_size,
    drawing_surface=drawing_surface,
    scaled_surface=scaled_surface,
)

pygame.init()
GameLoop(
    level=level_1,
    clock=clock,
    renderer=renderer,
).run()

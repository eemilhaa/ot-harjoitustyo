import pygame
from game_loop import GameLoop
from level import Level
from sprites.player import Player
from maps import map_1
from sprites.background import BackGround1


level_1 = Level(
    player=Player(5, 160),
    game_map=map_1,
    background=BackGround1()
)
pygame.init()

clock = pygame.time.Clock()

display_size = (1200, 900)

display = pygame.display.set_mode(display_size)
display_surface = pygame.Surface((240, 180))

GameLoop(
    level=level_1,
    display_size=display_size,
    display=display,
    display_surface=display_surface,
    clock=clock
).run()

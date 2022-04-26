# TODO
import unittest
import pygame
from sprites.player import Player
from level import Level
from game_loop import GameLoop
# from database import DataBase
# from renderer import Renderer
from sprites.background import BackGround1


MAP_1 = [
    [0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1],
]

MAP_2 = [
    [0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1],
]
CLOCK = pygame.time.Clock

# RENDERER = Renderer()
# DATABASE = DataBase()



class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(
            player=Player(20, 10),
            game_map=MAP_1,
            background=BackGround1()
        )
        self.level_2 = Level(
            player=Player(20, 10),
            game_map=MAP_1,
            background=BackGround1()
        )
        self.game_loop = GameLoop(

        )

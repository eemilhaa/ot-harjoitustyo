# TODO
import unittest
import pygame
from sprites.player import Player
from level import Level
from game_loop import GameLoop
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


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def __init__(self):
        self.content = None

    def render(self):
        pass


class StubDataBase:
    def store_result(self, result):
        pass


class StubClock:
    def tick(self):
        pass


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

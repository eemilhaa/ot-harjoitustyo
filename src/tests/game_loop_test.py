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
    def tick(self, fps):
        pass


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(
            player=Player(20, 20),
            game_map=MAP_1,
            background=BackGround1()
        )
        self.level_2 = Level(
            player=Player(20, 20),
            game_map=MAP_1,
            background=BackGround1()
        )

    def test_level_completion(self):
        events = [
            pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_SPACE})
        ]
        game_loop = GameLoop(
            levels=[self.level_1, self.level_2],
            clock=StubClock(),
            renderer=StubRenderer(),
            event_queue=StubEventQueue(events),
            database=StubDataBase()
        )
        game_loop.run()

        self.assertTrue(self.level_1.won)

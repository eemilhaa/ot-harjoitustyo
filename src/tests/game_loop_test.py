# TODO
import unittest
import pygame
from game.sprites.player import Player
from game.level import Level
from game.game_loop import GameLoop
from game.sprites.background import BackGround


MAP_1 = [
    [0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1],
]

MAP_2 = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 0],
    [1, 1, 1, 1, 1, 1],
]

MAP_3 = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
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
            background=BackGround()
        )
        self.level_2 = Level(
            player=Player(10, 30),
            game_map=MAP_2,
            background=BackGround()
        )
        self.level_3 = Level(
            player=Player(10, 30),
            game_map=MAP_3,
            background=BackGround()
        )

    def test_level_completion(self):
        events = [
            pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_SPACE})
        ]
        game_loop = GameLoop(
            levels=[
                self.level_1,
            ],
            clock=StubClock(),
            renderer=StubRenderer(),
            event_queue=StubEventQueue(events),
            database=StubDataBase()
        )
        game_loop.run()

        self.assertTrue(self.level_1.won)

    def test_level_loss(self):
        events = [
            pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_LEFT})
        ]
        game_loop = GameLoop(
            levels=[
                self.level_1,
            ],
            clock=StubClock(),
            renderer=StubRenderer(),
            event_queue=StubEventQueue(events),
            database=StubDataBase()
        )
        game_loop.run()

        self.assertTrue(self.level_1.lost)

    def test_loop_return_value_win(self):
        events = [
            pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_SPACE})
        ]
        game_loop = GameLoop(
            levels=[
                self.level_1,
            ],
            clock=StubClock(),
            renderer=StubRenderer(),
            event_queue=StubEventQueue(events),
            database=StubDataBase()
        )
        value = game_loop.run()

        self.assertEqual(value, "game_won_menu")

    def test_loop_return_value_loss(self):
        events = [
            pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_LEFT})
        ]
        game_loop = GameLoop(
            levels=[
                self.level_1,
            ],
            clock=StubClock(),
            renderer=StubRenderer(),
            event_queue=StubEventQueue(events),
            database=StubDataBase()
        )
        value = game_loop.run()

        self.assertEqual(value, 0)

    def test_level_transition(self):
        events = [
            pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RIGHT})
        ]
        game_loop = GameLoop(
            levels=[
                self.level_2,
                self.level_3,
            ],
            clock=StubClock(),
            renderer=StubRenderer(),
            event_queue=StubEventQueue(events),
            database=StubDataBase()
        )
        game_loop.run()

        self.assertTrue(self.level_2.won and self.level_3.won)

import unittest
from sprites.player import Player
from level import Level
from sprites.background import BackGround1


MAP_1 = [
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
]


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.level = Level(
            player=Player(0, 0),
            game_map=MAP_1,
            background=BackGround1()
        )

    def test_can_move_right(self):
        collide_rects = self.level.ground
        pos1 = self.level.player.rect.x
        self.level.player.move_right(collide_rects)
        pos2 = self.level.player.rect.x
        self.assertTrue(pos1 < pos2)

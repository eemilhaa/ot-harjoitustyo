import unittest
import pygame
from sprites.player import Player
from level import Level
from sprites.background import BackGround1


MAP_1 = [
    [0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1],
]


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.level = Level(
            player=Player(20, 10),
            game_map=MAP_1,
            background=BackGround1()
        )

    def test_can_move_left(self):
        pos1 = self.level.player.rect.x
        self.level.player.move_left(self.level.ground)
        pos2 = self.level.player.rect.x
        self.assertTrue(pos1 > pos2)

    def test_can_move_right(self):
        pos1 = self.level.player.rect.x
        self.level.player.move_right(self.level.ground)
        pos2 = self.level.player.rect.x
        self.assertTrue(pos1 < pos2)

    def test_can_fall(self):
        pos1 = self.level.player.rect.y
        for _ in range(100):
            self.level.player.update_position(
                self.level.ground,
                self.level.target,
            )
        pos2 = self.level.player.rect.y
        self.assertTrue(pos1 < pos2)

    def test_can_jump(self):
        for _ in range(100):
            self.level.player.update_position(
                self.level.ground,
                self.level.target,
            )
        pos1 = self.level.player.rect.y
        self.level.player.jump()
        self.level.player.update_position(
            self.level.ground,
            self.level.target,
        )
        pos2 = self.level.player.rect.y
        self.assertTrue(pos1 > pos2)

    def test_controls_left(self):
        pos1 = self.level.player.rect.x
        event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_LEFT})
        self.level.player.controls(event)
        self.level.player.update_position(
            self.level.ground,
            self.level.target,
        )
        pos2 = self.level.player.rect.x
        self.assertTrue(pos1 > pos2)

    def test_controls_right(self):
        pos1 = self.level.player.rect.x
        event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RIGHT})
        self.level.player.controls(event)
        self.level.player.update_position(
            self.level.ground,
            self.level.target,
        )
        pos2 = self.level.player.rect.x
        self.assertTrue(pos1 < pos2)

    def test_cannot_jump_falling(self):
        self.assertEqual(self.level.player.can_jump, False)

    def test_falling_to_ground_resets_jump(self):
        # fall to ground first
        for _ in range(100):
            self.level.player.update_position(
                self.level.ground,
                self.level.target,
            )
        self.assertEqual(self.level.player.can_jump, True)

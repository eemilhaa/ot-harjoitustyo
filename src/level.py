import pygame
from sprites.ground import Ground
from sprites.ground_top import GroundTop
from sprites.target import Target


class Level:
    """A class for representing a level in the game
    

    """
    def __init__(self, player, game_map, background):
        self.player = player

        self.game_map = game_map

        self.background = background

        self.ground = pygame.sprite.Group()
        self.target = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.won = False
        self.lost = False

        # build and group automatically
        self._build_map()
        self._group_sprites()

    def _build_map(self):
        row_number = 0
        for row in self.game_map:
            column_number = 0
            for tile in row:
                if tile == 1:
                    self.ground.add(
                        GroundTop(
                            column_number*10,
                            row_number*10,
                        )
                    )
                if tile == 2:
                    self.ground.add(
                        Ground(
                            column_number*10,
                            row_number*10,
                        )
                    )
                if tile == 3:
                    self.target.add(
                        Target(
                            column_number*10,
                            row_number*10,
                        )
                    )
                column_number += 1
            row_number += 1

    def _group_sprites(self):
        self.all_sprites.add(
            self.background,
            self.ground,
            self.target,
            self.player,
        )

    def update(self):
        self.player.update_position(
            self.ground,
            self.target
        )
        if self.player.rect.y > 180:
            self.lost = True
        if self.player.won:
            self.won = True

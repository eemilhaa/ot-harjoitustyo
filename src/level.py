import pygame
from sprites.ground import Ground, GroundTop


class Level:
    def __init__(self, player, game_map, background):
        self.player = player

        self.game_map = game_map
        self.tilesize = 10

        self.background = background

        self.ground = pygame.sprite.Group()
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
                            column_number*self.tilesize,
                            row_number*self.tilesize,
                        )
                    )
                if tile == 2:
                    self.ground.add(
                        Ground(
                            column_number*self.tilesize,
                            row_number*self.tilesize,
                        )
                    )
                column_number += 1
            row_number += 1

    def _group_sprites(self):
        self.all_sprites.add(
            self.background,
            self.ground,
            self.player,
        )

    def update(self):
        self.player.update_position(
            self.ground
        )
        if self.player.rect.y > 180:
            self.lost = True
        if self.player.rect.y < 0:
            self.won = True

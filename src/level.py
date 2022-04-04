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

        # build and group automatically
        self._build_map()
        self._group_sprites()

    def _build_map(self):
        y = 0
        for row in self.game_map:
            x = 0
            for tile in row:
                # Add a collideable rect for every 1
                if tile == 1:
                    self.ground.add(
                        GroundTop(
                            x*self.tilesize,
                            y*self.tilesize,
                        )
                    )
                if tile == 2:
                    self.ground.add(
                        Ground(
                            x*self.tilesize,
                            y*self.tilesize,
                        )
                    )
                x += 1
            y += 1

    def _group_sprites(self):
        self.all_sprites.add(
            self.background,
            self.ground,
            self.player,
        )

#    def _create_sprite(self, tile):
#        if tile == 1:
#            sprite

    def update(self):
        self.player.move(
            self.ground
        )

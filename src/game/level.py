import pygame
from game.sprites.ground import Ground
from game.sprites.ground_top import GroundTop
from game.sprites.target import Target


class Level:
    """A class for representing a level in the game

    The level class is most importantly responsible for providing a sprite
    group with all the sprites of the game and an update function to keep
    track of the level's state

    Attributes:
        player: A Player object
        game_map: A 2-dimensional array that represents a level's map
        background: A sprite that is drawn as a backround image
        ground: A sprite group that holds all sprites the player can collide
        with
        target: A sprite group for the target sprite
        all_sprites: A sprite group for hosting all sprites
        won: Is the level won
        lost: Is the level lost
    """

    def __init__(self, player, game_map, background):
        """Inits the level and sprite groups

        Args:
            player: A Player object
            game_map: A 2-dimensional array that represents a level's map
            background: A sprite that is drawn as a backround image
        """

        self.player = player
        self.game_map = game_map
        self.background = background

        self.ground = pygame.sprite.Group()
        self.target = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.won = False
        self.lost = False

        # build and group automatically when creating a level
        self._build_map()
        self._group_sprites()

    def _build_map(self):
        """A function for building the map of a level

        The map building is done with a for loop nested within another for
        loop. The outer loop loops the rows of the map array (lists) while the
        nested loop loops the columns (list items). Each item is looped over,
        and a sprite is constructed based on the value. The sprites are then
        added to their respective sprite groups.
        """

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
        """Groups all sprite groups to one single group

        This is done to make rendering a level easier
        """

        self.all_sprites.add(
            self.background,
            self.ground,
            self.target,
            self.player,
        )

    def update(self):
        """Updates the level and keeps track if it is won or lost

        In practice this means updating the players position and keeping track
        if the player has lost (fallen down) or won (reached the target).
        """
        self.player.update_position(
            self.ground,
            self.target
        )
        if self.player.rect.y > 180:
            self.lost = True
        if self.player.won:
            self.won = True

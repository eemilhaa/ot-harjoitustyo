import pygame
# from sprites.ground import Ground, GroundTop


class Menu:
    def __init__(self, background, button):

        self.background = background
        self.button = button
        self.all_sprites = pygame.sprite.Group()

        # build and group automatically
        self._group_sprites()

    def _group_sprites(self):
        self.all_sprites.add(
            self.background,
            self.button.sprite,
        )

    def update(self):
        pass

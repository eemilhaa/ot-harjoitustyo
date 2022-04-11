import pygame
# from sprites.ground import Ground, GroundTop


class Menu:
    def __init__(self, background):

        self.background = background
        self.buttons = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        # build and group automatically
        self._group_sprites()

    def _group_sprites(self):
        self.all_sprites.add(
            self.background,
            self.buttons,
        )

    def update(self):
        pass

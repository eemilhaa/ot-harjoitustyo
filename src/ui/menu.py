import pygame
# from sprites.ground import Ground, GroundTop


class Menu:
    def __init__(self, background, buttons: list):

        self.background = background
        self.buttons = buttons
        self.all_sprites = pygame.sprite.Group()

        # build and group automatically
        self._group_sprites()

    def _group_sprites(self):
        for button in self.buttons:
            self.all_sprites.add(
                button.sprite,
            )

    def update(self):
        pass

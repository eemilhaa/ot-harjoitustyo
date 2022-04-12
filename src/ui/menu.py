import pygame


class Menu:
    def __init__(self, background, buttons: list, text=None):

        self.background = background
        self.buttons = buttons
        self.all_sprites = pygame.sprite.Group()

        if text:
            image = self.background.image.copy()
            self.write(image=image, text=text)
        # build and group automatically
        self._group_sprites()

    def _group_sprites(self):
        for button in self.buttons:
            self.all_sprites.add(
                self.background,
                button.sprite,
            )

    def update(self):
        pass

    # TODO make into a global function
    def write(self, image, text):
        """write text on the menu"""

        color = (255, 255, 255)
        textsurface = pygame.font.SysFont(
            "Arial", 12).render(text, True, color)
        textrect = textsurface.get_rect(center=image.get_rect().center)
        image.blit(textsurface, textrect)
        self.background.image = image

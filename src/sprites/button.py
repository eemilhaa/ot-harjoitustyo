import pygame
from image_loader import load_image


class ButtonBackGround(pygame.sprite.Sprite):
    def __init__(self, x_location, y_location):
        super().__init__()

        self.image = load_image("button_background.png")

        self.rect = self.image.get_rect()
        self.rect.x = x_location
        self.rect.y = y_location
import pygame
from image_loader import load_image


class BackGround1(pygame.sprite.Sprite):
    def __init__(self, x_location=0, y_location=0):
        super().__init__()
        self.image = load_image("background_1.png")

        self.rect = self.image.get_rect()
        self.rect.x = x_location
        self.rect.y = y_location

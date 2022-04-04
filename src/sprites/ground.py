import pygame
from image_loader import load_image


class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = load_image("ground.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class GroundTop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = load_image("ground_top.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

import pygame
from image_loader import load_image


class BackGround1(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.image = load_image("background_1.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# More backrounds here?
#class BackGround2(pygame.sprite.Sprite):
#    def __init__(self, x=0, y=0):
#        super().__init__()
#        self.image = load_image("background_2.png")
#
#        self.rect = self.image.get_rect()
#        self.rect.x = x
#        self.rect.y = y

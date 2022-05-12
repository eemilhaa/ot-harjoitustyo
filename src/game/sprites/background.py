import pygame
from loaders.image_loader import load_image


class BackGround(pygame.sprite.Sprite):
    """A sprite class to implement a backround for the game.

    Attributes:
        image: A image to visually represent the sprite in the game
        rect: A pygame Rect object to represent the bounds of the sprite
        x_location: the location on the x axis to which the sprite gets drawn
        y_location: the location on the y axis to which the sprite gets drawn
    """

    def __init__(self, x_location=0, y_location=0):
        """Inits the class.

        Args:
            x_location: the location on the x axis to which the sprite gets
            drawn (use the default as a background completely fills the screen)
            y_location: the location on the y axis to which the sprite gets
            drawn (use the default as a background completely fills the screen)
        """
        super().__init__()
        self.image = load_image("background_1.png")

        self.rect = self.image.get_rect()
        self.rect.x = x_location
        self.rect.y = y_location

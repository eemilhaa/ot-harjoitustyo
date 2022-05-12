import pygame
from loaders.image_loader import load_image


class Ground(pygame.sprite.Sprite):
    """A sprite class to represent ground tiles in the game.

    Attributes:
        image: A image to visually represent the sprite in the game
        rect: A pygame Rect object to represent the bounds of the sprite
        x_location: the location on the x axis to which the sprite gets drawn
        y_location: the location on the y axis to which the sprite gets drawn
    """

    def __init__(self, x_location, y_location):
        """Inits the class.

        Args:
            x_location: the location on the x axis to which the sprite gets
            drawn
            y_location: the location on the y axis to which the sprite gets
            drawn
        """
        super().__init__()
        self.image = load_image("ground.png")

        self.rect = self.image.get_rect()
        self.rect.x = x_location
        self.rect.y = y_location

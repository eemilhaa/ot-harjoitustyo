import os
import pygame


def load_image(filename):
    """A function for loading images

    Args:
        filename: The name of the image file to load

    Returns:
        A pygame Surface object that can be drawn to the screen
    """

    dirname = os.path.dirname(__file__)

    return pygame.image.load(
        os.path.join(
            dirname,
            "..",
            "assets",
            "img",
            filename,
        )
    )

import os
import pygame


def load_image(filename):
    """A function for loading images
    
    Args:
        filename: The name of the image file to load

    Returns:
        A pygame image.load() function call with the desired image
    """

    dirname = os.path.dirname(__file__)
    return pygame.image.load(
        os.path.join(
            dirname,
            "img",
            filename,
        )
    )

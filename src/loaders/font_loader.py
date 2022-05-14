import os
import pygame


def load_font(filename: str, fontsize: int):
    """A function for loading a font.

    Args:
        filename: The name of the font file to load (normal or bold)
        fontsize: The desired fontsize

    Returns:
        A pygame font object that is used to render text to the screen
    """

    dirname = os.path.dirname(__file__)

    return pygame.font.Font(
        os.path.join(
            dirname,
            "..",
            "assets",
            "font",
            filename,
        ),
        fontsize
    )

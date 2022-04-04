import pygame
import os


def load_image(filename):
    dirname = os.path.dirname(__file__)
    return pygame.image.load(
        os.path.join(
            dirname,
            # "..",
            "img",
            filename,
        )
    )


import os
import pygame


def load_font(filename, fontsize):
    dirname = os.path.dirname(__file__)
    return pygame.font.Font(
        os.path.join(
            dirname,
            # "..",
            "font",
            filename,
        ),
        fontsize
    )

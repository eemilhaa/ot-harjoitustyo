import pygame
from font_loader import load_font


def write(
    surface,
    string,
    position,
    color,
    font,
    size,
):
    """write text to the display"""

    font = load_font(font, size)
    text = font.render(string, True, color)
    surface.blit(text, position)

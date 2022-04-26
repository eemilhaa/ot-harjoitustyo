from font_loader import load_font


def write(
    surface,
    string,
    position,
    color,
    font,
    fontsize,
):
    """write text to the display"""

    font = load_font(font, fontsize)
    text = font.render(string, True, color)
    surface.blit(text, position)

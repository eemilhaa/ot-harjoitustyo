from font_loader import load_font


def write(
    surface,
    string,
    position,
    color,
    font,
    fontsize,
):
    """A function for writing text to the display

    Args:
        surface: The surface on which the text is drawn
        string: The content of the text
        position: Where on the screen the text is drawn
        color: The color of the text
        font: Name of font file to load (bold or regular)
        fontsize: The size of the font
    """

    font = load_font(font, fontsize)
    text = font.render(string, True, color)
    surface.blit(text, position)

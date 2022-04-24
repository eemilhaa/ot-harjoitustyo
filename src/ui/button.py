from font_loader import load_font


# TODO add support for any type of on-click functions
class Button:
    """A class for implementing buttons.

    A button consists of a sprite backround, text and a reference to a
    function. When the user clicks the button the function gets executed.
    """

    def __init__(self, sprite, x_location, y_location, on_click, text=None):
        """The constructor"""

        self.sprite = sprite(x_location, y_location)
        self.on_click = on_click
        if text:
            image = self.sprite.image.copy()
            self.write_text(image=image, text=text)

    def click(self):
        self.on_click()

    # TODO make into a global function
    def write_text(self, image, text):
        """write text on the button"""

        color = (255, 255, 255)

        font = load_font("regular.ttf", 12)
        textsurface = font.render(text, True, color)
        textrect = textsurface.get_rect(center=image.get_rect().center)
        image.blit(textsurface, textrect)
        self.sprite.image = image

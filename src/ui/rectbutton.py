import pygame


# TODO add support for any type of on-click functions
class RButton:
    """A class for implementing buttons.

    A button consists of a sprite backround, text and a reference to a
    function. When the user clicks the button the function gets executed.
    """

    def __init__(
        self,
        x_location,
        y_location,
        color,
        on_click,
        width,
        text=None,
    ):
        """The constructor"""

        self.x_location = x_location
        self.y_location = y_location
        self.rect = pygame.Rect(x_location, y_location, width, width/2)
        self.on_click = on_click
        self.text = text
        self.color = color

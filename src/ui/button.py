import pygame


# TODO docstrings
class Button:
    """A class for implementing buttons

    A button consists of a rect, text and a reference to a function. When the
    user clicks the button the function gets executed.
    """

    def __init__(
        self,
        location,
        color,
        on_click,
        width,          #
        text=None,
    ):
        """The constructor"""

        self.x_location = location[0]
        self.y_location = location[1]
        self.rect = pygame.Rect(
            self.x_location,
            self.y_location,
            width,
            width/2
        )
        self.on_click = on_click
        self.text = text
        self.color = color

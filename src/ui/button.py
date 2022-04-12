# TODO add support for any type of on-click functions
class Button:
    """A class for implementing buttons.

    A button consists of a sprite and a reference to a function. When the
    user presses the button the function.
    """

    def __init__(self, sprite, x_location, y_location, on_click):
        """The constructor"""

        self.sprite = sprite(x_location, y_location)
        self.on_click = on_click

    def on_click(self):
        """what happens when the button is pressed."""

        self.on_click()

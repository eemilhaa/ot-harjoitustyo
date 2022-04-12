import sys
import pygame


# TODO add support for any type of on-click functions
class Button:
    """A class for implementing buttons.

    A button consists of a sprite and a target loop. When the
    user presses the button the target loop gets executed.
    """

    def __init__(self, sprite, x_location, y_location, target_loop=None):
        """The constructor"""

        self.sprite = sprite(x_location, y_location)
        self.target_loop = target_loop

    def on_click(self):
        """what happens when the button is pressed.

        Leaving target loop empty results in a quit button
        """

        if not self.target_loop:
            sys.exit()
        self.target_loop.run()

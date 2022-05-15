import pygame


class Button:
    """A class for implementing buttons

    A button consists of a rect, text and a reference to a function. When the
    user clicks the button the function gets executed.

    Attributes:
        location: The location on the screen to draw the button in
        rect: A rect to represent the button and to check for clicks
        color: The color of the button
        on_click: The function that gets executed when the button is clicked
        width: The width of the button in pixels
        text: The text that gets written on the button
    """

    def __init__(
        self,
        location,
        color,
        on_click,
        width,
        text,
    ):
        """Inits the button

        Args:
            location: The location on the screen to draw the button in
            color: The color of the button
            on_click: The function that gets executed when the button is
            clicked
            width: The width of the button in pixels
            text: The text that gets written on the button
        """

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

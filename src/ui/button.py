import pygame


# TODO this could be a sprite
class Button:
    def __init__(self, sprite, x_location, y_location, target_loop):
        self.sprite = sprite(x_location, y_location)
        self.target_loop = target_loop

    def click(self):
        self.target_loop.run()

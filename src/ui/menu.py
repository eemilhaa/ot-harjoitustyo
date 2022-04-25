import pygame


class Menu:
    def __init__(self, background, buttons: list, text=None):

        self.background = background
        self.buttons = buttons
        self.text = text

import pygame


class EventQueue:
    """An abstraction class for getting pygame events"""

    def get(self):
        """A method for getting the events"""
        return pygame.event.get()

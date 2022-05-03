import pygame


class Clock:
    """An abstraction class for the pygame clock

    Attributes:
        clock: A pygame.time.Clock object
    """

    def __init__(self):
        """Inits Clock with a pygame clock"""
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """Uses the clock with the given fps value"""
        self._clock.tick(fps)

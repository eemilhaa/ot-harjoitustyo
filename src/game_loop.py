import sys
import pygame


class GameLoop:
    def __init__(
        self,
        level,
        clock,
        renderer
    ):
        self.level = level
        self.clock = clock
        self.renderer = renderer

    def run(self):
        while True:
            self.handle_events()

            self.renderer.render()

            self.clock.tick(60)

    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.level.player.controls(event)

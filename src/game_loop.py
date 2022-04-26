import sys
import pygame


class GameLoop:
    def __init__(
        self,
        levels,
        clock,
        renderer,
        database,
    ):
        self.levels = levels
        self.clock = clock
        self.renderer = renderer
        self.database = database

    def run(self):
        count = None
        for count, level in enumerate(self.levels):
            self.renderer.content = level
            while True:
                self._handle_events(level)

                level.update()

                if level.lost:
                    result_level = count
                    break

                if level.won:
                    result_level = count + 1
                    break

                self.renderer.render()

                self.clock.tick(60)
            if level.lost:
                break

        self.database.store_result(result_level)
        return count
        # Continue to next level if won (no break)

    def _handle_events(self, level):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            level.player.controls(event)

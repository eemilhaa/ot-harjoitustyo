import sys
import pygame


class GameLoop:
    def __init__(self, level, display_size, display_surface, display, clock):
        self.level = level
        self.display_size = display_size
        self.display = display
        self.display_surface = display_surface
        self.clock = clock

    def run(self):
        while True:
            self.handle_events()

            self.render()

            self.clock.tick(60)

    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.level.player.controls(event)

    # Make into own class?
    def render(self):
        self.level.update()

        self.level.all_sprites.draw(self.display_surface)

        # Use two surfaces to scale up pixels
        scaling_surface = pygame.transform.scale(
            self.display_surface,
            self.display_size,
        )
        self.display.blit(scaling_surface, (0, 0))
        pygame.display.update()

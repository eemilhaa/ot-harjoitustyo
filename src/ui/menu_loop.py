import sys
import pygame
from writer import write


class MenuLoop:
    def __init__(
        self,
        menu,
        clock,
        renderer=None
    ):

        self.display_size = (1200, 900)
        self.display = pygame.display.set_mode(self.display_size)

        self.menu = menu
        self.clock = clock
        self.renderer = renderer

    def run(self):
        while True:
            self._handle_events()

            self.menu.update()

            # self.renderer.render()
            self.display.fill(self.menu.background)
            self.menu.all_sprites.draw(self.display)    # TODO
            
            # Draw buttons TODO make into separate method
            for button in self.menu.buttons:
                # https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
                pygame.draw.rect(
                    surface=self.display,
                    color=button.color,
                    rect=button.rect
                )
                write(
                    surface=self.display,
                    string=button.text,
                    position=(button.x_location, button.y_location),
                    color=(255, 255, 255),              # TODO
                    font="regular.ttf",
                    size=40,                            # TODO
                )

            # menu.text.draw

            self.display.blit(self.display, (0, 0))
            pygame.display.update()

            self.clock.tick(60)

    def _handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # click_location = self.transform_click_location(event.pos)
                for button in self.menu.buttons:
                    if button.rect.collidepoint(event.pos):
                        button.on_click()

    # TODO maybe switch to using native resolution for menus?
    def transform_click_location(self, click_location: tuple):
        # TODO remove hardcoding if this stays
        return tuple(i/5 for i in click_location)

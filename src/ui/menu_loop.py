import sys
import pygame


class MenuLoop:
    def __init__(
        self,
        menu,
        clock,
        renderer,
    ):
        self.menu = menu
        self.clock = clock
        self.renderer = renderer

    def run(self):
        while True:
            self._handle_events()

            self.menu.update()

            self.renderer.render()

            self.clock.tick(60)

    def _handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_location = self.transform_click_location(event.pos)
                for button in self.menu.buttons:
                    if button.sprite.rect.collidepoint(click_location):
                        button.on_click()

    # TODO maybe switch to using native resolution for menus?
    def transform_click_location(self, click_location: tuple):
        # TODO remove hardcoding if this stays
        return tuple(i/5 for i in click_location)

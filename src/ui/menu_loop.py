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
            # TODO detect click on button
#            if event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_0:
#                    self.menu.buttons[0].on_click()
#                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_location = self.transform_click_location(event.pos)
                for button in self.menu.buttons:
                    print(type(button.sprite.rect))
                    print(button.sprite.rect.x)
                    print(click_location)
                    print(type(click_location))
                    if button.sprite.rect.collidepoint(click_location):
                        button.on_click()

    def transform_click_location(self, click_location: tuple):
        return tuple(i/5 for i in click_location)

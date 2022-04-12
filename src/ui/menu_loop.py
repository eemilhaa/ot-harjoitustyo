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
                for button in self.menu.buttons:
                    print(type(button.sprite.rect))
                    print(button.sprite.rect.x)
                    print(event.pos)
                    if button.sprite.rect.collidepoint(event.pos):
                        button.on_click()

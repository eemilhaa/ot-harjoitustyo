import sys
import pygame
from writer import write


class MenuLoop:
    def __init__(
        self,
        display,
        menus,
        clock,
    ):

        self.display = display

        self.menus = menus
        self.menu = menus["start"]
        self.clock = clock
        self.fontsize = int(display.get_width() * 0.05)

    def run(self):
        while True:
            self._handle_events()

            self.display.fill(self.menu.background)

            self.draw_buttons()
            self.draw_text()

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
                        click_result = button.on_click()
                        print(click_result)
                        if click_result == 0:
                            self.menu = self.menus["controls"]
                        if type(click_result) == str:
                            self.menu = self.menus[click_result]

    def draw_buttons(self):
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
                font="bold.ttf",
                fontsize=self.fontsize,             # TODO
            )

    def draw_text(self):
        y_location = 0
        for line in self.menu.text:
            write(
                surface=self.display,
                string=line,
                position=(0, y_location),
                color=(200, 200, 205),
                font="regular.ttf",
                fontsize=self.fontsize
            )
            y_location += self.fontsize

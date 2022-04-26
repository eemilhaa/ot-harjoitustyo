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
                for button in self.menu.buttons:
                    if button.rect.collidepoint(event.pos):
                        self.use_button(button=button)

    def use_button(self, button):

        click_result = button.on_click()
        # Navigation buttons return the key of the target menu (str)
        if type(click_result) == str:
            self.menu = self.menus[click_result]
        # the game loop returns the number of the level to which the player got
        # to (int)
        elif type(click_result) == int:
            self.menu = self.menus["game_over"]
            self.menu.text = [
                "GAME OVER",
                "",
                f"You got to level {click_result + 1}"
            ]

    def draw_buttons(self):

        for button in self.menu.buttons:
            pygame.draw.rect(
                surface=self.display,
                color=button.color,
                rect=button.rect
            )
            write(
                surface=self.display,
                string=button.text,
                position=(button.x_location, button.y_location),
                color=(255, 255, 255),
                font="bold.ttf",
                fontsize=self.fontsize,
            )

    def draw_text(self):

        y_location = 0
        for line in self.menu.text:
            write(
                surface=self.display,
                string=line,
                position=(0, y_location),
                color=(200, 200, 200),
                font="regular.ttf",
                fontsize=self.fontsize
            )
            y_location += self.fontsize

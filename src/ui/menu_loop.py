import sys
import pygame
from writer import write


class MenuLoop:
    def __init__(
        self,
        display,
        menus,
        clock,
        database,
    ):
        """Sets up the menu loop"""

        self.display = display
        self.menus = menus
        self.menu = menus["start"]
        self.clock = clock
        self.fontsize = int(display.get_width() * 0.05)
        self.database = database

    def run(self):
        """Checks events, draws everything in the current menu"""

        while True:
            self._handle_events()

            self.display.fill(self.menu.background)

            self.draw_buttons()
            self.draw_text()

            self.display.blit(self.display, (0, 0))
            pygame.display.update()

            self.clock.tick(60)

    def _handle_events(self):
        """Checks for quitting and button presses"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.menu.buttons:
                    if button.rect.collidepoint(event.pos):
                        self.use_button(button=button)

    def use_button(self, button):
        """Decides the next menu based what the clicked button returns"""

        click_result = button.on_click()
        # Navigation buttons return the key of the target menu (str)
        if type(click_result) == str:
            target_menu = click_result
        # the game loop returns the number of the level to which the player got
        # to (int)
        elif type(click_result) == int:
            target_menu = "game_over"

        # Update menus on click
        self.update_menus(click_result, target_menu)

    def update_menus(self, click_result, target_menu):
        """Updates all menus with dynamic content"""

        if type(click_result) == int:
            self.menus["game_over"].text = [
                "GAME OVER",
                "",
                f"You got to level {click_result + 1}",
            ]
        self.menus["stats"].text = [
            "STATS",
            "",
            f"Levels completed: {self.database.query_highscore()}",
            f"Total tries: {self.database.query_number_of_runs()}",
        ]
        self.menu = self.menus[target_menu]

    def draw_buttons(self):
        """Draws a menu's buttons"""

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
        """Draws a menu's text"""

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
            y_location += self.fontsize * 1.2

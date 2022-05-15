import sys
import pygame
from ui.writer import write


class MenuLoop:
    """A class for running the menus.

    Running in this context means checking for clicks on the buttons, handling
    navigation between menus, updating menus and displaying the menus to the
    user.

    Attributes:
        display: A pygame Surface object to draw on
        menus: A dict of menu objects
        database: A DataBase object
    """

    def __init__(
        self,
        display,
        menus,
        database,
    ):
        """Inits the MenuLoop

        Args:
            display: A pygame Surface object to draw on
            menus: A dict of menu objects
            database: A DataBase object
        """

        self.display = display
        self.menus = menus
        self.menu = menus["start_menu"]
        self.clock = pygame.time.Clock()
        self.fontsize = int(display.get_width() * 0.05)
        self.database = database

    def run(self):
        """The main menu loop.

        The run loop checks for events, draws everything in the current menu
        and handles navigation between menus.
        """

        while True:
            self._handle_events()

            self.display.fill(self.menu.background)

            self._draw_buttons()
            self._draw_text()

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
                        self._use_button(button=button)

    def _use_button(self, button):
        """A method for using buttons.

        In practice this means executing the buttons on_click function, and
        Deciding the next menu based on what the function returns. on_click
        functions return the key of the target menu (str), the exception being
        the game_loop.run() call.

        Args:
            button: A button to click
        """

        target_menu = None
        click_result = button.on_click()
        if type(click_result) == str:
            target_menu = click_result
        # A lost game_loop returns the count of the level
        elif type(click_result) == int:
            target_menu = "game_over_menu"

        # Update menus on click
        self._update_menus(click_result, target_menu)

    def _update_menus(self, click_result, target_menu):
        """Updates the menu view and all menus with dynamic content

        Args:
            click_result: Result of the button click that caused the update
            target_menu: The menu to display next
        """

        if type(click_result) == int:
            self.menus["game_over_menu"].text = [
                "GAME OVER",
                "",
                f"You got to level {click_result + 1}",
            ]
        self.menus["stats_menu"].text = [
            "STATS",
            "",
            f"Levels completed: {self.database.query_highscore()}",
            f"Total tries: {self.database.query_number_of_runs()}",
        ]
        if target_menu:
            self.menu = self.menus[target_menu]

    def _draw_buttons(self):
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

    def _draw_text(self):
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

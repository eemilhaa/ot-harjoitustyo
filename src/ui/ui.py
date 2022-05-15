import sys
from ui.menu import Menu
from ui.button import Button
from ui.menu_loop import MenuLoop


class UI:
    """A class for constructing the UI.

    The purpose here is to have all code related to generating the UI
    components in one place. It exists only to produce a functional MenuLoop
    with the desired menus and buttons.

    Attributes (only for eventually passing them to the MenuLoop):
        display: A pygame Surface object
        database: A DataBase object
        game_start_function: A special on click function for entering the game
        loop
    """

    def __init__(self, display, database, game_start_function):
        """Inits the UI constructing process

        Args:
            display: A pygame Surface object
            database: A DataBase object
            game_start_function: A special on click function for entering the
            game loop
        """

        self.display = display
        self.database = database
        self.game_start_function = game_start_function
        self._create_buttons()
        self._create_menus()
        self._create_menu_loop()

    def _create_buttons(self):
        """All buttons are created here"""

        self._calculate_button_locations()
        self.buttons = {
            "start_game": Button(
                location=self.button_locations["bottom_right"],
                color=(100, 200, 100),
                text="START",
                width=self.button_width,
                on_click=self.game_start_function,
            ),
            "retry": Button(
                location=self.button_locations["bottom_right"],
                color=(100, 200, 100),
                text="RETRY",
                width=self.button_width,
                on_click=self.game_start_function,
            ),
            "quit": Button(
                location=self.button_locations["bottom_left"],
                color=(255, 100, 100),
                text="QUIT",
                width=self.button_width,
                on_click=sys.exit,
            ),
            "controls": Button(
                location=self.button_locations["top_right"],
                color=(255, 150, 100),
                text="CONTROLS",
                width=self.button_width,
                on_click=self.to_controls_menu,
            ),
            "start_menu": Button(
                location=self.button_locations["top_left"],
                color=(255, 150, 100),
                text="BACK",
                width=self.button_width,
                on_click=self.to_start_menu,
            ),
            "stats_menu": Button(
                location=self.button_locations["top_left"],
                color=(255, 150, 100),
                text="STATS",
                width=self.button_width,
                on_click=self.to_stats_menu,
            ),
            "reset_stats": Button(
                location=self.button_locations["top_right"],
                color=(255, 100, 100),
                text="RESET",
                width=self.button_width,
                on_click=self.database.reset_database,
            )
        }

    def _calculate_button_locations(self):
        """A function to calculate button locations more cleanly"""

        display_width, display_height = self.display.get_size()
        self.button_width = display_width / 4
        self.button_locations = {
            "top_left": (
                self.button_width*0.5,
                display_height-self.button_width*1.5
            ),
            "top_right": (
                display_width-self.button_width*1.5,
                display_height-self.button_width*1.5,
            ),
            "bottom_left": (
                self.button_width*0.5,
                display_height-self.button_width*0.75,
            ),
            "bottom_right": (
                display_width-self.button_width*1.5,
                display_height-self.button_width*0.75,
            )
        }

    def _create_menus(self):
        """All menus are created here"""

        self.menus = {
            "start_menu": Menu(
                buttons=[
                    self.buttons["start_game"],
                    self.buttons["quit"],
                    self.buttons["controls"],
                    self.buttons["stats_menu"],
                ],
                text=[
                    "START MENU",
                    "",
                    "click the buttons to advance"
                ],
                background=(54, 54, 70),
            ),
            "controls_menu": Menu(
                buttons=[
                    self.buttons["start_menu"],
                ],
                text=[
                    "CONTROLS",
                    "",
                    "LEFT ARROW --- LEFT",
                    "RIGHT ARROW -- RIGHT",
                    "SPACE -------- JUMP",
                ],
                background=(70, 70, 70),
            ),
            "game_over_menu": Menu(
                buttons=[
                    self.buttons["retry"],
                    self.buttons["quit"],
                    self.buttons["start_menu"],
                ],
                text=[],  # This is set in the menu loop based on game outcome
                background=(100, 50, 50),
            ),
            "stats_menu": Menu(
                buttons=[
                    self.buttons["start_menu"],
                    self.buttons["reset_stats"],
                ],
                text=[],
                background=(70, 70, 70),
            ),
            "game_won_menu": Menu(
                buttons=[
                    self.buttons["quit"],
                    self.buttons["start_menu"],
                ],
                text=[
                    "GAME WON",
                    "",
                    "You beat all the levels!"
                ],
                background=(50, 100, 50),
            )
        }

    def _create_menu_loop(self):
        """The menu loop is created here"""

        self.menu_loop = MenuLoop(
            menus=self.menus,
            display=self.display,
            database=self.database,
        )

    # on_click functions for simple menu-to-menu navigation
    def to_start_menu(self):
        """Returns the dict key of the start menu"""

        return "start_menu"

    def to_controls_menu(self):
        """Returns the dict key of the controls menu"""

        return "controls_menu"

    def to_stats_menu(self):
        """Returns the dict key of the stats menu"""

        return "stats_menu"

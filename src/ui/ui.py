import sys
from ui.menu import Menu
from ui.button import Button
from ui.menu_loop import MenuLoop


class UI:
    # TODO docstrings
    """A class for constructing the UI."""

    def __init__(self, display, clock, database, game_start_function):
        self.display = display
        self.clock = clock
        self.database = database
        self.game_start_function = game_start_function
        self._create_buttons()
        self._create_menus()
        self._create_menu_loop()

    def _create_buttons(self):
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
            )
        }

    def _calculate_button_locations(self):
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
        self.menus = {
            "start_menu": Menu(
                background=(54, 54, 70),
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
            ),
            "controls_menu": Menu(
                background=(70, 70, 70),
                buttons=[
                    self.buttons["start_menu"],
                ],
                text=[
                    "CONTROLS",
                    "",
                    "LEFT ARROW --- LEFT",
                    "RIGHT ARROW -- RIGHT",
                    "SPACE -------- JUMP",
                ]
            ),
            "game_over_menu": Menu(
                background=(100, 50, 50),
                buttons=[
                    self.buttons["retry"],
                    self.buttons["quit"],
                    self.buttons["start_menu"],
                ],
                text=[]  # This is set in the menu loop based on game outcome
            ),
            "stats_menu": Menu(
                background=(70, 70, 70),
                buttons=[
                    self.buttons["start_menu"],
                ],
                text=[]
            ),
            "game_won_menu": Menu(
                background=(50, 100, 50),
                buttons=[
                    self.buttons["quit"],
                    self.buttons["start_menu"],
                ],
                text=[
                    "GAME WON",
                    "",
                    "You beat all the levels!"
                ]
            )
        }

    def _create_menu_loop(self):
        self.menu_loop = MenuLoop(
            menus=self.menus,
            clock=self.clock,
            display=self.display,
            database=self.database,
        )

    def to_start_menu(self):
        """Returns the dict key of the start menu"""

        return "start_menu"

    def to_controls_menu(self):
        """Returns the dict key of the controls menu"""

        return "controls_menu"

    def to_stats_menu(self):
        """Returns the dict key of the stats menu"""

        return "stats_menu"

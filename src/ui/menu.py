class Menu:
    """A class for implementing menus

    A menu consists of buttons, text and a background. The buttons provide the
    menu with functionality, and the text is the textual content of the menu.
    The backround is the color of the menu's backround.

    Attributes:
        buttons: A list of Button objects
        text: A list of strings, each string is written on its own line.
        backround: The RGB value of the menu's backround color
    """

    def __init__(self, buttons: list, text: list, background: tuple):
        """Inits the menu

        Args:
            buttons: A list of Button objects
            text: A list of strings, each string is written on its own line.
            backround: The RGB value of the menu's backround color
        """

        self.buttons = buttons
        self.text = text
        self.background = background

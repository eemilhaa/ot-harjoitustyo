import pygame


class Renderer:
    """A class for rendering content to the screen.

    The renderer takes content which it then scales up to the correct display
    size and renders to the display. This makes the pixelated look of the game
    happen.

    Attributes:
        display: the display to which the content should be rendered on
        content: The content to render to the screen. For example a level.
    """

    def __init__(
        self,
        display,
        content=None,
    ):
        """Inits the Renderer.

        Args:
            display: the display to which the content should be rendered on.
            content: The content to render to the screen. For example a level.
        """

        self.content = content
        self.display = display
        self.display_size = display.get_size()
        self.drawing_surface = pygame.Surface((240, 180))
        self.scaled_surface = pygame.Surface(self.display_size)

    def render(self):
        """Renders everything in the game.

        Everything is first drawn onto the small drawing surface that is always
        sized 240x180 pixels. This small surface with everything drawn onto it
        is then scaled up to whatever displaysize and drawn to the full-sized
        display.
        """

        self.content.all_sprites.draw(self.drawing_surface)

        self._scale()

        self.display.blit(self.scaled_surface, (0, 0))
        pygame.display.update()

    def _scale(self):
        """scales drawing_surface to the size of the display."""

        pygame.transform.scale(
            self.drawing_surface,
            self.display_size,
            self.scaled_surface,
        )

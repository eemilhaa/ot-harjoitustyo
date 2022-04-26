import pygame


class Renderer:
    """A class for rendering content to the screen."""

    def __init__(
        self,
        display,
        drawing_surface,
        scaled_surface,
        # Default to None so renderer can be called in a loop with dynamic
        # content
        content=None,
    ):
        # TODO
        """The constructor.

        Args:
            content:
            display:
            display_size:
            scaled_surface:
        """
        self.content = content
        self.display = display
        self.display_size = display.get_size()
        self.drawing_surface = drawing_surface
        self.scaled_surface = scaled_surface

    def render(self):
        """Renders everything in the game."""

        self.content.all_sprites.draw(self.drawing_surface)

        self._scale()

        self.display.blit(self.scaled_surface, (0, 0))
        pygame.display.update()

    def _scale(self):
        """scales drawing_surface to the size of display"""

        pygame.transform.scale(
            self.drawing_surface,
            self.display_size,
            self.scaled_surface,
        )

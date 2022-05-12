import sys
import pygame


class GameLoop:
    """The main loop of the game

    This class takes the game's component classes and uses them to implement a
    main loop. It's fundamental purpose is to provide a run function that makes
    the game run.

    Attributes:
        levels: A list of any number of Level objects
        clock: A Clock object for drawing the game at correct fps
        renderer: A Renderer object to render the game to the display
        event_queue: An EventQueue object to catch pygame events
        database: A DataBase object to store data about game runs into
    """
    def __init__(
        self,
        levels,
        clock,
        renderer,
        event_queue,
        database,
    ):
        """Inits the game loop.

        Args:
            levels: A list of any number of Level objects
            clock: A Clock object
            renderer: A Renderer object
            event_queue: An EventQueue object
            database: A DataBase object
        """

        self.levels = levels
        self.clock = clock
        self.renderer = renderer
        self.event_queue = event_queue
        self.database = database

    def run(self):
        """The main function of the game loop.

        This function does the looping. It loops over the levels in
        self.levels and provides a while loop for a level to run in. The while
        loop handles player-induced events, updates and renders the level and
        breaks the loop based on the state of the level being played. After the
        loop exits, the highest level the player completed gets saved to the
        database.

        Returns:
            count: the index of the level the loop exited on. This gets
            returned if the player loses the game

            "game_won_menu": The dictionary key that the UI uses to navigate to
            the game won -menu. This gets returned if the player beats all
            levels.
        """

        count = None
        for count, level in enumerate(self.levels):
            self.renderer.content = level
            while True:
                self._handle_events(level)

                level.update()

                if level.lost:
                    result_level = count
                    break

                if level.won:
                    result_level = count + 1
                    break

                self.renderer.render()

                self.clock.tick(60)
            if level.lost:
                break
        self.database.store_result(result_level)
        if result_level == len(self.levels):
            return "game_won_menu"
        return count

    def _handle_events(self, level):
        """Handles all user-induced events

        In practice this means whatching for quitting and then passing other
        events to player controls to move the player sprite.

        Args:
            level: The level on which the game is currently running
        """

        for event in self.event_queue.get():
            if event.type == pygame.QUIT:
                sys.exit()
            level.player.controls(event)

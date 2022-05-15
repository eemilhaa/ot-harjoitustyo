import pygame
from loaders.image_loader import load_image


class Player(pygame.sprite.Sprite):
    """A class for representing the player.

    This class hosts everything related to the player. Most importantly the
    logic related to player movement and controls.

    Attributes:
        image: A image to visually represent the player in the game
        rect: A pygame Rect object to logically represent the player in the
        game
        rect.x: The players position on the x axis
        rect.y: The players position on the y axis
        speed: The speed at which the player moves horizontally
        jump_speed: The speed at which a jump starts upwards
        y_momentum: A constantly increasing momentum downwards to represent
        gravity
        left: Is the player moving left
        right: Is the player moving right
        can_jump: Is the player allowed to jump
        won: has the player won a level
    """

    def __init__(self, x_location, y_location):
        """Inits the player class.

        Args:
            x_location: The players starting position on the x axis
            y_location: The players starting position on the y axis
        """

        super().__init__()

        self.image = load_image("player.png")
        self.rect = self.image.get_rect()

        self.rect.x = x_location
        self.rect.y = y_location

        self.speed = 1
        self.jump_speed = -4
        self.y_momentum = 0

        self.left = False
        self.right = False
        self.can_jump = False

        self.won = False

    def controls(self, event):
        """Decides where the player should move based on events.

        Args:
            event: A pygame event
        """

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left = True
            if event.key == pygame.K_RIGHT:
                self.right = True
            if event.key == pygame.K_SPACE and self.can_jump:
                self._jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left = False
            if event.key == pygame.K_RIGHT:
                self.right = False

    def update_position(self, collide_rects, target_rects):
        """Updates player position and checks for winning.

        Moving is done in relation to the the map of the level.

        Args:
            collide_rects: All the rects the player can collide with
            target_rects: The rect(s) that the player has to reach in order to
            win
        """

        # Update x axis
        if self.left:
            self._move_left(collide_rects)
        if self.right:
            self._move_right(collide_rects)

        # Update y axis
        self.rect.y += self.y_momentum
        if self.y_momentum > 0:
            self._check_down_collisions(collide_rects)
        if self.y_momentum < 0:
            self._check_up_collisions(collide_rects)

        # Limit falling speed
        if self.y_momentum < 3:
            self.y_momentum += 0.30

        # See if target is reached
        if self._get_collisions(target_rects):
            self.won = True

    def _move_left(self, collide_rects):
        """Moves the player left.

        After moving checks for collisions and restricts movement by resetting
        players position if collisions happen

        Args:
            collide_rects: the group of rects that the player can collide with
        """

        self.rect.x -= self.speed
        for tile in self._get_collisions(collide_rects):
            self.rect.left = tile.rect.right

    def _move_right(self, collide_rects):
        """Moves the player right.

        After moving checks for collisions and restricts movement by resetting
        players position if collisions happen

        Args:
            collide_rects: the group of rects that the player can collide with
        """

        self.rect.x += self.speed
        for tile in self._get_collisions(collide_rects):
            self.rect.right = tile.rect.left

    def _jump(self):
        """Sets the player's y_momentum to the jump_speed value.

        This makes the player jump as the value is negative.
        """

        self.y_momentum = self.jump_speed
        self.can_jump = False

    def _check_down_collisions(self, collide_rects):
        """Checks for collisons while falling down.

        Also restricts movement by resetting players position if collisions
        happen. y_momentum is also reset on collision down.

        Args:
            collide_rects: the group of rects that the player can collide with
        """

        for tile in self._get_collisions(collide_rects):
            self.rect.bottom = tile.rect.top
            self.y_momentum = 0
            self.can_jump = True

    def _check_up_collisions(self, collide_rects):
        """Checks for collisons while jumping up.

        Also restricts movement by resetting players position if collisions
        happen. y_momentum is set to positive to achieve a bouncing effect if
        the player hits a tile while moving up.

        Args:
            collide_rects: the group of rects that the player can collide with
        """

        for tile in self._get_collisions(collide_rects):
            self.rect.top = tile.rect.bottom
            self.y_momentum = 0.25

    def _get_collisions(self, tiles):
        """A function for getting all the tiles the player collides with.

        Args:
            tiles: The tiles to check collisons for

        Returns:
            collision_list: A list of tiles the player collides with
        """
        collision_list = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                collision_list.append(tile)
        return collision_list

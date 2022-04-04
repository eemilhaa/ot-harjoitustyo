import pygame
from image_loader import load_image


class Player(pygame.sprite.Sprite):
    def __init__(self, x=50, y=40):
        super().__init__()

        self.image = load_image("player.png")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.speed = 1
        self.jump_speed = -4
        self.y_momentum = 0

        self.left = False
        self.right = False
        self.can_jump = False
        self.jump = False

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def controls(self, event: pygame.event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left = True
            if event.key == pygame.K_RIGHT:
                self.right = True
            if event.key == pygame.K_SPACE and self.can_jump:
                self.jump = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left = False
            if event.key == pygame.K_RIGHT:
                self.right = False

    def update_position(self, collide_rects):
        if self.left:
            self.move_left(collide_rects)
        if self.right:
            self.move_right(collide_rects)
        if self.y_momentum > 0:
            self.rect.y += self.y_momentum
            for tile in self.get_collisions(collide_rects):
                self.rect.bottom = tile.rect.top
                self.y_momentum = 0
                self.can_jump = True
        if self.y_momentum < 0:
            self.rect.y += self.y_momentum
            for tile in self.get_collisions(collide_rects):
                self.rect.top = tile.rect.bottom
                self.y_momentum = 0.25
        if self.jump:
            self.y_momentum = self.jump_speed
            self.jump = False
            self.can_jump = False

        if self.y_momentum < 3:
            self.y_momentum += 0.25

    def move_left(self, collide_rects):
        self.rect.x -= self.speed
        for tile in self.get_collisions(collide_rects):
            self.rect.left = tile.rect.right

    def move_right(self, collide_rects):
        self.rect.x += self.speed
        for tile in self.get_collisions(collide_rects):
            self.rect.right = tile.rect.left

    # TODO
    def fall(self):
        pass
    # TODO
    def jump(self):
        pass

    def get_collisions(self, tiles):
        collision_list = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                collision_list.append(tile)
        return collision_list

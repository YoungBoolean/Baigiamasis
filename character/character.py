import pygame
from ui.constants import CHARACTER_WIDTH, CHARACTER_HEIGHT, NON_WALKABLE_AREAS, SPRITE_PATH_LIST, ENEMY_SPRITE_PATH_LIST


class Character:
    def __init__(self, x, y, screen_width, screen_height, sprite_path=SPRITE_PATH_LIST,
                 enemy_sprite_path=ENEMY_SPRITE_PATH_LIST, enemy=False):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width_scale = self.screen_width / 800  # original width
        self.height_scale = self.screen_height / 600  # original height
        self.character_width, self.character_height = (CHARACTER_WIDTH * self.width_scale,
                                                       CHARACTER_HEIGHT * self.height_scale)
        self.rect = pygame.Rect(x, y, self.character_width, self.character_height)
        if enemy:
            self.sprites = [pygame.image.load(sprite).convert_alpha() for sprite in enemy_sprite_path]
        else:
            self.sprites = [pygame.image.load(sprite).convert_alpha() for sprite in sprite_path]
        self.sprite_index = 0
        self.image = pygame.transform.scale(self.sprites[0],
                                            (self.character_width, self.character_height))
        self.flipped_image = pygame.transform.flip(self.image, True, False)  # Flip the sprite

    def move(self, dx, dy):
        new_rect = self.rect.move(dx, dy)
        if dx >= 5 * self.width_scale:
            self.sprite_index += 1
            self.image = pygame.transform.scale(self.sprites[self.sprite_index],
                                                (self.character_width, self.character_height))
            self.flipped_image = pygame.transform.flip(self.image, True, False)  # Flip the sprite
            self.image = self.flipped_image
            if self.sprite_index >= 2:
                self.sprite_index = 0
        if dx == -5 * self.width_scale or dx == -15 * self.width_scale:
            self.sprite_index += 1
            self.image = pygame.transform.scale(self.sprites[self.sprite_index],
                                                (self.character_width, self.character_height))
            if self.sprite_index >= 2:
                self.sprite_index = 0
        if self.is_within_bounds(new_rect) and not self.collides_with_non_walkable(new_rect):
            self.rect = new_rect

    def is_within_bounds(self, rect):
        return (rect.left >= 0 and rect.right <= self.screen_width and rect.top >= 0
                and rect.bottom <= self.screen_height)

    def collides_with_non_walkable(self, rect):
        for area in NON_WALKABLE_AREAS:
            scaled_rect = pygame.Rect(
                area.x * self.width_scale,
                area.y * self.height_scale,
                area.width * self.width_scale,
                area.height * self.height_scale
            )
            if rect.colliderect(scaled_rect):
                return True
        return False

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def return_position(self):
        return self.rect.topleft

    def chase(self, target_x, target_y, chase_speed):
        # Calculate the distance to the target
        distance_x = target_x - self.rect.x
        distance_y = target_y - self.rect.y
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5

        # Normalize the direction
        if distance > 0:
            direction_x = distance_x / distance
            direction_y = distance_y / distance

            # Update the position
            dx = direction_x * chase_speed
            dy = direction_y * chase_speed
            self.move(dx, dy)
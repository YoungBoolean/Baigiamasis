import pygame
from ui.constants import CHARACTER_WIDTH, CHARACTER_HEIGHT, NON_WALKABLE_AREAS


class Character:
    def __init__(self, x, y, screen_width, screen_height, sprite='resources/character_assets/char_template.png'):
        self.rect = pygame.Rect(x, y, CHARACTER_WIDTH, CHARACTER_HEIGHT)
        self.sprite = pygame.image.load(sprite).convert_alpha()
        self.image = pygame.transform.scale(self.sprite, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
        self.flipped_image = pygame.transform.flip(self.image, True, False)  # Flip the sprite
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move(self, dx, dy):
        new_rect = self.rect.move(dx, dy)
        if dx == 5:
            self.image = self.flipped_image
        if dx == -5:
            self.image = pygame.transform.scale(self.sprite, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
        if self.is_within_bounds(new_rect) and not self.collides_with_non_walkable(new_rect):
            self.rect = new_rect


    def is_within_bounds(self, rect):
        return rect.left >= 0 and rect.right <= self.screen_width and rect.top >= 0 and rect.bottom <= self.screen_height

    def collides_with_non_walkable(self, rect):
        for area in NON_WALKABLE_AREAS:
            if rect.colliderect(area):
                return True
        return False

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
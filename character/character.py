import pygame
from ui.constants import CHARACTER_WIDTH, CHARACTER_HEIGHT


class Character:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, CHARACTER_WIDTH, CHARACTER_HEIGHT)
        self.image = pygame.Surface((CHARACTER_WIDTH, CHARACTER_HEIGHT))
        self.image.fill((255, 0, 0))  # Red rectangle as a placeholder for the character image

    def move(self, dx, dy):
        new_rect = self.rect.move(dx, dy)
        if self.is_within_bounds(new_rect) and not self.collides_with_non_walkable(new_rect):
            self.rect = new_rect

    def is_within_bounds(self, rect):
        return rect.left >= 0 and rect.right <= SCREEN_WIDTH and rect.top >= 0 and rect.bottom <= SCREEN_HEIGHT

    def collides_with_non_walkable(self, rect):
        for area in NON_WALKABLE_AREAS:
            if rect.colliderect(area):
                return True
        return False

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
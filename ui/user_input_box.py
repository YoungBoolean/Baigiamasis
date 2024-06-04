"""
user_input_box.py

This module contains the InputBox class, it is responsbile for drawing the characters, which the user enters, on screen.
"""

import pygame
from ui.constants import TEXT_FONT_PATH, WHITE, BLACK


class InputBox:
    """InputBox class, responsible for drawing the user entered characters, i.e. Username, on screen."""

    def __init__(self, x, y, w, h, text='', max_font_size=24,
                 font_path=TEXT_FONT_PATH):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = WHITE
        self.text = text
        self.font = pygame.font.Font(font_path, max_font_size)
        self.text_surf = self.font.render(text, True, BLACK)
        self.username = None

    def handle_event(self, event):
        """Takes an event, checks if it's valid and saves the characters entered."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.username = self.text  # Save the entered username
                print(self.username)  # Print the username for debugging
                self.text = ''
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if event.unicode.isalnum():  # Only allow alphanumeric characters
                    self.text += event.unicode

            self.text_surf = self.font.render(self.text, True, BLACK)

    def update(self):
        """Resizes the box if the text is too long."""
        width = max(200, self.text_surf.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        """Renders the text."""
        screen.blit(self.text_surf, (self.rect.x + 5, self.rect.y + 5))

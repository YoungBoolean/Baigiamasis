import pygame
from ui.constants import FONT_PATH, BUTTON_FILE_PATH, TEXT_FONT_PATH, USER_NAME, WHITE, BLACK, GREEN, DARK_GREEN, GRAY


class InputBox:
    def __init__(self, x, y, w, h, text='', max_font_size=24,
                 font_path=TEXT_FONT_PATH):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = WHITE
        self.text = text
        self.font = pygame.font.Font(font_path, max_font_size)
        self.text_surf = self.font.render(text, True, BLACK)
        self.username = None

    def handle_event(self, event):
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
        # Resize the box if the text is too long.
        width = max(200, self.text_surf.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.text_surf, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.

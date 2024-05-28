import pygame
from ui.constants import FONT_PATH, BUTTON_FILE_PATH, TEXT_FONT_PATH


class Button:
    def __init__(self, x, y, text='', max_font_size=24, scroll=False,
                 button_text_box_size=(0, 0),
                 button_text_padding=120, button_file_path='resources/menu_button.png',
                 font_path=FONT_PATH, button_size=(300, 50), text_color=(255, 255, 255)):
        self.text_color = text_color
        self.button_size = button_size
        self.button_text_box_size = button_text_box_size
        self.button_text_padding = button_text_padding
        self.button_image = pygame.image.load(button_file_path).convert_alpha()
        self.image = pygame.transform.scale(self.button_image, self.button_size)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.max_font_size = max_font_size
        self.text = text
        self.font = pygame.font.Font(font_path, self.max_font_size)
        self.text_surf, self.text_rect = self.update_text(self.text)
        self.button_sound = pygame.mixer.Sound('resources/button_press.wav')
        self.scroll = scroll
        self.scroll_button_size = (20, 400)
        self.hover_button_file_counter = 1
        self.animation_done = False

    @classmethod
    def get_button_size(cls, button_size=(300, 50)):
        return button_size

    def update_text(self, text):
        """Update the text and adjust font size if the text is too long."""
        self.text = text
        font_size = self.max_font_size
        self.font = pygame.font.Font(FONT_PATH, font_size)
        text_surf = self.font.render(self.text, True, self.text_color)

        # Decrease font size until the text fits the button width
        while text_surf.get_width() > self.rect.width - self.button_text_padding:  # 20 pixels of padding
            font_size -= 1
            self.font = pygame.font.Font(FONT_PATH, font_size)
            text_surf = self.font.render(self.text, True, self.text_color)

        # Define the text_rect with the new size and center it on the button
        text_rect = text_surf.get_rect(center=self.rect.center)
        self.text_rect = text_rect
        self.text_surf = text_surf
        return text_surf, text_rect

    def draw(self, screen):
        # Draw scroll button if enabled
        if self.scroll:
            # Draw the scroll button at a specific position relative to the button
            scroll_button_rect = pygame.Rect(self.rect.right + 10, self.rect.top, *self.scroll_button_size)
            pygame.draw.rect(screen, (0, 0, 255),
                             scroll_button_rect)
        else:
            # Draw the button and the text centered on it.
            screen.blit(self.image, self.rect)
            screen.blit(self.text_surf, self.text_rect)

    def check_hover(self, screen, repeat=True):
        # Check if the mouse is hovering over the button and change the image accordingly.
        max_hover_button_file_index = 18
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            filename = f"{self.hover_button_file_counter}.png"
            hover_image_load = pygame.image.load(BUTTON_FILE_PATH + filename).convert_alpha()
            hover_image = pygame.transform.scale(hover_image_load, self.button_size)
            screen.blit(hover_image, self.rect)
            self.hover_button_file_counter += 1
            screen.blit(self.text_surf, self.text_rect)
            if repeat:
                if self.hover_button_file_counter >= max_hover_button_file_index:
                    self.hover_button_file_counter = 1

    def text_box_appear(self, screen, file_path='resources/text_button/', max_index=14):
        if not self.animation_done:
            filename = f"{self.hover_button_file_counter}.png"
            image_load = pygame.image.load(file_path + filename).convert_alpha()
            image = pygame.transform.scale(image_load, self.button_size)
            screen.blit(image, self.rect)
            screen.blit(self.text_surf, self.text_rect)
            if self.hover_button_file_counter < max_index:
                self.hover_button_file_counter += 1
            else:
                self.animation_done = True
        filename = f"{self.hover_button_file_counter}.png"
        image_load = pygame.image.load(file_path + filename).convert_alpha()
        image = pygame.transform.scale(image_load, self.button_size)
        screen.blit(image, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def reset_animation(self):
        self.hover_button_file_counter = 1
        self.animation_done = False

    def play_button_sound(self):
        self.button_sound.play()

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.play_button_sound()
                return True
        return False

import pygame
from ui.constants import FONT_PATH, BUTTON_FILE_PATH


class Button:
    """Button class - responsible for the creation and functionality of buttons"""
    def __init__(self, x, y,
                 text='',
                 max_font_size=24,
                 scroll=False,
                 button_text_box_size=(0, 0),
                 button_text_padding=120,
                 button_file_path='resources/menu_button.png',
                 font_path=FONT_PATH,
                 button_size=(300, 50),
                 text_color=(255, 255, 255)):
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
        self.go_back = False

    def get_button_size(self):
        """Returns the size of the button"""
        return self.button_size

    def draw(self, screen):
        """Draw the button and the text centered on it."""
        screen.blit(self.image, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def check_hover(self, screen, repeat=True):
        """Check if the mouse is hovering over the button and change the image accordingly."""
        max_hover_button_file_index = 18
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            filename = f"{self.hover_button_file_counter}.png"
            hover_image_load = pygame.image.load(BUTTON_FILE_PATH + filename).convert_alpha()
            hover_image = pygame.transform.scale(hover_image_load, self.button_size)
            screen.blit(hover_image, self.rect)
            if not self.go_back:
                self.hover_button_file_counter += 1
            screen.blit(self.text_surf, self.text_rect)
            if repeat:
                if self.go_back:
                    if self.hover_button_file_counter > 1:
                        self.hover_button_file_counter -= 1
                    else:
                        self.go_back = False
                if not self.go_back:
                    if self.hover_button_file_counter >= max_hover_button_file_index:
                        self.go_back = True

    def text_box_appear(self, screen, file_path='resources/text_button/', max_index=14):
        """Animate the first appearance of the text_box button"""
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

    def update_text(self, text: str):
        """Update the text and adjust font size if the text is too long."""
        self.text = text
        font_size = self.max_font_size
        text_surf = self.font.render(self.text, True, self.text_color)

        # Decrease font size until the text fits the button width
        while text_surf.get_width() > self.rect.width - self.button_text_padding:
            font_size -= 1
            self.font = pygame.font.Font(FONT_PATH, font_size)
            text_surf = self.font.render(self.text, True, self.text_color)

        # Define the text_rect with the new size and center it on the button
        text_rect = text_surf.get_rect(center=self.rect.center)
        self.text_rect = text_rect
        self.text_surf = text_surf
        return text_surf, text_rect

    def render_multiline_text(self, text, color, screen, line_spacing=1.5):
        """Render multi-line text to a pygame surface."""
        words = [word.split(' ') for word in text.splitlines()]
        space_width, space_height = self.font.size(' ')
        x, y = self.rect.topleft
        max_width, max_height = self.rect.size

        for line in words:
            for word in line:
                word_surface = self.font.render(word, True, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = self.rect.left
                    y += word_height * line_spacing
                screen.blit(word_surface, (x, y))
                x += word_width + space_width
            x = self.rect.left
            y += word_height * line_spacing

    def reset_animation(self):
        """Reset the animation of the button"""
        self.hover_button_file_counter = 1
        self.animation_done = False

    def play_button_sound(self):
        """Play sound when button is clicked"""
        self.button_sound.play()

    def is_clicked(self, event):
        """Check if the button is clicked"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.play_button_sound()
                return True
        return False

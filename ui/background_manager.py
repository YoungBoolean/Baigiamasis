# background_manager.py
import pygame

from ui.constants import BACKGROUND_IMAGE_PATH, FONT_PATH, BACKGROUND_IMAGE_PATH_LIST, LOADING_IMAGE_PATH_LIST


class BackgroundManager:
    def __init__(self, screen_size, image_path_list=BACKGROUND_IMAGE_PATH_LIST):
        self.screen_size = screen_size
        self.images = [self.load_and_scale_background(img_path, self.screen_size) for img_path in
                       image_path_list]
        self.current_frame = 0
        self.frame_count = len(self.images)
        self.frame_duration = 100  # duration each frame is displayed in milliseconds
        self.last_update = pygame.time.get_ticks()

    def load_and_scale_background(self, image_path, screen_size):
        # Load the image
        background = pygame.image.load(image_path)
        # Scale the image
        background = pygame.transform.scale(background, screen_size)
        return background

    def update_screen_size(self, new_screen_size, image_path_list=BACKGROUND_IMAGE_PATH_LIST):
        self.screen_size = new_screen_size
        self.images = [self.load_and_scale_background(img_path, self.screen_size) for img_path in
                       image_path_list]

    def update_background(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.last_update = now

    def change_and_draw_background(self, img_path, screen):
        self.images = self.load_and_scale_background(img_path, self.screen_size)
        screen.blit(self.images, (0, 0))

    def draw_background(self, screen):
        screen.blit(self.images[self.current_frame], (0, 0))

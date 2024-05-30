# background_manager.py
import pygame

from ui.constants import BACKGROUND_IMAGE_PATH_LIST, BACKGROUND_PLACEHOLDER_IMAGE_PATH


class BackgroundManager:
    def __init__(self, screen_size, slideshow=True, clouds=True):
        self.screen_size = screen_size
        self.slideshow = slideshow
        self.image_path = BACKGROUND_PLACEHOLDER_IMAGE_PATH
        self.image_path_list=BACKGROUND_IMAGE_PATH_LIST
        if self.slideshow:
            self.images_slideshow = [self.load_and_scale_background(img_path, self.screen_size) for img_path in
                                     self.image_path_list]
            self.frame_count = len(self.images_slideshow)
        self.image = self.load_and_scale_background(self.image_path, self.screen_size)
        self.current_frame = 0
        self.frame_duration = 100  # duration each frame is displayed in milliseconds
        self.last_update = pygame.time.get_ticks()
        self.counter = -800
        if clouds:
            self.clouds_image = self.load_and_scale_background('resources/main_map/clouds.png', self.screen_size)

    def load_and_scale_background(self, image_path, screen_size):
        # Load the image
        background = pygame.image.load(image_path)
        # Scale the image
        background = pygame.transform.scale(background, screen_size)
        return background

    def update_screen_size(self, new_screen_size, image_path_list=BACKGROUND_IMAGE_PATH_LIST):
        self.screen_size = new_screen_size
        self.images_slideshow = [self.load_and_scale_background(img_path, self.screen_size) for img_path in
                                 image_path_list]

    def update_image_path(self, img_path):
        self.image_path = img_path

    def update_image_slideshow_path(self, img_path_list):
        self.image_path_list = img_path_list

    def update_background_slideshow(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.last_update = now

    def move_from_left_to_right(self, screen):
        self.counter += 1
        screen.blit(self.clouds_image, (self.counter, 0))
        if self.counter == 900:
            self.counter = -800

    def draw_background(self, screen):
        if self.slideshow:
            screen.blit(self.images_slideshow[self.current_frame], (0, 0))
        else:
            self.image = self.load_and_scale_background(self.image_path, self.screen_size)
            screen.blit(self.image, (0, 0))

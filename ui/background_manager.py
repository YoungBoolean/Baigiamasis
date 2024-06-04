"""
background_manager.py

This module contains the BackgroundManager class, which is responsbile for drawing, animation,
positions of background images for the game screen.
"""

import pygame

from ui.constants import BACKGROUND_IMAGE_PATH_LIST, BACKGROUND_PLACEHOLDER_IMAGE_PATH


class BackgroundManager:
    """Manages the drawing, animation, positions of background images for the game screen."""

    def __init__(self, screen_size, slideshow=True, clouds=True):
        self.screen_size = screen_size
        self.slideshow = slideshow
        self.image_path = BACKGROUND_PLACEHOLDER_IMAGE_PATH
        self.image_path_list = BACKGROUND_IMAGE_PATH_LIST
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
        self.filter_img = self.load_and_scale_background('resources/scene_backgrounds/filter.png', self.screen_size)

    def load_and_scale_background(self, image_path, screen_size):
        """Loads and scales a background image."""

        # Load the image
        background = pygame.image.load(image_path)
        # Scale the image
        background = pygame.transform.scale(background, screen_size)
        return background

    def update_screen_size(self, new_screen_size, image_path_list=BACKGROUND_IMAGE_PATH_LIST):
        """Updates the screen size and reloads background images for the slideshow."""
        self.screen_size = new_screen_size
        self.images_slideshow = [self.load_and_scale_background(img_path, self.screen_size) for img_path in
                                 image_path_list]
        self.frame_count = len(self.images_slideshow)

    def update_image_path(self, img_path):
        """Updates the path to the current background image."""
        self.image_path = img_path

    def update_background_slideshow(self):
        """Updates the current frame in the background slideshow."""
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.last_update = now

    def move_from_left_to_right(self, screen, settings):
        """Moves the clouds animation from left to right on the screen."""
        screen_width, screen_height = settings.current_resolution
        self.counter += 2
        clouds_img = pygame.transform.scale(self.clouds_image, self.screen_size)
        screen.blit(clouds_img, (self.counter, 0))
        if self.counter == 900 + screen_width / 2:
            self.counter = -800

    def draw_background(self, screen):
        """Draws the background image on the screen. If self.slideshow is toggled, draws the animation frame instead"""
        if self.slideshow:
            if self.frame_count > 0:
                try:
                    screen.blit(self.images_slideshow[self.current_frame], (0, 0))
                except IndexError:
                    self.image = self.load_and_scale_background(self.image_path, self.screen_size)
                    screen.blit(self.image, (0, 0))
        else:
            self.image = self.load_and_scale_background(self.image_path, self.screen_size)
            screen.blit(self.image, (0, 0))

    def draw_filter(self, screen):
        """Draws a filter effect on the background."""
        filter_img = pygame.transform.scale(self.filter_img, self.screen_size)
        screen.blit(filter_img, (0, 0))

"""
settings_menu.py

This module contains the SettingsMenu class, it is responsbile for drawing the settings menu, changing of resolutions.
"""

import sys

import pygame

from ui.button import Button
from ui.constants import FPS, RESOLUTIONS


class SettingsMenu:
    """SettingsMenu class, responsible for drawing the settings menu, button object creation"""

    def __init__(self, screen, clock, settings, background_manager, background_manager_loading):
        self.screen = screen
        self.clock = clock
        self.settings = settings
        self.background_manager = background_manager
        self.background_manager_loading = background_manager_loading
        self.screen_width, self.screen_height = settings.current_resolution
        self.start()

    def create_buttons(self):
        """Creates buttons"""
        original_width, original_height = RESOLUTIONS[0]
        width_scale = self.screen_width / original_width
        height_scale = self.screen_height / original_height

        resolution_btn = Button(250 * width_scale, 180 * height_scale,
                                f'{self.settings.current_resolution[0]} x {self.settings.current_resolution[1]}',
                                button_size=(300 * width_scale, 50 * height_scale))

        fullscreen_btn = Button(250 * width_scale, 240 * height_scale,
                                'Windowed' if self.settings.fullscreen else 'Fullscreen',
                                button_size=(300 * width_scale, 50 * height_scale))

        back_btn = Button(250 * width_scale, 300 * height_scale,
                          'Back', button_size=(300 * width_scale, 50 * height_scale))

        return resolution_btn, fullscreen_btn, back_btn

    def start(self):
        """Starts the settings menu loop"""
        resolution_btn, fullscreen_btn, back_btn = self.create_buttons()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                if resolution_btn.is_clicked(event):
                    self.settings.increase_resolution()
                    self.screen = pygame.display.set_mode(self.settings.current_resolution)
                    resolution_btn_text = (f'{self.settings.current_resolution[0]} x '
                                           f'{self.settings.current_resolution[1]}')
                    self.background_manager.update_screen_size(self.settings.current_resolution)
                    self.background_manager_loading.update_screen_size(self.settings.current_resolution)
                    resolution_btn.update_text(resolution_btn_text)
                if fullscreen_btn.is_clicked(event):
                    self.settings.toggle_fullscreen()
                    self.update_screen_mode(self.screen, self.settings, self.background_manager)
                    self.update_screen_mode(self.screen, self.settings, self.background_manager_loading)
                    self.background_manager.update_screen_size(self.settings.current_resolution)
                    self.background_manager_loading.update_screen_size(self.settings.current_resolution)
                    fullscreen_btn.update_text('Windowed' if self.settings.fullscreen else 'Fullscreen')
                if back_btn.is_clicked(event):
                    return  # Returns back to main menu

            self.background_manager_loading.update_background_slideshow()
            self.background_manager_loading.draw_background(self.screen)
            resolution_btn.draw(self.screen)
            resolution_btn.check_hover(self.screen)
            fullscreen_btn.draw(self.screen)
            fullscreen_btn.check_hover(self.screen)
            back_btn.draw(self.screen)
            back_btn.check_hover(self.screen)
            self.background_manager.draw_filter(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)

    def update_screen_mode(self, screen, settings, background_manager):
        """Updates the screen mode"""
        if settings.fullscreen:
            self.screen = pygame.display.set_mode(settings.current_resolution, pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(settings.current_resolution)

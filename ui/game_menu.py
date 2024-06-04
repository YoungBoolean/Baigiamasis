"""
game_menu.py

This module contains the GameMenu class, which is responsible for drawing the main menu, main menu buttons.
This is the entry point of what the user sees when they run the program.
"""

import sys

import pygame

from ui.button import Button
from ui.constants import FPS, RESOLUTIONS
from ui.settings_menu import SettingsMenu
from game import start
from .load_menu import LoadMenu


class GameMenu:
    """
    Game menu game loop class, responsible for drawing the main menu,
    button object creation, entries to other menus
    """

    def __init__(self, screen, clock, settings, background_manager, background_manager_loading):
        self.screen = screen
        self.clock = clock
        self.settings = settings
        self.background_manager = background_manager
        self.background_manager_loading = background_manager_loading
        self.screen_width, self.screen_height = settings.current_resolution
        self.start()

    def create_buttons(self):
        """Creates buttons, to be used in the GameMenu loop"""
        original_width, original_height = RESOLUTIONS[0]
        width_scale = self.screen_width / original_width
        height_scale = self.screen_height / original_height

        start_btn = Button(250 * width_scale, 180 * height_scale,
                           'New game', button_size=(300 * width_scale, 50 * height_scale))

        load_btn = Button(250 * width_scale, 240 * height_scale,
                          'Load game', button_size=(300 * width_scale, 50 * height_scale))

        settings_btn = Button(250 * width_scale, 300 * height_scale,
                              'Settings', button_size=(300 * width_scale, 50 * height_scale))

        return start_btn, load_btn, settings_btn

    def start(self):
        """Starts the main menu game loop"""
        start_btn, load_btn, settings_btn = self.create_buttons()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

                # Starts the game if start_btn is clicked
                if start_btn.is_clicked(event):
                    self.screen.fill((0, 0, 0))
                    start(self.screen, self.clock, self.settings, self.background_manager_loading,
                          self.background_manager)
                    self.background_manager_loading.update_screen_size(self.settings.current_resolution)
                    self.background_manager_loading.update_background_slideshow()

                # Starts the load menu if load_btn is clicked
                if load_btn.is_clicked(event):
                    LoadMenu(self.screen, self.clock, self.settings,
                             self.background_manager, self.background_manager_loading)

                # Starts the settings menu if settings_btn is clicked
                if settings_btn.is_clicked(event):
                    SettingsMenu(self.screen, self.clock, self.settings,
                                 self.background_manager, self.background_manager_loading)

            # Drawing of backgrounds
            self.background_manager_loading.update_background_slideshow()
            self.background_manager_loading.draw_background(self.screen)

            # Drawing of buttons, filter
            load_btn.draw(self.screen)
            load_btn.check_hover(self.screen)
            start_btn.draw(self.screen)
            start_btn.check_hover(self.screen)
            settings_btn.draw(self.screen)
            settings_btn.check_hover(self.screen)
            self.background_manager.draw_filter(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)

import sys

import pygame

from ui.button import Button
from ui.constants import FPS
from ui.settings_menu import settings_menu
from game import start
from ui.utilities import calculate_position
from .load_menu import LoadMenu


class GameMenu:
    """Game menu game loop class, responsible for drawing the main menu, button object creation"""

    def __init__(self, screen, clock, settings, background_manager, background_manager_loading):
        self.screen = screen
        self.clock = clock
        self.settings = settings
        self.background_manager = background_manager
        self.background_manager_loading = background_manager_loading
        self.screen_width, self.screen_height = settings.current_resolution
        self.start()

    def create_buttons(self) -> tuple:
        start_btn_x, start_btn_y = calculate_position(self.screen_width, self.screen_height, 0.313,
                                                      0.62)
        start_btn = Button(start_btn_x,
                           start_btn_y,
                           'New game')

        load_btn_x, load_btn_y = calculate_position(self.screen_width, self.screen_height, 0.313, 0.72)
        load_btn = Button(load_btn_x,
                          load_btn_y,
                          'Load game')

        settings_btn_x, settings_btn_y = calculate_position(self.screen_width, self.screen_height, 0.313, 0.82)
        settings_btn = Button(settings_btn_x,
                              settings_btn_y,
                              'Settings')

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

                if start_btn.is_clicked(event):
                    self.screen.fill((0, 0, 0))
                    start(self.screen, self.clock, self.settings, self.background_manager_loading,
                          self.background_manager)
                    self.background_manager_loading.update_screen_size(self.settings.current_resolution)
                    self.background_manager_loading.update_background_slideshow()

                if load_btn.is_clicked(event):
                    LoadMenu(self.screen, self.clock, self.settings,
                             self.background_manager, self.background_manager_loading)

                if settings_btn.is_clicked(event):
                    settings_menu(self.screen, self.clock, self.settings,
                                  self.background_manager, self.background_manager_loading)

            self.background_manager_loading.update_background_slideshow()
            self.background_manager_loading.draw_background(self.screen)

            load_btn.draw(self.screen)
            load_btn.check_hover(self.screen)
            start_btn.draw(self.screen)
            start_btn.check_hover(self.screen)
            settings_btn.draw(self.screen)
            settings_btn.check_hover(self.screen)
            self.background_manager.draw_filter(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)

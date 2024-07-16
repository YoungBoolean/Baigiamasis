"""
load_menu.py

This module contains the LoadMenu class, it is responsbile for drawing the load menu, listing of save files.
"""

import sys

import pygame

from ui.button import Button
from ui.constants import FPS, RESOLUTIONS
from game import start
from database.save_states import savestate


class LoadMenu:
    """Game menu game loop class, responsible for drawing the load menu and it's button object creation"""

    def __init__(self, screen, clock, settings, background_manager,
                 background_manager_loading, button_image, button_image_solid, loaded_hover_image_list,
                 save_state=savestate):
        self.screen = screen
        self.clock = clock
        self.settings = settings
        self.background_manager = background_manager
        self.background_manager_loading = background_manager_loading
        self.button_image = button_image
        self.button_image_solid = button_image_solid
        self.loaded_hover_image_list = loaded_hover_image_list
        self.screen_width, self.screen_height = settings.current_resolution
        self.save_state = save_state
        self.screen_width, self.screen_height = settings.current_resolution
        self.original_width, self.original_height = RESOLUTIONS[0]
        self.width_scale = self.screen_width / self.original_width
        self.height_scale = self.screen_height / self.original_height
        self.start()

    def start(self):
        """Starts the main menu game loop"""
        no_saves_btn = None
        save_btn_list = []
        list_of_saves = self.save_state.get_saved_games()
        if list_of_saves:
            height = 120
            for save in list_of_saves:  # Creates buttons with save file information if any saves exist
                btn_o = Button(155 * self.width_scale,
                               height * self.height_scale, self.button_image, self.loaded_hover_image_list,
                               self.width_scale,
                               f'{save[1]} {save[2]} {save[3]}',
                               button_text_padding=4, button_size=(500 * self.width_scale, 50 * self.height_scale))
                save_btn_list.append([btn_o, save[4], save[5], save[6]])
                height += 60
        else:
            no_saves_btn = Button(155 * self.width_scale,
                                  120 * self.height_scale, self.button_image, self.loaded_hover_image_list,
                                  self.width_scale,
                                  f'There are currently no saves!', button_text_padding=10,
                                  button_size=(500 * self.width_scale, 50 * self.height_scale))

        back_btn = Button(260 * self.width_scale,
                          60 * self.height_scale, self.button_image, self.loaded_hover_image_list, self.width_scale,
                          'Back', button_size=(300 * self.width_scale, 50 * self.height_scale),
                          )
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

                if save_btn_list:
                    for saves_btn in save_btn_list:
                        if saves_btn[0].is_clicked(event):
                            username = saves_btn[0].text.split()[0]
                            game_state = saves_btn[0].text.split()[1]
                            items = [saves_btn[1], saves_btn[2], saves_btn[3]]
                            self.screen.fill((0, 0, 0))
                            # Starts the game from the selected save file
                            start(self.screen, self.clock, self.settings, self.background_manager_loading,
                                  self.background_manager, self.button_image, self.button_image_solid,
                                  self.loaded_hover_image_list,
                                  save_state=game_state, player_name=username, items=items)
                            return  # Returns back to main menu once main game loop is completed, terminated.

                if back_btn.is_clicked(event):
                    return  # Returns back to main menu

            self.background_manager_loading.update_background_slideshow()
            self.background_manager_loading.draw_background(self.screen)
            back_btn.draw(self.screen)
            back_btn.check_hover(self.screen)
            if no_saves_btn:
                no_saves_btn.draw(self.screen)
                no_saves_btn.check_hover(self.screen)
            for element in save_btn_list:
                element[0].draw(self.screen)
                element[0].check_hover(self.screen)

            self.background_manager.draw_filter(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)

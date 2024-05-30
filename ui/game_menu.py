import sys

import pygame

from ui.button import Button
from ui.constants import FPS
from ui.settings_menu import settings_menu
from game import start
from save_states import load_game
from ui.utilities import calculate_position


def game_menu(screen, clock, settings, background_manager, background_manager_loading):
    screen_width, screen_height = settings.current_resolution

    loaded_state = load_game()
    if loaded_state:
        load_possible = True
    else:
        load_possible = False

    def create_buttons():
        start_btn_x, start_btn_y = calculate_position(screen_width, screen_height, 0.313,
                                                      0.62 if load_possible else 0.4)
        start_btn = Button(start_btn_x,
                           start_btn_y,
                           'New game')

        if load_possible:
            load_btn_x, load_btn_y = calculate_position(screen_width, screen_height, 0.313, 0.72)
            load_btn = Button(load_btn_x,
                              load_btn_y,
                              'Load game')
        else:
            load_btn = None

        settings_btn_x, settings_btn_y = calculate_position(screen_width, screen_height, 0.313, 0.82)
        settings_btn = Button(settings_btn_x,
                              settings_btn_y,
                              'Settings')

        return start_btn, load_btn, settings_btn

    start_btn, load_btn, settings_btn = create_buttons()

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
                screen.fill((0, 0, 0))
                start(screen, clock, settings, background_manager_loading)

            if load_possible:
                if load_btn.is_clicked(event):
                    loaded_state = load_game()
                    game_state = loaded_state['game_state']
                    username = loaded_state.get('username')
                    screen.fill((0, 0, 0))
                    start(screen, clock, settings, background_manager_loading, save_state=game_state,
                          player_name=username)

            if settings_btn.is_clicked(event):
                settings_menu(screen, clock, settings, background_manager, background_manager_loading)

        background_manager.update_background()
        background_manager.draw_background(screen)

        if load_possible:
            load_btn.draw(screen)
            load_btn.check_hover(screen)
        start_btn.draw(screen)
        start_btn.check_hover(screen)
        settings_btn.draw(screen)
        settings_btn.check_hover(screen)

        pygame.display.flip()
        clock.tick(FPS)

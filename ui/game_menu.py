import sys

import pygame

from ui.button import Button
from ui.constants import FPS
from ui.settings_menu import settings_menu
from game import start
from save_states import load_game


def game_menu(screen, clock, settings, background_manager, background_manager_loading):
    if load_game():
        load_possible = True
        loaded_state = load_game()
    else:
        load_possible = False

    start_btn = Button((settings.current_resolution[0] - Button.get_button_size()[0]) / 2,
                       settings.current_resolution[1] - Button.get_button_size()[1] * (4.5 if load_possible else 3),
                       'New game')
    if load_possible:
        load_btn = Button((settings.current_resolution[0] - Button.get_button_size()[0]) / 2,
                          settings.current_resolution[1] - Button.get_button_size()[1] * 3,
                          'Load game')
    settings_btn = Button((settings.current_resolution[0] - Button.get_button_size()[0]) / 2,
                          settings.current_resolution[1] - Button.get_button_size()[1] * 1.5,
                          'Settings')

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

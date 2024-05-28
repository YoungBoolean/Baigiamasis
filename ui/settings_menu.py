import sys

import pygame

from ui.button import Button
from ui.constants import FPS


def settings_menu(screen, clock, settings, background_manager, background_manager_loading):
    resolution_btn = Button((settings.current_resolution[0] - Button.get_button_size()[0]) / 2,
                                settings.current_resolution[1] - Button.get_button_size()[1] * 5,
                                f'{settings.current_resolution[0]} x {settings.current_resolution[1]}')

    fullscreen_btn = Button((settings.current_resolution[0] - Button.get_button_size()[0]) / 2,
                            settings.current_resolution[1] - Button.get_button_size()[1] * 3.5,
                            'Windowed' if settings.fullscreen else 'Fullscreen')

    back_btn = Button((settings.current_resolution[0] - Button.get_button_size()[0]) / 2,
                      settings.current_resolution[1] - Button.get_button_size()[1] * 1.5,
                      'Back')

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
                settings.increase_resolution()
                screen = pygame.display.set_mode(settings.current_resolution)
                resolution_btn_text = f'{settings.current_resolution[0]} x {settings.current_resolution[1]}'
                background_manager.update_screen_size(settings.current_resolution)
                background_manager_loading.update_screen_size(settings.current_resolution)
                resolution_btn.update_text(resolution_btn_text)
            if fullscreen_btn.is_clicked(event):
                settings.toggle_fullscreen()
                update_screen_mode(screen, settings, background_manager)
                background_manager.update_screen_size(settings.current_resolution)
                background_manager_loading.update_screen_size(settings.current_resolution)
                fullscreen_btn.update_text('Windowed' if settings.fullscreen else 'Fullscreen')
            if back_btn.is_clicked(event):
                return

        background_manager.update_background()
        background_manager.draw_background(screen)
        resolution_btn.draw(screen)
        resolution_btn.check_hover(screen)
        fullscreen_btn.draw(screen)
        fullscreen_btn.check_hover(screen)
        back_btn.draw(screen)
        back_btn.check_hover(screen)

        pygame.display.flip()
        clock.tick(FPS)


def update_screen_mode(screen, settings, background_manager):
    if settings.fullscreen:
        screen = pygame.display.set_mode(settings.current_resolution, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(settings.current_resolution)

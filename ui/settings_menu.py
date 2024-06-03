import sys

import pygame

from ui.button import Button
from ui.constants import FPS
from ui.utilities import calculate_position


def settings_menu(screen, clock, settings, background_manager, background_manager_loading):
    screen_width, screen_height = settings.current_resolution

    resolution_btn_x, resolution_btn_y = calculate_position(screen_width, screen_height, 0.313, 0.62)
    resolution_btn = Button(resolution_btn_x,
                            resolution_btn_y,
                            f'{settings.current_resolution[0]} x {settings.current_resolution[1]}')

    fullscreen_btn_x, fullscreen_btn_y = calculate_position(screen_width, screen_height, 0.313, 0.72)
    fullscreen_btn = Button(fullscreen_btn_x,
                            fullscreen_btn_y,
                            'Windowed' if settings.fullscreen else 'Fullscreen')
    back_btn_x, back_btn_y = calculate_position(screen_width, screen_height, 0.313, 0.82)
    back_btn = Button(back_btn_x,
                      back_btn_y,
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
                update_screen_mode(screen, settings, background_manager_loading)
                background_manager.update_screen_size(settings.current_resolution)
                background_manager_loading.update_screen_size(settings.current_resolution)
                fullscreen_btn.update_text('Windowed' if settings.fullscreen else 'Fullscreen')
            if back_btn.is_clicked(event):
                return

        background_manager_loading.update_background_slideshow()
        background_manager_loading.draw_background(screen)
        resolution_btn.draw(screen)
        resolution_btn.check_hover(screen)
        fullscreen_btn.draw(screen)
        fullscreen_btn.check_hover(screen)
        back_btn.draw(screen)
        back_btn.check_hover(screen)
        background_manager.draw_filter(screen)

        pygame.display.flip()
        clock.tick(FPS)


def update_screen_mode(screen, settings, background_manager):
    if settings.fullscreen:
        screen = pygame.display.set_mode(settings.current_resolution, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(settings.current_resolution)

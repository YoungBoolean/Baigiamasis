import sys
import pygame

from ui.button import Button
from ui.constants import FPS, GameState, TEXT_FONT_PATH
from ui.user_input_box import InputBox
from save_states import save_game


def start(screen, clock, settings, background_manager_loading, save_state=GameState.INPUT, player_name='Player'):
    game_state = save_state
    user_name = player_name

    text_btn = Button((settings.current_resolution[0] - Button.get_button_size((1420, 0))[0] / 2),
                      settings.current_resolution[1] - Button.get_button_size((0, 90))[1] * 3,
                      '', button_size=(650, 252), font_path=TEXT_FONT_PATH, text_color=(20, 20, 20))
    settings_btn = Button((settings.current_resolution[0] - Button.get_button_size()[0]) / 2,
                          settings.current_resolution[1] - Button.get_button_size()[1] * 1.5,
                          'Settings')
    username_input_box = InputBox((settings.current_resolution[0] - Button.get_button_size((1550, 0))[0] / 2),
                                  settings.current_resolution[1] - Button.get_button_size((0, 100))[1] * 3, 300, 200)
    username_ask_btn = Button((settings.current_resolution[0] - Button.get_button_size((1420, 0))[0] / 2),
                              settings.current_resolution[1] - Button.get_button_size((0, 90))[1] * 3,
                              'Please enter your name', button_size=(650, 252), font_path=TEXT_FONT_PATH,
                              text_color=(20, 20, 20))
    save_btn = Button((settings.current_resolution[0] - Button.get_button_size((150, 25))[0]),
                      settings.current_resolution[1] - Button.get_button_size((150, 25))[1] * 24,
                      'Save game', button_size=(150, 25), text_color=(20, 20, 20), max_font_size=50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            username_input_box.handle_event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if save_btn.is_clicked(event):
                save_game({'game_state': game_state, 'username': user_name})
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if game_state == GameState.INPUT:
                    game_state = GameState.MENU
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                if game_state == GameState.MENU:
                    game_state = GameState.SCENE_1
                    text_btn.reset_animation()
                elif game_state == GameState.SCENE_1:
                    game_state = GameState.SCENE_2
                    text_btn.reset_animation()
                elif game_state == GameState.SCENE_2:
                    game_state = GameState.SCENE_3
                    text_btn.reset_animation()
                elif game_state == GameState.SCENE_3:
                    game_state = GameState.SCENE_4
                    text_btn.reset_animation()

        if game_state == GameState.INPUT:
            screen.fill((200, 200, 200))
            username_input_box.update()
            username_input_box.draw(screen)
            username_ask_btn.text_box_appear(screen)
        elif game_state == GameState.MENU:
            player_name = username_input_box.username if username_input_box.username else player_name
            background_manager_loading.update_background()
            background_manager_loading.draw_background(screen)

        elif game_state == GameState.SCENE_1:
            screen.fill((0, 0, 0))  # Clear the screen with black before drawing
            background_manager_loading.change_and_draw_background('resources/main_map/night.jpg', screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text(f'Nice to meet you, {player_name}')
            save_btn.draw(screen)
        elif game_state == GameState.SCENE_2:
            screen.fill((0, 0, 0))
            background_manager_loading.change_and_draw_background('resources/main_map/night.jpg', screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text('Enjoy! :)')
            save_btn.draw(screen)
        elif game_state == GameState.SCENE_3:
            screen.fill((0, 0, 0))
            background_manager_loading.change_and_draw_background('resources/main_map/night.jpg', screen)
            save_btn.draw(screen)
        elif game_state == GameState.SCENE_4:
            screen.fill((0, 0, 0))
            background_manager_loading.change_and_draw_background('resources/main_map/day.jpg', screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text('Somewhere in a fictional town, fictional country.')
            save_btn.draw(screen)

        save_btn.check_hover(screen)
        pygame.display.flip()
        clock.tick(FPS)

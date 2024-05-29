import sys
import pygame

from ui.button import Button
from ui.constants import FPS, GameState, TEXT_FONT_PATH
from ui.user_input_box import InputBox
from save_states import save_game, load_game


def start(screen, clock, settings, background_manager_loading, save_state=GameState.INPUT, player_name='Player'):
    screen_width, screen_height = settings.current_resolution
    game_state = save_state
    user_name = player_name

    text_btn = Button((screen_width - Button.get_button_size((652, 252))[0] / 0.9),
                      screen_height - Button.get_button_size((652, 252))[1] * 0.99,
                      '', button_size=(652, 252), font_path=TEXT_FONT_PATH, text_color=(20, 20, 20),
                      button_text_padding=20)
    menu_btn = Button((screen_width - Button.get_button_size()[0]) / 2,
                      screen_height - Button.get_button_size()[1] * 1.5,
                      'Settings')
    username_input_box = InputBox((screen_width - Button.get_button_size((1550, 0))[0] / 2.6),
                                  screen_height - Button.get_button_size((0, 100))[1] * 0.97, 300, 200)
    username_ask_btn = Button((screen_width - Button.get_button_size((652, 252))[0] / 0.9),
                              screen_height - Button.get_button_size((652, 252))[1] * 0.99,
                              'Please enter your name:', button_size=(652, 252), font_path=TEXT_FONT_PATH,
                              text_color=(20, 20, 20), button_text_padding=20)
    save_btn = Button((screen_width - Button.get_button_size((150, 25))[0]),
                      screen_height - Button.get_button_size((150, 25))[1] * 24,
                      'Save game', button_size=(150, 25), text_color=(20, 20, 20), button_text_padding=20,
                      button_file_path='resources/button_hover/14.png')
    load_btn = Button((screen_width - Button.get_button_size((150, 25))[0] / 0.5),
                      screen_height - Button.get_button_size((150, 25))[1] * 24,
                      'Load game', button_size=(150, 25), text_color=(20, 20, 20), button_text_padding=20,
                      button_file_path='resources/button_hover/14.png')
    menu_btn = Button((screen_width - Button.get_button_size((150, 25))[0] / 0.333),
                      screen_height - Button.get_button_size((150, 25))[1] * 24,
                      'Menu', button_size=(150, 25), text_color=(20, 20, 20), button_text_padding=90,
                      button_file_path='resources/button_hover/14.png')

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
            if load_btn.is_clicked(event):
                loaded_state = load_game()
                if loaded_state:
                    game_state = loaded_state['game_state']
                    user_name = loaded_state.get('username')
            if menu_btn.is_clicked(event):
                return
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
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
            username_ask_btn.text_box_appear(screen)
            username_input_box.update()
            username_input_box.draw(screen)
        elif game_state == GameState.MENU:
            player_name = username_input_box.username if username_input_box.username else player_name
            background_manager_loading.change_and_draw_background('resources/main_map/night.jpg', screen)
        elif game_state == GameState.SCENE_1:
            screen.fill((0, 0, 0))  # Clear the screen with black before drawing
            background_manager_loading.change_and_draw_background('resources/main_map/night.jpg', screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text(f'Nice to meet you, {player_name}')
            save_btn.draw(screen)
            load_btn.draw(screen)
            menu_btn.draw(screen)
        elif game_state == GameState.SCENE_2:
            screen.fill((0, 0, 0))
            background_manager_loading.change_and_draw_background('resources/main_map/night.jpg', screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text('Enjoy! :)')
            save_btn.draw(screen)
            load_btn.draw(screen)
            menu_btn.draw(screen)
        elif game_state == GameState.SCENE_3:
            screen.fill((0, 0, 0))
            background_manager_loading.change_and_draw_background('resources/main_map/night.jpg', screen)
            save_btn.draw(screen)
            load_btn.draw(screen)
            menu_btn.draw(screen)
        elif game_state == GameState.SCENE_4:
            screen.fill((0, 0, 0))
            background_manager_loading.change_and_draw_background('resources/main_map/day.jpg', screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text('Somewhere in a fictional town, fictional country.')
            save_btn.draw(screen)
            load_btn.draw(screen)
            menu_btn.draw(screen)

        save_btn.check_hover(screen)
        load_btn.check_hover(screen)
        menu_btn.check_hover(screen)
        pygame.display.flip()
        clock.tick(FPS)

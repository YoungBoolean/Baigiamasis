"""
game.py

This module contains the start function, which is responsible for running, managing the Main game loop and it's logic.
"""

import datetime
import sys
from random import randint

import pygame

from ui.button import Button
from ui.constants import FPS, GameStateName, TEXT_FONT_PATH, RESOLUTIONS, USER_NAME
from ui.user_input_box import InputBox
from character.character import Character
from ui.utilities import when_character_in_specific_coords
from database.save_states import savestate
from game_states import GameState


def start(screen, clock, settings, background_manager_loading, background_manager, button_image, button_image_solid,
          loaded_hover_image_list, save_state=GameStateName.LOADING_SCREEN, player_name=USER_NAME, items=None):
    """Starts the main game loop and sets up screen resolution and scaling"""
    if items is None:
        items = [0, 0, 0]
    screen_width, screen_height = settings.current_resolution
    original_width, original_height = RESOLUTIONS[0]
    width_scale = screen_width / original_width
    height_scale = screen_height / original_height

    # Initialize game state and player name
    game_state = save_state
    user_name = player_name

    # Create button objects
    text_btn = Button(80 * width_scale,
                      350 * height_scale, button_image, loaded_hover_image_list, width_scale,
                      '', button_size=(652 * width_scale, 252 * height_scale),
                      font_path=TEXT_FONT_PATH,
                      text_color=(20, 20, 20),
                      button_text_padding=40, max_font_size=24)

    username_input_box = InputBox(240 * width_scale,
                                  515 * height_scale, 300, 200, width_scale)

    username_ask_btn = Button(80 * width_scale,
                              350 * height_scale, button_image, loaded_hover_image_list, width_scale,
                              'Please enter your name:',
                              button_size=(652 * width_scale, 252 * height_scale),
                              font_path=TEXT_FONT_PATH,
                              text_color=(20, 20, 20),
                              button_text_padding=20, max_font_size=24)

    save_btn = Button(650 * width_scale,
                      1 * height_scale, button_image_solid, loaded_hover_image_list, width_scale,
                      'Save game',
                      button_size=(150 * width_scale, 25 * height_scale),
                      text_color=(20, 20, 20),
                      button_text_padding=20)

    load_btn = Button(500 * width_scale,
                      1 * height_scale, button_image_solid, loaded_hover_image_list, width_scale,
                      'Load game',
                      button_size=(150 * width_scale, 25 * height_scale),
                      text_color=(20, 20, 20),
                      button_text_padding=20)

    menu_btn = Button(350 * width_scale,
                      1 * height_scale, button_image_solid, loaded_hover_image_list, width_scale,
                      'Menu',
                      button_size=(150 * width_scale, 25 * height_scale),
                      text_color=(20, 20, 20), button_text_padding=90)

    choice_btn_1 = Button((260 * width_scale),
                          (180 * height_scale), button_image_solid, loaded_hover_image_list, width_scale,
                          'Choice 1', text_color=(20, 20, 20), button_text_padding=10)

    choice_btn_2 = Button((260 * width_scale),
                          (250 * height_scale), button_image_solid, loaded_hover_image_list, width_scale,
                          'Choice 2', text_color=(20, 20, 20), button_text_padding=10)

    choice_btn_3 = Button((260 * width_scale),
                          (320 * height_scale), button_image_solid, loaded_hover_image_list, width_scale,
                          'Choice 3', text_color=(20, 20, 20), button_text_padding=10)

    choice_btn_4 = Button((260 * width_scale),
                          (390 * height_scale), button_image_solid, loaded_hover_image_list, width_scale,
                          'Choice 3', text_color=(20, 20, 20), button_text_padding=10)

    # Create character objects
    character = Character(screen_width // 2, screen_height // 2, screen_width, screen_height)
    chasing_character = Character(screen_width // 3, screen_height // 3, screen_width, screen_height, enemy=True)

    # Initialize miscellaneous operators, checkers, lists
    last_enemy_creation_time = datetime.datetime.now()
    enemies = [chasing_character]
    random_number_generator = None

    # Initialize GameState class for handling different game_states
    game_state_object = GameState(screen, settings, background_manager,
                                  background_manager_loading, text_btn,
                                  username_input_box, username_ask_btn, choice_btn_1,
                                  choice_btn_2, choice_btn_3, choice_btn_4, user_name)

    running = True

    while running:
        choice_made = False

        if game_state == GameStateName.LAIPTINE_SCENE_2:
            random_number_generator = randint(1, 10)

        if game_state == GameStateName.WORLD_MOVEMENT or GameStateName.NIGHTMARE_WORLD_MOVEMENT:
            keys = pygame.key.get_pressed()
            dx, dy = 0, 0
            if keys[pygame.K_LEFT]:
                dx = -5 * width_scale  # Move left
            if keys[pygame.K_RIGHT]:
                dx = 5 * width_scale  # Move right
            if keys[pygame.K_UP]:
                dy = -5 * width_scale  # Move up
            if keys[pygame.K_DOWN]:
                dy = 5 * width_scale  # Move down
            if keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT]:
                dx = -15 * width_scale  # Move left FASTER
            if keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT]:
                dx = 15 * width_scale  # Move right FASTER
            if keys[pygame.K_UP] and keys[pygame.K_LSHIFT]:
                dy = -15 * width_scale  # Move up FASTER
            if keys[pygame.K_DOWN] and keys[pygame.K_LSHIFT]:
                dy = 15 * width_scale  # Move down FASTER

            if game_state == GameStateName.WORLD_MOVEMENT:
                # Clear screen
                screen.fill((0, 0, 0))
                # Update character position
                character.move(dx, dy)
                background_manager.update_image_path('resources/main_map/day_exclamations.jpg')
                background_manager.draw_background(screen)
                character.draw(screen)
                background_manager.update_image_path('resources/main_map/trees.png')
                background_manager.draw_background(screen)
                background_manager.update_image_path('resources/main_map/clouds.png')
                background_manager.move_from_left_to_right(screen, settings)

                # if character moves to a specific coordinate
                if when_character_in_specific_coords(width_scale,
                                                     height_scale,
                                                     character,
                                                     (730, 780),
                                                     (30, 80)):
                    text_btn.text_box_appear(screen)
                    text_btn.update_text('')
                    text_btn.render_multiline_text('Would you like to Enter the Store?\n"Press "Y" to Enter',
                                                   screen)
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_y]:
                        game_state = GameStateName.STORE_SCENE_1

                if when_character_in_specific_coords(width_scale,
                                                     height_scale,
                                                     character,
                                                     (370, 390),
                                                     (270, 320)):
                    text_btn.text_box_appear(screen)
                    text_btn.update_text('')
                    text_btn.render_multiline_text('Go back home?\n"Press "Y" to Enter"',
                                                   screen)
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_y]:
                        game_state = GameStateName.NARVELIS_SCENE_23

            elif game_state == GameStateName.NIGHTMARE_WORLD_MOVEMENT:
                enemy_char_pos = None
                # Clear screen
                screen.fill((0, 0, 0))
                # Update character position
                character.move(dx, dy)
                main_char_pos = character.return_position()

                # Draw elements
                background_manager.update_image_path('resources/main_map/night.jpg')
                background_manager.draw_background(screen)
                character.draw(screen)

                # Update existing enemies
                for enemy in enemies:
                    enemy_char_pos = enemy.return_position()
                    enemy.chase(main_char_pos[0], main_char_pos[1], chase_speed=3)
                    enemy.draw(screen)

                # Create a new enemy every 10 seconds
                current_time = datetime.datetime.now()
                if (current_time - last_enemy_creation_time).total_seconds() >= 10:
                    chasing_character = Character(screen_width // 3, screen_height // 3, screen_width, screen_height,
                                                  enemy=True)
                    enemies.append(chasing_character)
                    last_enemy_creation_time = current_time

                if main_char_pos == enemy_char_pos:
                    game_state = GameStateName.GAME_OVER

                # if character moves to a specific coordinate
                if when_character_in_specific_coords(width_scale,
                                                     height_scale,
                                                     character,
                                                     (730, 780),
                                                     (30, 80)):
                    text_btn.text_box_appear(screen)
                    text_btn.update_text('')
                    text_btn.render_multiline_text('Would you like to SAVE YOURSELF NOW?\n'
                                                   'Press "Y" to YES YES YES PLEASE SO SPOOKY',
                                                   screen)
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_y]:
                        game_state = GameStateName.BEDROOM_SCENE_12

        for event in pygame.event.get():
            # Mouse coordinates printing
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print("Mouse clicked at:", mouse_pos)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            # Main Button clicks (save, load, menu)
            if save_btn.is_clicked(event):
                savestate.save_game(f"{game_state}", user_name, items=items)
            if load_btn.is_clicked(event):
                last_gamestate, last_player_name, _items = savestate.get_last_save()
                items = []
                for item in _items:
                    for deeper_item_because_theres_a_tuple_inside_as_well_lol in item:
                        items.append(deeper_item_because_theres_a_tuple_inside_as_well_lol)
                print(items)
                if last_gamestate and last_player_name:
                    start(screen, clock, settings, background_manager_loading, background_manager, button_image,
                          button_image_solid,
                          loaded_hover_image_list,
                          save_state=last_gamestate, player_name=last_player_name, items=items)
                    return
            if menu_btn.is_clicked(event):
                return

            # Username input handling
            if game_state == GameStateName.INTRO_INPUT:
                username_input_box.handle_event(event)
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                    game_state = GameStateName.MENU

            # Game state specific choice button handling
            choice_made, game_state, items = game_state_object.handle_choice_button_game_states(
                game_state, event, choice_made,
                items,
                character)

            # Space or Mouse click events for advancing the game state
            if not choice_made and (event.type == pygame.MOUSEBUTTONDOWN or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)):
                game_state, user_name, items = game_state_object.handle_game_state(
                    game_state, random_number_generator, user_name, character, items)
                if game_state is None and user_name is None:
                    return

        # Screen drawing based on game state
        game_state_object.handle_game_state_drawing(game_state, items)

        # Update the display, continously draw save, load, menu buttons and check their hovers
        # background_manager.draw_filter(screen)
        if not game_state == GameStateName.GAME_OVER or not game_state == GameStateName.GAME_COMPLETED:
            save_btn.draw(screen)
            load_btn.draw(screen)
            menu_btn.draw(screen)
            save_btn.check_hover(screen)
            load_btn.check_hover(screen)
            menu_btn.check_hover(screen)
        pygame.display.flip()
        clock.tick(FPS)

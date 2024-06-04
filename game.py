"""
game.py

This module contains the start function, which is responsible for running, managing the main game loop and it's logic.
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


# Starts the main game loop
def start(screen, clock, settings, background_manager_loading, background_manager,
          save_state=GameStateName.LOADING_SCREEN, player_name=USER_NAME):
    # Setup screen resolution and scaling
    screen_width, screen_height = settings.current_resolution
    original_width, original_height = RESOLUTIONS[0]
    width_scale = screen_width / original_width
    height_scale = screen_height / original_height

    # Initialize game state and player name
    game_state = save_state
    user_name = player_name

    # Create button objects
    text_btn = Button(80 * width_scale,
                      350 * height_scale,
                      '', button_size=(652 * width_scale, 252 * height_scale),
                      font_path=TEXT_FONT_PATH,
                      text_color=(20, 20, 20),
                      button_text_padding=20)

    multi_text_btn = Button(130 * width_scale,
                            400 * height_scale,
                            '', button_size=(652 * width_scale, 252 * height_scale),
                            font_path=TEXT_FONT_PATH,
                            text_color=(20, 20, 20),
                            button_text_padding=20)

    username_input_box = InputBox(240 * width_scale,
                                  515 * height_scale, 300, 200)

    username_ask_btn = Button(80 * width_scale,
                              350 * height_scale,
                              'Please enter your name:',
                              button_size=(652 * width_scale, 252 * height_scale),
                              font_path=TEXT_FONT_PATH,
                              text_color=(20, 20, 20),
                              button_text_padding=20)

    save_btn = Button(650 * width_scale,
                      1 * height_scale,
                      'Save game',
                      button_size=(150 * width_scale, 25 * height_scale),
                      text_color=(20, 20, 20),
                      button_text_padding=20,
                      button_file_path='resources/button/button_hover_animation/14.png')

    load_btn = Button(500 * width_scale,
                      1 * height_scale,
                      'Load game',
                      button_size=(150 * width_scale, 25 * height_scale),
                      text_color=(20, 20, 20),
                      button_text_padding=20,
                      button_file_path='resources/button/button_hover_animation/14.png')

    menu_btn = Button(350 * width_scale,
                      1 * height_scale,
                      'Menu',
                      button_size=(150 * width_scale, 25 * height_scale),
                      text_color=(20, 20, 20), button_text_padding=90,
                      button_file_path='resources/button/button_hover_animation/14.png')

    choice_btn_1 = Button((260 * width_scale),
                          (180 * height_scale),
                          'Choice 1', text_color=(20, 20, 20), button_text_padding=10,
                          button_file_path='resources/button/button_hover_animation/14.png')

    choice_btn_2 = Button((260 * width_scale),
                          (250 * height_scale),
                          'Choice 2', text_color=(20, 20, 20), button_text_padding=10,
                          button_file_path='resources/button/button_hover_animation/14.png')

    choice_btn_3 = Button((260 * width_scale),
                          (320 * height_scale),
                          'Choice 3', text_color=(20, 20, 20), button_text_padding=10,
                          button_file_path='resources/button/button_hover_animation/14.png')

    choice_btn_4 = Button((260 * width_scale),
                          (390 * height_scale),
                          'Choice 3', text_color=(20, 20, 20), button_text_padding=10,
                          button_file_path='resources/button/button_hover_animation/14.png')

    # Create character objects
    character = Character(screen_width // 2, screen_height // 2, screen_width, screen_height)
    chasing_character = Character(screen_width // 3, screen_height // 3, screen_width, screen_height, enemy=True)

    # Initialize miscelenious operators, checkers, lists
    pigeon_money_taken = False
    camel_blue_received = False
    last_enemy_creation_time = datetime.datetime.now()
    enemies = [chasing_character]

    # Initialize GameState class for handling different game_states
    game_state_object = GameState(screen, settings, background_manager,
                                  background_manager_loading, text_btn, multi_text_btn,
                                  username_input_box, username_ask_btn, choice_btn_1,
                                  choice_btn_2, choice_btn_3, choice_btn_4, user_name)

    running = True

    while running:
        random_number_generator = randint(1, 10)
        choice_made = False

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
                    multi_text_btn.render_multiline_text('Would you like to Enter the Store?\n"Press "Y" to Enter',
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
                    multi_text_btn.render_multiline_text('Go back home?\n"Press "Y" to Enter"',
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
                    multi_text_btn.render_multiline_text('Would you like to SAVE YOURSELF NOW?\n'
                                                         'Press "Y" to YES YES YES PLEASE',
                                                         screen)
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_y]:
                        game_state = GameStateName.BEDROOM_SCENE_12

        for event in pygame.event.get():
            # mouse coordinates printing
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print("Mouse clicked at:", mouse_pos)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            # Button clicks
            if save_btn.is_clicked(event):
                savestate.save_game(f"{game_state}", user_name)
            if load_btn.is_clicked(event):
                last_gamestate, last_player_name = savestate.get_last_save()
                if last_gamestate and last_player_name:
                    start(screen, clock, settings, background_manager_loading, background_manager,
                          save_state=last_gamestate, player_name=last_player_name)
                    return
            if menu_btn.is_clicked(event):
                return

            # Username input handling
            if game_state == GameStateName.INTRO_INPUT:
                username_input_box.handle_event(event)
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                    game_state = GameStateName.MENU

            # Game state specific button handling
            if game_state in [GameStateName.BEDROOM_SCENE_3, GameStateName.BEDROOM_SCENE_5]:
                if choice_btn_1.is_clicked(event):
                    game_state = GameStateName.BALCONY_SCENE_1
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_2.is_clicked(event):
                    game_state = GameStateName.KITCHEN_SCENE_1
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_3.is_clicked(event):
                    game_state = GameStateName.BATHROOM_SCENE_1
                    text_btn.reset_animation()
                    choice_made = True

            if game_state == GameStateName.BALCONY_SCENE_3:
                if choice_btn_1.is_clicked(event):
                    game_state = GameStateName.BEDROOM_SCENE_4
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_2.is_clicked(event):
                    game_state = GameStateName.BALCONY_SCENE_4
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_3.is_clicked(event):
                    game_state = GameStateName.BALCONY_SCENE_5
                    text_btn.reset_animation()
                    choice_made = True

            if game_state == GameStateName.KITCHEN_SCENE_4:
                if choice_btn_1.is_clicked(event):
                    game_state = GameStateName.KITCHEN_SCENE_5
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_2.is_clicked(event):
                    game_state = GameStateName.KITCHEN_SCENE_7
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_3.is_clicked(event):
                    game_state = GameStateName.LAIPTINE_SCENE_1
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_4.is_clicked(event):
                    game_state = GameStateName.BEDROOM_SCENE_4
                    text_btn.reset_animation()
                    choice_made = True

            if game_state == GameStateName.NARVELIS_SCENE_7:
                if choice_btn_1.is_clicked(event):
                    game_state = GameStateName.NARVELIS_SCENE_15
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_2.is_clicked(event):
                    game_state = GameStateName.NARVELIS_SCENE_8
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_3.is_clicked(event):
                    game_state = GameStateName.WORLD_MOVEMENT
                    text_btn.reset_animation()
                    choice_made = True

            if game_state == GameStateName.STORE_SCENE_6:
                if choice_btn_1.is_clicked(event):
                    if pigeon_money_taken:
                        game_state = GameStateName.STORE_SCENE_26
                    else:
                        game_state = GameStateName.STORE_SCENE_7
                        text_btn.reset_animation()
                        choice_made = True
                elif choice_btn_2.is_clicked(event):
                    character.move(-20, 0)
                    game_state = GameStateName.WORLD_MOVEMENT
                    text_btn.reset_animation()
                    choice_made = True

            if game_state == GameStateName.STORE_SCENE_12:
                if choice_btn_1.is_clicked(event):
                    character.move(-20, 0)
                    game_state = GameStateName.WORLD_MOVEMENT
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_2.is_clicked(event):
                    game_state = GameStateName.STORE_SCENE_13
                    text_btn.reset_animation()
                    choice_made = True

            if game_state == GameStateName.STORE_SCENE_20:
                if choice_btn_1.is_clicked(event):
                    game_state = GameStateName.WORLD_MOVEMENT
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_2.is_clicked(event):
                    game_state = GameStateName.STORE_SCENE_21
                    text_btn.reset_animation()
                    choice_made = True

            if game_state == GameStateName.BEDROOM_SCENE_11:
                if choice_btn_1.is_clicked(event):
                    game_state = GameStateName.BALCONY_SCENE_7
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_2.is_clicked(event):
                    game_state = GameStateName.KITCHEN_SCENE_9
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_3.is_clicked(event):
                    game_state = GameStateName.BATHROOM_SCENE_3
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_4.is_clicked(event):
                    game_state = GameStateName.SLEEP_SCENE_1
                    text_btn.reset_animation()
                    choice_made = True

            if game_state == GameStateName.KITCHEN_SCENE_10:
                if choice_btn_1.is_clicked(event):
                    game_state = GameStateName.KITCHEN_SCENE_11
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_2.is_clicked(event):
                    game_state = GameStateName.WORLD_MOVEMENT
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_3.is_clicked(event):
                    game_state = GameStateName.BEDROOM_SCENE_11
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_4.is_clicked(event):
                    game_state = GameStateName.KITCHEN_SCENE_12
                    text_btn.reset_animation()
                    choice_made = True

            if game_state == GameStateName.BALCONY_SCENE_8:
                if choice_btn_1.is_clicked(event):
                    game_state = GameStateName.BEDROOM_SCENE_11
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_2.is_clicked(event):
                    if camel_blue_received:
                        game_state = GameStateName.BALCONY_SCENE_12
                        text_btn.reset_animation()
                        choice_made = True
                    else:
                        game_state = GameStateName.BALCONY_SCENE_9
                        text_btn.reset_animation()
                        choice_made = True
                elif choice_btn_3.is_clicked(event):
                    game_state = GameStateName.BALCONY_SCENE_5
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_4.is_clicked(event):
                    if pigeon_money_taken:
                        text_btn.text_box_appear(screen)
                        text_btn.update_text('There is no more money in the pigeon nest')
                    else:
                        game_state = GameStateName.BALCONY_SCENE_10
                        choice_made = True
                    text_btn.reset_animation()

            if game_state == GameStateName.BATHROOM_SCENE_2:
                if choice_btn_1.is_clicked(event):
                    game_state = GameStateName.BEDROOM_SCENE_4
                    text_btn.reset_animation()
                    choice_made = True

            if game_state == GameStateName.BATHROOM_SCENE_4:
                if choice_btn_1.is_clicked(event):
                    game_state = GameStateName.BEDROOM_SCENE_11
                    text_btn.reset_animation()
                    choice_made = True

            # Space or Mouse click events for advancing the game state
            if not choice_made and (event.type == pygame.MOUSEBUTTONDOWN or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)):

                game_state = game_state_object.handle_game_state(game_state, random_number_generator)

                if game_state == GameStateName.MENU:
                    user_name = username_input_box.username if username_input_box.username else player_name
                    game_state = GameStateName.INTRO_SCENE_1
                    text_btn.reset_animation()
                elif game_state == GameStateName.GAME_OVER:
                    text_btn.reset_animation()
                    savestate.delete_user(user_name)
                    return
                elif game_state == GameStateName.STORE_SCENE_29:
                    camel_blue_received = True
                    game_state = GameStateName.WORLD_MOVEMENT
                elif game_state == GameStateName.BALCONY_SCENE_11:
                    pigeon_money_taken = True
                    game_state = GameStateName.BALCONY_SCENE_8
                elif game_state == GameStateName.GAME_COMPLETED:
                    return

        # Screen drawing based on game state
        game_state_object.handle_game_state_drawing(game_state)

        # Update the display, continously draw save, load, menu buttons and check their hovers
        if game_state == GameStateName.BALCONY_SCENE_8:
            if not pigeon_money_taken:
                choice_btn_4.draw(screen)
                choice_btn_4.check_hover(screen)
        background_manager.draw_filter(screen)
        if not game_state == GameStateName.GAME_OVER or not game_state == GameStateName.GAME_COMPLETED:
            save_btn.draw(screen)
            load_btn.draw(screen)
            menu_btn.draw(screen)
            save_btn.check_hover(screen)
            load_btn.check_hover(screen)
            menu_btn.check_hover(screen)
        pygame.display.flip()
        clock.tick(FPS)

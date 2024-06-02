import sys
import time
from random import randint

import pygame

from ui.button import Button
from ui.constants import FPS, GameState, TEXT_FONT_PATH, LOADING_IMAGE_PATH_LIST, RESOLUTIONS, CHOICED_GAME_STATE_LIST
from ui.user_input_box import InputBox
from save_states import save_game, load_game
from character.character import Character
from ui.utilities import when_character_in_specific_coords
from ui.game_text import story_text


def start(screen, clock, settings, background_manager_loading, background_manager,
          save_state=GameState.LOADING_SCREEN, player_name='Player'):
    screen_width, screen_height = settings.current_resolution
    original_width, original_height = RESOLUTIONS[0]
    width_scale = screen_width / original_width
    height_scale = screen_height / original_height

    game_state = save_state
    user_name = player_name

    text_btn = Button((80 * width_scale),
                      (350 * height_scale),
                      '', button_size=(652 * width_scale, 252 * height_scale),
                      font_path=TEXT_FONT_PATH,
                      text_color=(20, 20, 20),
                      button_text_padding=20)
    multi_text_btn = Button((130 * width_scale),
                            (400 * height_scale),
                            '', button_size=(652 * width_scale, 252 * height_scale),
                            font_path=TEXT_FONT_PATH,
                            text_color=(20, 20, 20),
                            button_text_padding=20)
    username_input_box = InputBox((240 * width_scale),
                                  (515 * height_scale), 300, 200)
    username_ask_btn = Button((80 * width_scale),
                              (350 * height_scale),
                              'Please enter your name:',
                              button_size=(652 * width_scale, 252 * height_scale),
                              font_path=TEXT_FONT_PATH,
                              text_color=(20, 20, 20),
                              button_text_padding=20)
    save_btn = Button((650 * width_scale),
                      (1 * height_scale),
                      'Save game',
                      button_size=(150 * width_scale, 25 * height_scale),
                      text_color=(20, 20, 20),
                      button_text_padding=20,
                      button_file_path='resources/button/button_hover_animation/14.png')
    load_btn = Button((500 * width_scale),
                      (1 * height_scale),
                      'Load game',
                      button_size=(150 * width_scale, 25 * height_scale),
                      text_color=(20, 20, 20),
                      button_text_padding=20,
                      button_file_path='resources/button/button_hover_animation/14.png')
    menu_btn = Button((350 * width_scale),
                      (1 * height_scale),
                      'Menu',
                      button_size=(150 * width_scale, 25 * height_scale),
                      text_color=(20, 20, 20), button_text_padding=90,
                      button_file_path='resources/button/button_hover_animation/14.png')
    character = Character(screen_width // 2, screen_height // 2, screen_width, screen_height)
    choice_btn_1 = Button((260 * width_scale),
                          (180 * height_scale),
                          'Choice 1', text_color=(20, 20, 20))
    choice_btn_2 = Button((260 * width_scale),
                          (250 * height_scale),
                          'Choice 2', text_color=(20, 20, 20))
    choice_btn_3 = Button((260 * width_scale),
                          (320 * height_scale),
                          'Choice 3', text_color=(20, 20, 20))
    choice_btn_4 = Button((260 * width_scale),
                          (390 * height_scale),
                          'Choice 3', text_color=(20, 20, 20))

    running = True
    while running:
        random_number_generator = randint(1,10)
        choice_made = False
        if game_state == GameState.WORLD_MOVEMENT:
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
            # Clear screen
            screen.fill((0, 0, 0))
            # Update character position
            character.move(dx, dy)
            background_manager.update_image_path('resources/main_map/day.jpg')
            background_manager.draw_background(screen)
            character.draw(screen)
            background_manager.update_image_path('resources/main_map/trees.png')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/main_map/clouds1.png')
            background_manager.move_from_left_to_right(screen, settings)

            # if character moves to a specific coordinate
            if when_character_in_specific_coords(width_scale,
                                                 height_scale,
                                                 character,
                                                 (735, 770),
                                                 (65, 100)):
                game_state = GameState.STORE_SCENE_1

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
                save_game({'game_state': game_state, 'username': user_name})
            if load_btn.is_clicked(event):
                loaded_state = load_game()
                if loaded_state:
                    game_state = loaded_state['game_state']
                    user_name = loaded_state.get('username')
            if menu_btn.is_clicked(event):
                return

            # Username input handling
            if game_state == GameState.INTRO_INPUT:
                username_input_box.handle_event(event)
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                    game_state = GameState.MENU

            # Game state specific button handling
            if game_state in [GameState.BEDROOM_SCENE_3, GameState.BEDROOM_SCENE_5]:
                if choice_btn_1.is_clicked(event):
                    game_state = GameState.BALCONY_SCENE_1
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_2.is_clicked(event):
                    game_state = GameState.KITCHEN_SCENE_1
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_3.is_clicked(event):
                    game_state = GameState.BATHROOM_SCENE_1
                    text_btn.reset_animation()
                    choice_made = True

            if game_state == GameState.BALCONY_SCENE_3:
                if choice_btn_1.is_clicked(event):
                    game_state = GameState.BEDROOM_SCENE_4
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_2.is_clicked(event):
                    game_state = GameState.BALCONY_SCENE_4
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_3.is_clicked(event):
                    game_state = GameState.BALCONY_SCENE_5
                    text_btn.reset_animation()
                    choice_made = True

            if game_state == GameState.KITCHEN_SCENE_4:
                if choice_btn_1.is_clicked(event):
                    game_state = GameState.KITCHEN_SCENE_5
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_2.is_clicked(event):
                    game_state = GameState.KITCHEN_SCENE_7
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_3.is_clicked(event):
                    game_state = GameState.LAIPTINE_SCENE_1
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_4.is_clicked(event):
                    game_state = GameState.BEDROOM_SCENE_4
                    text_btn.reset_animation()
                    choice_made = True

            if game_state == GameState.NARVELIS_SCENE_7:
                if choice_btn_1.is_clicked(event):
                    game_state = GameState.NARVELIS_SCENE_15
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_2.is_clicked(event):
                    game_state = GameState.NARVELIS_SCENE_8
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_3.is_clicked(event):
                    game_state = GameState.WORLD_MOVEMENT
                    text_btn.reset_animation()
                    choice_made = True

            if game_state == GameState.STORE_SCENE_6:
                if choice_btn_1.is_clicked(event):
                    game_state = GameState.STORE_SCENE_7
                    text_btn.reset_animation()
                    choice_made = True
                elif choice_btn_2.is_clicked(event):
                    game_state = GameState.WORLD_MOVEMENT
                    text_btn.reset_animation()
                    choice_made = True

            # Space or Mouse click events for advancing the game state
            if not choice_made and (event.type == pygame.MOUSEBUTTONDOWN or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)):
                if game_state == GameState.LOADING_SCREEN:
                    game_state = GameState.INTRO_INPUT
                elif game_state == GameState.MENU:
                    game_state = GameState.INTRO_SCENE_1
                    text_btn.reset_animation()
                elif game_state == GameState.INTRO_SCENE_1:
                    game_state = GameState.INTRO_SCENE_2
                    text_btn.reset_animation()
                elif game_state == GameState.INTRO_SCENE_2:
                    game_state = GameState.INTRO_SCENE_3
                    text_btn.reset_animation()
                elif game_state == GameState.INTRO_SCENE_3:
                    game_state = GameState.INTRO_SCENE_4
                    text_btn.reset_animation()
                elif game_state == GameState.INTRO_SCENE_4:
                    game_state = GameState.INTRO_SCENE_5
                    text_btn.reset_animation()
                elif game_state == GameState.INTRO_SCENE_5:
                    game_state = GameState.BEDROOM_SCENE_1
                    text_btn.reset_animation()
                elif game_state == GameState.BEDROOM_SCENE_1:
                    game_state = GameState.BEDROOM_SCENE_2
                    text_btn.reset_animation()
                elif game_state == GameState.BEDROOM_SCENE_2:
                    game_state = GameState.BEDROOM_SCENE_3
                    text_btn.reset_animation()
                elif game_state == GameState.BEDROOM_SCENE_4:
                    game_state = GameState.BEDROOM_SCENE_5
                    text_btn.reset_animation()
                elif game_state == GameState.BALCONY_SCENE_1:
                    game_state = GameState.BALCONY_SCENE_2
                    text_btn.reset_animation()
                elif game_state == GameState.BALCONY_SCENE_2:
                    game_state = GameState.BALCONY_SCENE_3
                    text_btn.reset_animation()
                elif game_state == GameState.BALCONY_SCENE_4:
                    game_state = GameState.BALCONY_SCENE_2
                    text_btn.reset_animation()
                elif game_state == GameState.BALCONY_SCENE_5:
                    game_state = GameState.GAME_OVER
                    text_btn.reset_animation()
                elif game_state == GameState.GAME_OVER:
                    text_btn.reset_animation()
                    return
                elif game_state == GameState.KITCHEN_SCENE_1:
                    game_state = GameState.KITCHEN_SCENE_2
                    text_btn.reset_animation()
                elif game_state == GameState.KITCHEN_SCENE_2:
                    game_state = GameState.KITCHEN_SCENE_3
                    text_btn.reset_animation()
                elif game_state == GameState.KITCHEN_SCENE_3:
                    game_state = GameState.KITCHEN_SCENE_4
                    text_btn.reset_animation()
                elif game_state == GameState.KITCHEN_SCENE_5:
                    game_state = GameState.KITCHEN_SCENE_6
                    text_btn.reset_animation()
                elif game_state == GameState.KITCHEN_SCENE_6:
                    game_state = GameState.KITCHEN_SCENE_4
                    text_btn.reset_animation()
                elif game_state == GameState.KITCHEN_SCENE_7:
                    game_state = GameState.KITCHEN_SCENE_8
                    text_btn.reset_animation()
                elif game_state == GameState.KITCHEN_SCENE_8:
                    game_state = GameState.KITCHEN_SCENE_4
                    text_btn.reset_animation()
                elif game_state == GameState.LAIPTINE_SCENE_1:
                    game_state = GameState.LAIPTINE_SCENE_2
                    text_btn.reset_animation()
                elif game_state == GameState.LAIPTINE_SCENE_2:
                    if random_number_generator < 5:
                        game_state = GameState.LAIPTINE_SCENE_3
                    else:
                        game_state = GameState.LAIPTINE_SCENE_4
                    text_btn.reset_animation()
                elif game_state == GameState.LAIPTINE_SCENE_3:
                    game_state = GameState.NARVELIS_SCENE_1
                    text_btn.reset_animation()
                elif game_state == GameState.LAIPTINE_SCENE_4:
                    game_state = GameState.LAIPTINE_SCENE_5
                    text_btn.reset_animation()
                elif game_state == GameState.LAIPTINE_SCENE_5:
                    game_state = GameState.LAIPTINE_SCENE_6
                    text_btn.reset_animation()
                elif game_state == GameState.LAIPTINE_SCENE_6:
                    game_state = GameState.NARVELIS_SCENE_1
                    text_btn.reset_animation()
                elif game_state == GameState.NARVELIS_SCENE_1:
                    game_state = GameState.NARVELIS_SCENE_2
                    text_btn.reset_animation()
                elif game_state == GameState.NARVELIS_SCENE_1:
                    game_state = GameState.NARVELIS_SCENE_2
                    text_btn.reset_animation()
                elif game_state == GameState.NARVELIS_SCENE_2:
                    game_state = GameState.NARVELIS_SCENE_3
                    text_btn.reset_animation()
                elif game_state == GameState.NARVELIS_SCENE_3:
                    game_state = GameState.NARVELIS_SCENE_4
                    text_btn.reset_animation()
                elif game_state == GameState.NARVELIS_SCENE_4:
                    game_state = GameState.NARVELIS_SCENE_5
                    text_btn.reset_animation()
                elif game_state == GameState.NARVELIS_SCENE_5:
                    game_state = GameState.NARVELIS_SCENE_6
                    text_btn.reset_animation()
                elif game_state == GameState.NARVELIS_SCENE_6:
                    game_state = GameState.NARVELIS_SCENE_7
                    text_btn.reset_animation()
                elif game_state == GameState.NARVELIS_SCENE_8:
                    game_state = GameState.NARVELIS_SCENE_9
                    text_btn.reset_animation()
                elif game_state == GameState.NARVELIS_SCENE_9:
                    game_state = GameState.NARVELIS_SCENE_10
                    text_btn.reset_animation()
                elif game_state == GameState.NARVELIS_SCENE_10:
                    game_state = GameState.NARVELIS_SCENE_7
                elif game_state == GameState.NARVELIS_SCENE_11:
                    game_state = GameState.NARVELIS_SCENE_12
                elif game_state == GameState.NARVELIS_SCENE_13:
                    game_state = GameState.NARVELIS_SCENE_14
                elif game_state == GameState.NARVELIS_SCENE_15:
                    game_state = GameState.NARVELIS_SCENE_16
                elif game_state == GameState.NARVELIS_SCENE_16:
                    game_state = GameState.NARVELIS_SCENE_17
                elif game_state == GameState.NARVELIS_SCENE_17:
                    game_state = GameState.NARVELIS_SCENE_18
                elif game_state == GameState.NARVELIS_SCENE_18:
                    game_state = GameState.NARVELIS_SCENE_19
                elif game_state == GameState.NARVELIS_SCENE_19:
                    game_state = GameState.NARVELIS_SCENE_20
                elif game_state == GameState.NARVELIS_SCENE_20:
                    game_state = GameState.NARVELIS_SCENE_21
                elif game_state == GameState.NARVELIS_SCENE_21:
                    game_state = GameState.NARVELIS_SCENE_22
                elif game_state == GameState.NARVELIS_SCENE_22:
                    game_state = GameState.NARVELIS_SCENE_7
                elif game_state == GameState.STORE_SCENE_1:
                    game_state = GameState.STORE_SCENE_2
                elif game_state == GameState.STORE_SCENE_2:
                    game_state = GameState.STORE_SCENE_3
                elif game_state == GameState.STORE_SCENE_3:
                    game_state = GameState.STORE_SCENE_4
                elif game_state == GameState.STORE_SCENE_5:
                    game_state = GameState.STORE_SCENE_6
                elif game_state == GameState.STORE_SCENE_7:
                    game_state = GameState.STORE_SCENE_8


        # Screen drawing based on game state
        if game_state == GameState.INTRO_INPUT:
            screen.fill((200, 200, 200))
            username_ask_btn.text_box_appear(screen)
            username_input_box.update()
            username_input_box.draw(screen)
        elif game_state == GameState.LOADING_SCREEN:
            background_manager_loading.update_screen_size(settings.current_resolution, LOADING_IMAGE_PATH_LIST)
            background_manager_loading.update_background_slideshow()
            background_manager_loading.draw_background(screen)
        elif game_state == GameState.MENU:
            player_name = username_input_box.username if username_input_box.username else player_name
            background_manager.update_image_path('resources/main_map/night.jpg')
            background_manager.draw_background(screen)
        elif game_state == GameState.INTRO_SCENE_1:
            text_btn.text_box_appear(screen)
            text_btn.update_text(f'Nice to meet you, {player_name}')
        elif game_state == GameState.INTRO_SCENE_2:
            text_btn.text_box_appear(screen)
            text_btn.update_text('Enjoy! :)')
        elif game_state == GameState.INTRO_SCENE_3:
            screen.fill((0, 0, 0))  # Clear the screen with black before drawing
            background_manager.update_image_path('resources/main_map/night.jpg')
            background_manager.draw_background(screen)
        elif game_state == GameState.INTRO_SCENE_4:
            text_btn.text_box_appear(screen)
            text_btn.update_text('')
            multi_text_btn.render_multiline_text('You can control your character with the arrow keys.\n'
                                                 'Hold "L_Shift" to sprint!', screen, color=(255, 40, 40))
        elif game_state == GameState.INTRO_SCENE_5:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/main_map/day.jpg')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text('Somewhere in a fictional town, fictional country.')
        elif game_state == GameState.BEDROOM_SCENE_1:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/bedroom.jpg')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text(story_text.get('HomeRoom').get('story')[0])
        elif game_state == GameState.BEDROOM_SCENE_2:
            text_btn.text_box_appear(screen)
            text_btn.update_text('')
            multi_text_btn.render_multiline_text(story_text.get('HomeRoom').get('story')[1], screen)
        elif game_state == GameState.BEDROOM_SCENE_3:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/bedroom.jpg')
            background_manager.draw_background(screen)
            choice_btn_1.update_text(story_text.get('HomeRoom').get('selection')[0])
            choice_btn_2.update_text(story_text.get('HomeRoom').get('selection')[1])
            choice_btn_3.update_text(story_text.get('HomeRoom').get('selection')[2])
            choice_btn_1.draw(screen)
            choice_btn_1.check_hover(screen)
            choice_btn_2.draw(screen)
            choice_btn_2.check_hover(screen)
            choice_btn_3.draw(screen)
            choice_btn_3.check_hover(screen)
        elif game_state == GameState.BEDROOM_SCENE_4:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/bedroom.jpg')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text(story_text.get('HomeRoom').get('story')[2])
        elif game_state == GameState.BEDROOM_SCENE_5:
            screen.fill((0, 0, 0))
            background_manager.draw_background(screen)
            choice_btn_1.update_text(story_text.get('HomeRoom').get('selection')[0])
            choice_btn_2.update_text(story_text.get('HomeRoom').get('selection')[1])
            choice_btn_3.update_text(story_text.get('HomeRoom').get('selection')[2])
            choice_btn_1.draw(screen)
            choice_btn_1.check_hover(screen)
            choice_btn_2.draw(screen)
            choice_btn_2.check_hover(screen)
            choice_btn_3.draw(screen)
            choice_btn_3.check_hover(screen)
        elif game_state == GameState.BALCONY_SCENE_1:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/balcony.jpg')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text(story_text.get('HomeBalcony').get('story')[0])
        elif game_state == GameState.BALCONY_SCENE_2:
            text_btn.text_box_appear(screen)
            text_btn.update_text('')
            multi_text_btn.render_multiline_text(story_text.get('HomeBalcony').get('story')[1], screen)
        elif game_state == GameState.BALCONY_SCENE_3:
            screen.fill((0, 0, 0))
            background_manager.draw_background(screen)
            choice_btn_1.update_text(story_text.get('HomeBalcony').get('selection')[0])
            choice_btn_2.update_text(story_text.get('HomeBalcony').get('selection')[1])
            choice_btn_3.update_text(story_text.get('HomeBalcony').get('selection')[2])
            choice_btn_1.draw(screen)
            choice_btn_1.check_hover(screen)
            choice_btn_2.draw(screen)
            choice_btn_2.check_hover(screen)
            choice_btn_3.draw(screen)
            choice_btn_3.check_hover(screen)
        elif game_state == GameState.BALCONY_SCENE_4:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/balcony.jpg')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text(story_text.get('HomeBalcony').get('story')[2])
        elif game_state == GameState.BALCONY_SCENE_5:
            screen.fill((0, 0, 0))
            text_btn.text_box_appear(screen)
            text_btn.update_text('')
            multi_text_btn.render_multiline_text(story_text.get('HomeBalcony').get('story')[3], screen)
        elif game_state == GameState.GAME_OVER:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/game_over.jpg')
            background_manager.draw_background(screen)
        elif game_state == GameState.KITCHEN_SCENE_1:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/kitchen.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/mom3.png')
            background_manager.draw_background(screen)
        elif game_state == GameState.KITCHEN_SCENE_2:
            text_btn.text_box_appear(screen)
            multi_text_btn.render_multiline_text(story_text.get('HomeKitchen').get('story')[0], screen)
        elif game_state == GameState.KITCHEN_SCENE_3:
            text_btn.text_box_appear(screen)
            multi_text_btn.render_multiline_text(story_text.get('HomeKitchen').get('story')[1], screen)
        elif game_state == GameState.KITCHEN_SCENE_4:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/kitchen.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/mom2.png')
            background_manager.draw_background(screen)
            choice_btn_1.update_text(story_text.get('HomeKitchen').get('selection')[0])
            choice_btn_2.update_text(story_text.get('HomeKitchen').get('selection')[1])
            choice_btn_3.update_text(story_text.get('HomeKitchen').get('selection')[2])
            choice_btn_4.update_text(story_text.get('HomeKitchen').get('selection')[3])
            choice_btn_1.draw(screen)
            choice_btn_1.check_hover(screen)
            choice_btn_2.draw(screen)
            choice_btn_2.check_hover(screen)
            choice_btn_3.draw(screen)
            choice_btn_3.check_hover(screen)
            choice_btn_4.draw(screen)
            choice_btn_4.check_hover(screen)
        elif game_state == GameState.KITCHEN_SCENE_5:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/kitchen.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/mom3.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text(f"{user_name}: " + story_text.get('HomeKitchen').get('player')[0])
        elif game_state == GameState.KITCHEN_SCENE_6:
            text_btn.text_box_appear(screen)
            text_btn.update_text("Mom: " + story_text.get('HomeKitchen').get('mom')[0])
        elif game_state == GameState.KITCHEN_SCENE_7:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/fridge.jpg')
            background_manager.draw_background(screen)
        elif game_state == GameState.KITCHEN_SCENE_8:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/fridge.jpg')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeKitchen').get('story')[2], screen)
        elif game_state == GameState.LAIPTINE_SCENE_1:
            screen.fill((0, 0, 0))
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeLaiptine').get('story')[0], screen)
        elif game_state == GameState.LAIPTINE_SCENE_2:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/kaimynas.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeLaiptine').get('story')[1], screen)
        elif game_state == GameState.LAIPTINE_SCENE_3:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/kaimynas2.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeLaiptine').get('story')[2], screen)
        elif game_state == GameState.LAIPTINE_SCENE_4:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/kaimynas2.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeLaiptine').get('story')[3], screen)
        elif game_state == GameState.LAIPTINE_SCENE_5:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/kaimynas2.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text(f"{user_name}: " + story_text.get('HomeLaiptine').get('player')[0])
        elif game_state == GameState.LAIPTINE_SCENE_6:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/kaimynas.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text(f"Kaimynas: " + story_text.get('HomeLaiptine').get('kaimynas')[0])
        elif game_state == GameState.NARVELIS_SCENE_1:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text(story_text.get('HomeNarvelis').get('story')[0])
        elif game_state == GameState.NARVELIS_SCENE_2:
            text_btn.text_box_appear(screen)
            text_btn.update_text(story_text.get('HomeNarvelis').get('story')[1])
        elif game_state == GameState.NARVELIS_SCENE_3:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas2.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text(" ")
            multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[2], screen)
        elif game_state == GameState.NARVELIS_SCENE_4:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text(" ")
            multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[3], screen)
        elif game_state == GameState.NARVELIS_SCENE_5:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text(story_text.get('HomeNarvelis').get('story')[4])
        elif game_state == GameState.NARVELIS_SCENE_6:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas2.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text(story_text.get('HomeNarvelis').get('story')[5])
        elif game_state == GameState.NARVELIS_SCENE_7:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            background_manager.draw_background(screen)
            choice_btn_1.update_text(story_text.get('HomeNarvelis').get('selection')[0])
            choice_btn_2.update_text(story_text.get('HomeNarvelis').get('selection')[1])
            choice_btn_3.update_text(story_text.get('HomeNarvelis').get('selection')[2])
            choice_btn_1.draw(screen)
            choice_btn_1.check_hover(screen)
            choice_btn_2.draw(screen)
            choice_btn_2.check_hover(screen)
            choice_btn_3.draw(screen)
            choice_btn_3.check_hover(screen)
        elif game_state == GameState.NARVELIS_SCENE_8:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas2.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[6], screen)
        elif game_state == GameState.NARVELIS_SCENE_9:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[7], screen)
        elif game_state == GameState.NARVELIS_SCENE_10:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[8], screen)
        elif game_state == GameState.NARVELIS_SCENE_11:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[9], screen)
        elif game_state == GameState.NARVELIS_SCENE_12:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[10], screen)
        elif game_state == GameState.NARVELIS_SCENE_13:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[11], screen)
        elif game_state == GameState.NARVELIS_SCENE_14:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas2.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[12], screen)
        elif game_state == GameState.NARVELIS_SCENE_15:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[13], screen)
        elif game_state == GameState.NARVELIS_SCENE_16:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas2.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[14], screen)
        elif game_state == GameState.NARVELIS_SCENE_17:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/playground.jpg')
            background_manager.draw_background(screen)
        elif game_state == GameState.NARVELIS_SCENE_18:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/playground.jpg')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[15], screen)
        elif game_state == GameState.NARVELIS_SCENE_19:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/playground.jpg')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[16], screen)
        elif game_state == GameState.NARVELIS_SCENE_20:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/playground.jpg')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[17], screen)
        elif game_state == GameState.NARVELIS_SCENE_21:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[18], screen)
        elif game_state == GameState.NARVELIS_SCENE_22:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/tupikas2.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[19], screen)
        elif game_state == GameState.STORE_SCENE_1:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/store.jpg')
            background_manager.draw_background(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[0], screen)
        elif game_state == GameState.STORE_SCENE_2:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/store.jpg')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[1], screen)
        elif game_state == GameState.STORE_SCENE_3:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/store.jpg')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[2], screen)
        elif game_state == GameState.STORE_SCENE_4:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/store.jpg')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[3], screen)
        elif game_state == GameState.STORE_SCENE_5:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[4], screen)
        elif game_state == GameState.STORE_SCENE_6:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            background_manager.draw_background(screen)
            choice_btn_1.update_text(story_text.get('Store').get('selection')[0])
            choice_btn_2.update_text(story_text.get('Store').get('selection')[1])
            choice_btn_1.draw(screen)
            choice_btn_1.check_hover(screen)
            choice_btn_2.draw(screen)
            choice_btn_2.check_hover(screen)
        elif game_state == GameState.STORE_SCENE_7:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(f"{user_name}: " + story_text.get('Store').get('player')[0], screen)
        elif game_state == GameState.STORE_SCENE_8:
            screen.fill((0, 0, 0))
            background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            background_manager.draw_background(screen)
            background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            background_manager.draw_background(screen)
            text_btn.text_box_appear(screen)
            text_btn.update_text("")
            multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[5], screen)
















        # Update the display, continously draw save, load, menu buttons and check their hovers
        save_btn.draw(screen)
        load_btn.draw(screen)
        menu_btn.draw(screen)
        save_btn.check_hover(screen)
        load_btn.check_hover(screen)
        menu_btn.check_hover(screen)
        pygame.display.flip()
        clock.tick(FPS)

"""
game_states.py

This module contains class GameState, which handles the drawing and logic of game_states.
"""

from ui.constants import GameStateName, LOADING_IMAGE_PATH_LIST
from ui.game_text import story_text


class GameState:
    """Handles different game states."""

    def __init__(self, screen, settings, background_manager, background_manager_loading,
                 text_btn, multi_text_btn, username_input_box, username_ask_btn,
                 choice_btn_1, choice_btn_2, choice_btn_3, choice_btn_4, user_name):
        self.screen = screen
        self.settings = settings
        self.background_manager = background_manager
        self.background_manager_loading = background_manager_loading
        self.user_name = user_name
        self.text_btn = text_btn
        self.multi_text_btn = multi_text_btn
        self.username_input_box = username_input_box
        self.username_ask_btn = username_ask_btn
        self.choice_btn_1 = choice_btn_1
        self.choice_btn_2 = choice_btn_2
        self.choice_btn_3 = choice_btn_3
        self.choice_btn_4 = choice_btn_4

    def handle_choice_button_game_states(self, game_state, event):
        """Handles game states with multiple choices"""
        choice_made = False
        if game_state in [GameStateName.BEDROOM_SCENE_3, GameStateName.BEDROOM_SCENE_5]:
            if self.choice_btn_1.is_clicked(event):
                game_state = GameStateName.BALCONY_SCENE_1
                self.text_btn.reset_animation()
                choice_made = True
            elif self.choice_btn_2.is_clicked(event):
                game_state = GameStateName.KITCHEN_SCENE_1
                self.text_btn.reset_animation()
                choice_made = True
            elif self.choice_btn_3.is_clicked(event):
                game_state = GameStateName.BATHROOM_SCENE_1
                self.text_btn.reset_animation()
                choice_made = True

        if game_state == GameStateName.BALCONY_SCENE_3:
            if self.choice_btn_1.is_clicked(event):
                game_state = GameStateName.BEDROOM_SCENE_4
                self.text_btn.reset_animation()
                choice_made = True
            elif self.choice_btn_2.is_clicked(event):
                game_state = GameStateName.BALCONY_SCENE_4
                self.text_btn.reset_animation()
                choice_made = True
            elif self.choice_btn_3.is_clicked(event):
                game_state = GameStateName.BALCONY_SCENE_5
                self.text_btn.reset_animation()
                choice_made = True

        if game_state == GameStateName.KITCHEN_SCENE_4:
            if self.choice_btn_1.is_clicked(event):
                game_state = GameStateName.KITCHEN_SCENE_5
                self.text_btn.reset_animation()
                choice_made = True
            elif self.choice_btn_2.is_clicked(event):
                game_state = GameStateName.KITCHEN_SCENE_7
                self.text_btn.reset_animation()
                choice_made = True
            elif self.choice_btn_3.is_clicked(event):
                game_state = GameStateName.LAIPTINE_SCENE_1
                self.text_btn.reset_animation()
                choice_made = True
            elif self.choice_btn_4.is_clicked(event):
                game_state = GameStateName.BEDROOM_SCENE_4
                self.text_btn.reset_animation()
                choice_made = True

        if game_state == GameStateName.NARVELIS_SCENE_7:
            if self.choice_btn_1.is_clicked(event):
                game_state = GameStateName.NARVELIS_SCENE_15
                self.text_btn.reset_animation()
                choice_made = True
            elif self.choice_btn_2.is_clicked(event):
                game_state = GameStateName.NARVELIS_SCENE_8
                self.text_btn.reset_animation()
                choice_made = True
            elif self.choice_btn_3.is_clicked(event):
                game_state = GameStateName.WORLD_MOVEMENT
                self.text_btn.reset_animation()
                choice_made = True

        if game_state == GameStateName.STORE_SCENE_20:
            if self.choice_btn_1.is_clicked(event):
                game_state = GameStateName.WORLD_MOVEMENT
                self.text_btn.reset_animation()
                choice_made = True
            elif self.choice_btn_2.is_clicked(event):
                game_state = GameStateName.STORE_SCENE_21
                self.text_btn.reset_animation()
                choice_made = True

        if game_state == GameStateName.BEDROOM_SCENE_11:
            if self.choice_btn_1.is_clicked(event):
                game_state = GameStateName.BALCONY_SCENE_7
                self.text_btn.reset_animation()
                choice_made = True
            elif self.choice_btn_2.is_clicked(event):
                game_state = GameStateName.KITCHEN_SCENE_9
                self.text_btn.reset_animation()
                choice_made = True
            elif self.choice_btn_3.is_clicked(event):
                game_state = GameStateName.BATHROOM_SCENE_3
                self.text_btn.reset_animation()
                choice_made = True
            elif self.choice_btn_4.is_clicked(event):
                game_state = GameStateName.SLEEP_SCENE_1
                self.text_btn.reset_animation()
                choice_made = True

        if game_state == GameStateName.KITCHEN_SCENE_10:
            if self.choice_btn_1.is_clicked(event):
                game_state = GameStateName.KITCHEN_SCENE_11
                self.text_btn.reset_animation()
                choice_made = True
            elif self.choice_btn_2.is_clicked(event):
                game_state = GameStateName.WORLD_MOVEMENT
                self.text_btn.reset_animation()
                choice_made = True
            elif self.choice_btn_3.is_clicked(event):
                game_state = GameStateName.BEDROOM_SCENE_11
                self.text_btn.reset_animation()
                choice_made = True
            elif self.choice_btn_4.is_clicked(event):
                game_state = GameStateName.KITCHEN_SCENE_12
                self.text_btn.reset_animation()
                choice_made = True

        if game_state == GameStateName.BATHROOM_SCENE_2:
            if self.choice_btn_1.is_clicked(event):
                game_state = GameStateName.BEDROOM_SCENE_4
                self.text_btn.reset_animation()
                choice_made = True

        if game_state == GameStateName.BATHROOM_SCENE_4:
            if self.choice_btn_1.is_clicked(event):
                game_state = GameStateName.BEDROOM_SCENE_11
                self.text_btn.reset_animation()
                choice_made = True

        return choice_made, game_state

    def handle_game_state(self, game_state,
                          random_number_generator):
        """Handles linear game states"""
        self.text_btn.reset_animation()
        game_state = game_state
        if game_state == GameStateName.LOADING_SCREEN:
            game_state = GameStateName.INTRO_INPUT
        elif game_state == GameStateName.INTRO_SCENE_1:
            game_state = GameStateName.INTRO_SCENE_2
        elif game_state == GameStateName.INTRO_SCENE_2:
            game_state = GameStateName.INTRO_SCENE_3
        elif game_state == GameStateName.INTRO_SCENE_3:
            game_state = GameStateName.INTRO_SCENE_4
        elif game_state == GameStateName.INTRO_SCENE_4:
            game_state = GameStateName.INTRO_SCENE_5
        elif game_state == GameStateName.INTRO_SCENE_5:
            game_state = GameStateName.BEDROOM_SCENE_1
        elif game_state == GameStateName.BEDROOM_SCENE_1:
            game_state = GameStateName.BEDROOM_SCENE_2
        elif game_state == GameStateName.BEDROOM_SCENE_2:
            game_state = GameStateName.BEDROOM_SCENE_3
        elif game_state == GameStateName.BEDROOM_SCENE_4:
            game_state = GameStateName.BEDROOM_SCENE_5
        elif game_state == GameStateName.BALCONY_SCENE_1:
            game_state = GameStateName.BALCONY_SCENE_2
        elif game_state == GameStateName.BALCONY_SCENE_2:
            game_state = GameStateName.BALCONY_SCENE_3
        elif game_state == GameStateName.BALCONY_SCENE_4:
            game_state = GameStateName.BALCONY_SCENE_2
        elif game_state == GameStateName.BALCONY_SCENE_5:
            game_state = GameStateName.GAME_OVER
        elif game_state == GameStateName.KITCHEN_SCENE_1:
            game_state = GameStateName.KITCHEN_SCENE_2
        elif game_state == GameStateName.KITCHEN_SCENE_2:
            game_state = GameStateName.KITCHEN_SCENE_3
        elif game_state == GameStateName.KITCHEN_SCENE_3:
            game_state = GameStateName.KITCHEN_SCENE_4
        elif game_state == GameStateName.KITCHEN_SCENE_5:
            game_state = GameStateName.KITCHEN_SCENE_6
        elif game_state == GameStateName.KITCHEN_SCENE_6:
            game_state = GameStateName.KITCHEN_SCENE_4
        elif game_state == GameStateName.KITCHEN_SCENE_7:
            game_state = GameStateName.KITCHEN_SCENE_8
        elif game_state == GameStateName.KITCHEN_SCENE_8:
            game_state = GameStateName.KITCHEN_SCENE_4
        elif game_state == GameStateName.LAIPTINE_SCENE_1:
            game_state = GameStateName.LAIPTINE_SCENE_2
        elif game_state == GameStateName.LAIPTINE_SCENE_2:
            if random_number_generator < 5:
                game_state = GameStateName.LAIPTINE_SCENE_3
            else:
                game_state = GameStateName.LAIPTINE_SCENE_4
        elif game_state == GameStateName.LAIPTINE_SCENE_3:
            game_state = GameStateName.NARVELIS_SCENE_1
        elif game_state == GameStateName.LAIPTINE_SCENE_4:
            game_state = GameStateName.LAIPTINE_SCENE_5
        elif game_state == GameStateName.LAIPTINE_SCENE_5:
            game_state = GameStateName.LAIPTINE_SCENE_6
        elif game_state == GameStateName.LAIPTINE_SCENE_6:
            game_state = GameStateName.NARVELIS_SCENE_1
        elif game_state == GameStateName.NARVELIS_SCENE_1:
            game_state = GameStateName.NARVELIS_SCENE_2
        elif game_state == GameStateName.NARVELIS_SCENE_1:
            game_state = GameStateName.NARVELIS_SCENE_2
        elif game_state == GameStateName.NARVELIS_SCENE_2:
            game_state = GameStateName.NARVELIS_SCENE_3
        elif game_state == GameStateName.NARVELIS_SCENE_3:
            game_state = GameStateName.NARVELIS_SCENE_4
        elif game_state == GameStateName.NARVELIS_SCENE_4:
            game_state = GameStateName.NARVELIS_SCENE_5
        elif game_state == GameStateName.NARVELIS_SCENE_5:
            game_state = GameStateName.NARVELIS_SCENE_6
        elif game_state == GameStateName.NARVELIS_SCENE_6:
            game_state = GameStateName.NARVELIS_SCENE_7
        elif game_state == GameStateName.NARVELIS_SCENE_8:
            game_state = GameStateName.NARVELIS_SCENE_9
        elif game_state == GameStateName.NARVELIS_SCENE_9:
            game_state = GameStateName.NARVELIS_SCENE_10
        elif game_state == GameStateName.NARVELIS_SCENE_10:
            game_state = GameStateName.NARVELIS_SCENE_7
        elif game_state == GameStateName.NARVELIS_SCENE_11:
            game_state = GameStateName.NARVELIS_SCENE_12
        elif game_state == GameStateName.NARVELIS_SCENE_13:
            game_state = GameStateName.NARVELIS_SCENE_14
        elif game_state == GameStateName.NARVELIS_SCENE_15:
            game_state = GameStateName.NARVELIS_SCENE_16
        elif game_state == GameStateName.NARVELIS_SCENE_16:
            game_state = GameStateName.NARVELIS_SCENE_17
        elif game_state == GameStateName.NARVELIS_SCENE_17:
            game_state = GameStateName.NARVELIS_SCENE_18
        elif game_state == GameStateName.NARVELIS_SCENE_18:
            game_state = GameStateName.NARVELIS_SCENE_19
        elif game_state == GameStateName.NARVELIS_SCENE_19:
            game_state = GameStateName.NARVELIS_SCENE_20
        elif game_state == GameStateName.NARVELIS_SCENE_20:
            game_state = GameStateName.NARVELIS_SCENE_21
        elif game_state == GameStateName.NARVELIS_SCENE_21:
            game_state = GameStateName.NARVELIS_SCENE_22
        elif game_state == GameStateName.NARVELIS_SCENE_22:
            game_state = GameStateName.NARVELIS_SCENE_7
        elif game_state == GameStateName.STORE_SCENE_1:
            game_state = GameStateName.STORE_SCENE_2
        elif game_state == GameStateName.STORE_SCENE_2:
            game_state = GameStateName.STORE_SCENE_3
        elif game_state == GameStateName.STORE_SCENE_3:
            game_state = GameStateName.STORE_SCENE_4
        elif game_state == GameStateName.STORE_SCENE_4:
            game_state = GameStateName.STORE_SCENE_5
        elif game_state == GameStateName.STORE_SCENE_5:
            game_state = GameStateName.STORE_SCENE_6
        elif game_state == GameStateName.STORE_SCENE_7:
            game_state = GameStateName.STORE_SCENE_8
        elif game_state == GameStateName.STORE_SCENE_8:
            game_state = GameStateName.STORE_SCENE_9
        elif game_state == GameStateName.STORE_SCENE_9:
            game_state = GameStateName.STORE_SCENE_10
        elif game_state == GameStateName.STORE_SCENE_10:
            game_state = GameStateName.STORE_SCENE_11
        elif game_state == GameStateName.STORE_SCENE_11:
            game_state = GameStateName.STORE_SCENE_12
        elif game_state == GameStateName.STORE_SCENE_13:
            game_state = GameStateName.STORE_SCENE_14
        elif game_state == GameStateName.STORE_SCENE_14:
            game_state = GameStateName.STORE_SCENE_15
        elif game_state == GameStateName.STORE_SCENE_15:
            game_state = GameStateName.STORE_SCENE_16
        elif game_state == GameStateName.STORE_SCENE_16:
            game_state = GameStateName.STORE_SCENE_17
        elif game_state == GameStateName.STORE_SCENE_17:
            game_state = GameStateName.STORE_SCENE_18
        elif game_state == GameStateName.STORE_SCENE_18:
            game_state = GameStateName.STORE_SCENE_19
        elif game_state == GameStateName.STORE_SCENE_19:
            game_state = GameStateName.STORE_SCENE_20
        elif game_state == GameStateName.STORE_SCENE_21:
            game_state = GameStateName.STORE_SCENE_22
        elif game_state == GameStateName.STORE_SCENE_22:
            game_state = GameStateName.STORE_SCENE_23
        elif game_state == GameStateName.STORE_SCENE_23:
            game_state = GameStateName.STORE_SCENE_24
        elif game_state == GameStateName.STORE_SCENE_24:
            game_state = GameStateName.STORE_SCENE_25
        elif game_state == GameStateName.STORE_SCENE_25:
            game_state = GameStateName.GAME_OVER
        elif game_state == GameStateName.STORE_SCENE_26:
            game_state = GameStateName.STORE_SCENE_27
        elif game_state == GameStateName.STORE_SCENE_27:
            game_state = GameStateName.STORE_SCENE_28
        elif game_state == GameStateName.STORE_SCENE_28:
            game_state = GameStateName.STORE_SCENE_29
        elif game_state == GameStateName.NARVELIS_SCENE_23:
            game_state = GameStateName.BEDROOM_SCENE_10
        elif game_state == GameStateName.BEDROOM_SCENE_10:
            game_state = GameStateName.BEDROOM_SCENE_11
        elif game_state == GameStateName.KITCHEN_SCENE_9:
            game_state = GameStateName.KITCHEN_SCENE_10
        elif game_state == GameStateName.KITCHEN_SCENE_11:
            game_state = GameStateName.KITCHEN_SCENE_10
        elif game_state == GameStateName.KITCHEN_SCENE_12:
            game_state = GameStateName.KITCHEN_SCENE_10
        elif game_state == GameStateName.BALCONY_SCENE_7:
            game_state = GameStateName.BALCONY_SCENE_8
        elif game_state == GameStateName.BALCONY_SCENE_9:
            game_state = GameStateName.BALCONY_SCENE_8
        elif game_state == GameStateName.BALCONY_SCENE_10:
            game_state = GameStateName.BALCONY_SCENE_11
        elif game_state == GameStateName.BALCONY_SCENE_12:
            game_state = GameStateName.BALCONY_SCENE_13
        elif game_state == GameStateName.BALCONY_SCENE_13:
            game_state = GameStateName.BALCONY_SCENE_14
        elif game_state == GameStateName.BALCONY_SCENE_14:
            game_state = GameStateName.BALCONY_SCENE_15
        elif game_state == GameStateName.BALCONY_SCENE_15:
            game_state = GameStateName.GAME_COMPLETED
        elif game_state == GameStateName.BATHROOM_SCENE_1:
            game_state = GameStateName.BATHROOM_SCENE_2
        elif game_state == GameStateName.BATHROOM_SCENE_3:
            game_state = GameStateName.BATHROOM_SCENE_4
        elif game_state == GameStateName.SLEEP_SCENE_1:
            game_state = GameStateName.SLEEP_SCENE_2
        elif game_state == GameStateName.SLEEP_SCENE_2:
            game_state = GameStateName.NIGHTMARE_WORLD_MOVEMENT

        return game_state

    def handle_game_state_drawing(self, game_state):
        """Draws all objects associated with a specific game_state"""
        if game_state == GameStateName.INTRO_INPUT:
            self.screen.fill((200, 200, 200))
            self.username_ask_btn.text_box_appear(self.screen)
            self.username_input_box.update()
            self.username_input_box.draw(self.screen)
        elif game_state == GameStateName.LOADING_SCREEN:
            self.background_manager_loading.update_screen_size(self.settings.current_resolution,
                                                               LOADING_IMAGE_PATH_LIST)
            self.background_manager_loading.update_background_slideshow()
            self.background_manager_loading.draw_background(self.screen)
        elif game_state == GameStateName.MENU:
            self.background_manager.update_image_path('resources/main_map/night.jpg')
            self.background_manager.draw_background(self.screen)
        elif game_state == GameStateName.INTRO_SCENE_1:
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text(f'Nice to meet you, {self.user_name}')
        elif game_state == GameStateName.INTRO_SCENE_2:
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text('Enjoy! :)')
        elif game_state == GameStateName.INTRO_SCENE_3:
            self.screen.fill((0, 0, 0))  # Clear the screen with black before drawing
            self.background_manager.update_image_path('resources/main_map/night.jpg')
            self.background_manager.draw_background(self.screen)
        elif game_state == GameStateName.INTRO_SCENE_4:
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text('')
            self.multi_text_btn.render_multiline_text('You can control your character with the arrow keys.\n'
                                                      'Hold "L_Shift" to sprint!', self.screen, color=(255, 40, 40))
        elif game_state == GameStateName.INTRO_SCENE_5:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/main_map/day.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text('Somewhere in a fictional town, fictional country.')
        elif game_state == GameStateName.BEDROOM_SCENE_1:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/bedroom.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text(story_text.get('HomeRoom').get('story')[0])
        elif game_state == GameStateName.BEDROOM_SCENE_2:
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text('')
            self.multi_text_btn.render_multiline_text(story_text.get('HomeRoom').get('story')[1], self.screen)
        elif game_state == GameStateName.BEDROOM_SCENE_3:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/bedroom.jpg')
            self.background_manager.draw_background(self.screen)
            self.choice_btn_1.update_text(story_text.get('HomeRoom').get('selection')[0])
            self.choice_btn_2.update_text(story_text.get('HomeRoom').get('selection')[1])
            self.choice_btn_3.update_text(story_text.get('HomeRoom').get('selection')[2])
            self.choice_btn_1.draw(self.screen)
            self.choice_btn_1.check_hover(self.screen)
            self.choice_btn_2.draw(self.screen)
            self.choice_btn_2.check_hover(self.screen)
            self.choice_btn_3.draw(self.screen)
            self.choice_btn_3.check_hover(self.screen)
        elif game_state == GameStateName.BEDROOM_SCENE_4:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/bedroom.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text(story_text.get('HomeRoom').get('story')[2])
        elif game_state == GameStateName.BEDROOM_SCENE_5:
            self.screen.fill((0, 0, 0))
            self.background_manager.draw_background(self.screen)
            self.choice_btn_1.update_text(story_text.get('HomeRoom').get('selection')[0])
            self.choice_btn_2.update_text(story_text.get('HomeRoom').get('selection')[1])
            self.choice_btn_3.update_text(story_text.get('HomeRoom').get('selection')[2])
            self.choice_btn_1.draw(self.screen)
            self.choice_btn_1.check_hover(self.screen)
            self.choice_btn_2.draw(self.screen)
            self.choice_btn_2.check_hover(self.screen)
            self.choice_btn_3.draw(self.screen)
            self.choice_btn_3.check_hover(self.screen)
        elif game_state == GameStateName.BALCONY_SCENE_1:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/balcony.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text(story_text.get('HomeBalcony').get('story')[0])
        elif game_state == GameStateName.BALCONY_SCENE_2:
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text('')
            self.multi_text_btn.render_multiline_text(story_text.get('HomeBalcony').get('story')[1], self.screen)
        elif game_state == GameStateName.BALCONY_SCENE_3:
            self.screen.fill((0, 0, 0))
            self.background_manager.draw_background(self.screen)
            self.choice_btn_1.update_text(story_text.get('HomeBalcony').get('selection')[0])
            self.choice_btn_2.update_text(story_text.get('HomeBalcony').get('selection')[1])
            self.choice_btn_3.update_text(story_text.get('HomeBalcony').get('selection')[2])
            self.choice_btn_1.draw(self.screen)
            self.choice_btn_1.check_hover(self.screen)
            self.choice_btn_2.draw(self.screen)
            self.choice_btn_2.check_hover(self.screen)
            self.choice_btn_3.draw(self.screen)
            self.choice_btn_3.check_hover(self.screen)
        elif game_state == GameStateName.BALCONY_SCENE_4:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/balcony.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text(story_text.get('HomeBalcony').get('story')[2])
        elif game_state == GameStateName.BALCONY_SCENE_5:
            self.screen.fill((0, 0, 0))
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text('')
            self.multi_text_btn.render_multiline_text(story_text.get('HomeBalcony').get('story')[3], self.screen)
        elif game_state == GameStateName.GAME_OVER:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/game_over.jpg')
            self.background_manager.draw_background(self.screen)
        elif game_state == GameStateName.KITCHEN_SCENE_1:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/kitchen.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/mom3.png')
            self.background_manager.draw_background(self.screen)
        elif game_state == GameStateName.KITCHEN_SCENE_2:
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text('')
            self.multi_text_btn.render_multiline_text(story_text.get('HomeKitchen').get('story')[0], self.screen)
        elif game_state == GameStateName.KITCHEN_SCENE_3:
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text('')
            self.multi_text_btn.render_multiline_text(story_text.get('HomeKitchen').get('story')[1], self.screen)
        elif game_state == GameStateName.KITCHEN_SCENE_4:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/kitchen.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/mom2.png')
            self.background_manager.draw_background(self.screen)
            self.choice_btn_1.update_text(story_text.get('HomeKitchen').get('selection')[0])
            self.choice_btn_2.update_text(story_text.get('HomeKitchen').get('selection')[1])
            self.choice_btn_3.update_text(story_text.get('HomeKitchen').get('selection')[2])
            self.choice_btn_4.update_text(story_text.get('HomeKitchen').get('selection')[3])
            self.choice_btn_1.draw(self.screen)
            self.choice_btn_1.check_hover(self.screen)
            self.choice_btn_2.draw(self.screen)
            self.choice_btn_2.check_hover(self.screen)
            self.choice_btn_3.draw(self.screen)
            self.choice_btn_3.check_hover(self.screen)
            self.choice_btn_4.draw(self.screen)
            self.choice_btn_4.check_hover(self.screen)
        elif game_state == GameStateName.KITCHEN_SCENE_5:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/kitchen.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/mom3.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text(f"{self.user_name}: " + story_text.get('HomeKitchen').get('player')[0])
        elif game_state == GameStateName.KITCHEN_SCENE_6:
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("Mom: " + story_text.get('HomeKitchen').get('mom')[0])
        elif game_state == GameStateName.KITCHEN_SCENE_7:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/fridge.jpg')
            self.background_manager.draw_background(self.screen)
        elif game_state == GameStateName.KITCHEN_SCENE_8:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/fridge.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeKitchen').get('story')[2], self.screen)
        elif game_state == GameStateName.LAIPTINE_SCENE_1:
            self.screen.fill((0, 0, 0))
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeLaiptine').get('story')[0], self.screen)
        elif game_state == GameStateName.LAIPTINE_SCENE_2:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kaimynas.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeLaiptine').get('story')[1], self.screen)
        elif game_state == GameStateName.LAIPTINE_SCENE_3:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kaimynas2.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeLaiptine').get('story')[2], self.screen)
        elif game_state == GameStateName.LAIPTINE_SCENE_4:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kaimynas2.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeLaiptine').get('story')[3], self.screen)
        elif game_state == GameStateName.LAIPTINE_SCENE_5:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kaimynas2.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text(f"{self.user_name}: " + story_text.get('HomeLaiptine').get('player')[0])
        elif game_state == GameStateName.LAIPTINE_SCENE_6:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kaimynas.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text(f"Kaimynas: " + story_text.get('HomeLaiptine').get('kaimynas')[0])
        elif game_state == GameStateName.NARVELIS_SCENE_1:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text(story_text.get('HomeNarvelis').get('story')[0])
        elif game_state == GameStateName.NARVELIS_SCENE_2:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text(story_text.get('HomeNarvelis').get('story')[1])
        elif game_state == GameStateName.NARVELIS_SCENE_3:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas2.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text(" ")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[2], self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_4:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text(" ")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[3], self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_5:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text(story_text.get('HomeNarvelis').get('story')[4])
        elif game_state == GameStateName.NARVELIS_SCENE_6:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas2.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text(story_text.get('HomeNarvelis').get('story')[5])
        elif game_state == GameStateName.NARVELIS_SCENE_7:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            self.background_manager.draw_background(self.screen)
            self.choice_btn_1.update_text(story_text.get('HomeNarvelis').get('selection')[0])
            self.choice_btn_2.update_text(story_text.get('HomeNarvelis').get('selection')[1])
            self.choice_btn_3.update_text(story_text.get('HomeNarvelis').get('selection')[2])
            self.choice_btn_1.draw(self.screen)
            self.choice_btn_1.check_hover(self.screen)
            self.choice_btn_2.draw(self.screen)
            self.choice_btn_2.check_hover(self.screen)
            self.choice_btn_3.draw(self.screen)
            self.choice_btn_3.check_hover(self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_8:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas2.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[6], self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_9:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[7], self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_10:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[8], self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_11:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[9], self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_12:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[10], self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_13:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[11], self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_14:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas2.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[12], self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_15:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[13], self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_16:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas2.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[14], self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_17:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/playground.jpg')
            self.background_manager.draw_background(self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_18:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/playground.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[15], self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_19:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/playground.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[16], self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_20:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/playground.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[17], self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_21:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[18], self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_22:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/tupikas2.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('HomeNarvelis').get('story')[19], self.screen)
        elif game_state == GameStateName.STORE_SCENE_1:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.update_text("")
            self.text_btn.text_box_appear(self.screen)
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[0], self.screen)
        elif game_state == GameStateName.STORE_SCENE_2:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[1], self.screen)
        elif game_state == GameStateName.STORE_SCENE_3:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[2], self.screen)
        elif game_state == GameStateName.STORE_SCENE_4:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[3], self.screen)
        elif game_state == GameStateName.STORE_SCENE_5:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[4], self.screen)
        elif game_state == GameStateName.STORE_SCENE_6:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            self.background_manager.draw_background(self.screen)
            self.choice_btn_1.update_text(story_text.get('Store').get('selection')[0])
            self.choice_btn_2.update_text(story_text.get('Store').get('selection')[1])
            self.choice_btn_1.draw(self.screen)
            self.choice_btn_1.check_hover(self.screen)
            self.choice_btn_2.draw(self.screen)
            self.choice_btn_2.check_hover(self.screen)
        elif game_state == GameStateName.STORE_SCENE_7:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(f"{self.user_name}: " + story_text.get('Store').get('player')[0],
                                                      self.screen)
        elif game_state == GameStateName.STORE_SCENE_8:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[5], self.screen)
        elif game_state == GameStateName.STORE_SCENE_9:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke2.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text("Cashier: " + story_text.get('Store').get('kasininke')[0],
                                                      self.screen)
        elif game_state == GameStateName.STORE_SCENE_10:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[6], self.screen)
        elif game_state == GameStateName.STORE_SCENE_11:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke2.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[7], self.screen)
        elif game_state == GameStateName.STORE_SCENE_12:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke2.png')
            self.background_manager.draw_background(self.screen)
            self.choice_btn_1.update_text(story_text.get('Store').get('selection')[1])
            self.choice_btn_2.update_text(story_text.get('Store').get('selection')[2])
            self.choice_btn_1.draw(self.screen)
            self.choice_btn_1.check_hover(self.screen)
            self.choice_btn_2.draw(self.screen)
            self.choice_btn_2.check_hover(self.screen)
        elif game_state == GameStateName.STORE_SCENE_13:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(f"{self.user_name}: " + story_text.get('Store').get('player')[1],
                                                      self.screen)
        elif game_state == GameStateName.STORE_SCENE_14:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[8], self.screen)
        elif game_state == GameStateName.STORE_SCENE_15:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text("Cashier: " + story_text.get('Store').get('kasininke')[1],
                                                      self.screen)
        elif game_state == GameStateName.STORE_SCENE_16:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[9], self.screen)
        elif game_state == GameStateName.STORE_SCENE_17:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(f"{self.user_name}: " + story_text.get('Store').get('player')[2],
                                                      self.screen)
        elif game_state == GameStateName.STORE_SCENE_18:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke2.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[10], self.screen)
        elif game_state == GameStateName.STORE_SCENE_19:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text("Cashier: " + story_text.get('Store').get('kasininke')[2],
                                                      self.screen)
        elif game_state == GameStateName.STORE_SCENE_20:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke2.png')
            self.background_manager.draw_background(self.screen)
            self.choice_btn_1.update_text(story_text.get('Store').get('selection')[1])
            self.choice_btn_2.update_text(story_text.get('Store').get('selection')[3])
            self.choice_btn_1.draw(self.screen)
            self.choice_btn_1.check_hover(self.screen)
            self.choice_btn_2.draw(self.screen)
            self.choice_btn_2.check_hover(self.screen)
        elif game_state == GameStateName.STORE_SCENE_21:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke2.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[11], self.screen)
        elif game_state == GameStateName.STORE_SCENE_22:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[12], self.screen)
        elif game_state == GameStateName.STORE_SCENE_23:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[13], self.screen)
        elif game_state == GameStateName.STORE_SCENE_24:
            self.screen.fill((0, 0, 0))
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[14], self.screen)
        elif game_state == GameStateName.STORE_SCENE_25:
            self.screen.fill((0, 0, 0))
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[15], self.screen)
        elif game_state == GameStateName.NARVELIS_SCENE_23:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/stairwell_entrance.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("Looks like the neighbour is gone.")
        elif game_state == GameStateName.BEDROOM_SCENE_10:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/bedroom.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("You're home, what do you do now?")
        elif game_state == GameStateName.BEDROOM_SCENE_11:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/bedroom.jpg')
            self.background_manager.draw_background(self.screen)
            self.choice_btn_1.update_text(story_text.get('HomeRoom').get('selection')[0])
            self.choice_btn_2.update_text(story_text.get('HomeRoom').get('selection')[1])
            self.choice_btn_3.update_text(story_text.get('HomeRoom').get('selection')[2])
            self.choice_btn_4.update_text(story_text.get('HomeRoom').get('selection')[3])
            self.choice_btn_1.draw(self.screen)
            self.choice_btn_1.check_hover(self.screen)
            self.choice_btn_2.draw(self.screen)
            self.choice_btn_2.check_hover(self.screen)
            self.choice_btn_3.draw(self.screen)
            self.choice_btn_3.check_hover(self.screen)
            self.choice_btn_4.draw(self.screen)
            self.choice_btn_4.check_hover(self.screen)
        elif game_state == GameStateName.KITCHEN_SCENE_9:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/kitchen.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/mom.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("You enter the Kitchen")
        elif game_state == GameStateName.KITCHEN_SCENE_10:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/kitchen.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/mom.png')
            self.background_manager.draw_background(self.screen)
            self.choice_btn_1.update_text(story_text.get('HomeKitchen').get('selection')[1])
            self.choice_btn_2.update_text(story_text.get('HomeKitchen').get('selection')[2])
            self.choice_btn_3.update_text(story_text.get('HomeKitchen').get('selection')[3])
            self.choice_btn_4.update_text(story_text.get('HomeKitchen').get('selection')[4])
            self.choice_btn_1.draw(self.screen)
            self.choice_btn_1.check_hover(self.screen)
            self.choice_btn_2.draw(self.screen)
            self.choice_btn_2.check_hover(self.screen)
            self.choice_btn_3.draw(self.screen)
            self.choice_btn_3.check_hover(self.screen)
            self.choice_btn_4.draw(self.screen)
            self.choice_btn_4.check_hover(self.screen)
        elif game_state == GameStateName.KITCHEN_SCENE_11:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/fridge.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(
                'Despite how many times you look at it,\nthere\'s still nothing edible inside..', self.screen)
        elif game_state == GameStateName.KITCHEN_SCENE_12:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/kitchen.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/mom2.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(
                'You\'re not desperate enough.', self.screen)
        elif game_state == GameStateName.BALCONY_SCENE_7:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/balcony.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(
                'You\'re here again..', self.screen)
        elif game_state == GameStateName.BALCONY_SCENE_8:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/balcony.jpg')
            self.background_manager.draw_background(self.screen)
            self.choice_btn_1.update_text(story_text.get('HomeBalcony').get('selection')[0])
            self.choice_btn_2.update_text(story_text.get('HomeBalcony').get('selection')[1])
            self.choice_btn_3.update_text(story_text.get('HomeBalcony').get('selection')[2])
            self.choice_btn_4.update_text(story_text.get('HomeBalcony').get('selection')[3])
            self.choice_btn_1.draw(self.screen)
            self.choice_btn_1.check_hover(self.screen)
            self.choice_btn_2.draw(self.screen)
            self.choice_btn_2.check_hover(self.screen)
            self.choice_btn_3.draw(self.screen)
            self.choice_btn_3.check_hover(self.screen)
        elif game_state == GameStateName.BALCONY_SCENE_9:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/balcony.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(
                'You have no smokes!', self.screen)
        elif game_state == GameStateName.BALCONY_SCENE_10:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/nest.jpg')
            self.background_manager.draw_background(self.screen)
        elif game_state == GameStateName.BALCONY_SCENE_11:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/nest.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(
                'You have found some currency! You take it from the nest.', self.screen)
        elif game_state == GameStateName.BALCONY_SCENE_12:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/balcony.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(
                'Ahh. Finally, your first smoke of the day.', self.screen)
        elif game_state == GameStateName.BALCONY_SCENE_13:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/balcony.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(
                'And it\'s yours to enjoy.', self.screen)
        elif game_state == GameStateName.BALCONY_SCENE_14:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/smoking.jpg')
            self.background_manager.draw_background(self.screen)
        elif game_state == GameStateName.BALCONY_SCENE_15:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/smoking2.jpg')
            self.background_manager.draw_background(self.screen)
        elif game_state == GameStateName.STORE_SCENE_26:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(f"{self.user_name}: " + story_text.get('Store').get('player')[0],
                                                      self.screen)
        elif game_state == GameStateName.STORE_SCENE_27:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke2.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text("Cashier: " + story_text.get('Store').get('kasininke')[0],
                                                      self.screen)
        elif game_state == GameStateName.STORE_SCENE_28:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text(story_text.get('Store').get('story')[16], self.screen)
        elif game_state == GameStateName.STORE_SCENE_29:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/store_kasa.jpg')
            self.background_manager.draw_background(self.screen)
            self.background_manager.update_image_path('resources/scene_backgrounds/kasininke.png')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text("")
            self.multi_text_btn.render_multiline_text('You have received a pack of cigarettes!', self.screen)
        elif game_state == GameStateName.GAME_COMPLETED:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/thanks_for_playing.jpg')
            self.background_manager.draw_background(self.screen)
        elif game_state == GameStateName.BATHROOM_SCENE_1:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/bathroom.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text('')
            self.multi_text_btn.render_multiline_text(story_text.get('HomeBathroom').get('story')[0], self.screen)
        elif game_state == GameStateName.BATHROOM_SCENE_2:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/bathroom.jpg')
            self.background_manager.draw_background(self.screen)
            self.choice_btn_1.update_text(story_text.get('HomeBathroom').get('selection')[0])
            self.choice_btn_1.draw(self.screen)
            self.choice_btn_1.check_hover(self.screen)
        elif game_state == GameStateName.BATHROOM_SCENE_3:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/bathroom.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text('')
            self.multi_text_btn.render_multiline_text(story_text.get('HomeBathroom').get('story')[2], self.screen)
        elif game_state == GameStateName.BATHROOM_SCENE_4:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/bathroom.jpg')
            self.background_manager.draw_background(self.screen)
            self.choice_btn_1.update_text(story_text.get('HomeBathroom').get('selection')[0])
            self.choice_btn_1.draw(self.screen)
            self.choice_btn_1.check_hover(self.screen)
        elif game_state == GameStateName.SLEEP_SCENE_1:
            self.screen.fill((0, 0, 0))
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text('You faceplant your head on the pillow.')
        elif game_state == GameStateName.SLEEP_SCENE_2:
            self.screen.fill((0, 0, 0))
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text('Before long you\'re taking a sound afternoon nap.')
        elif game_state == GameStateName.BEDROOM_SCENE_12:
            self.screen.fill((0, 0, 0))
            self.background_manager.update_image_path('resources/scene_backgrounds/bedroom.jpg')
            self.background_manager.draw_background(self.screen)
            self.text_btn.text_box_appear(self.screen)
            self.text_btn.update_text('What the hell was that?')

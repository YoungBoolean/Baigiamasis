"""
start_game.py

This module initializes the Pygame environment and sets up the main game window. It also creates
instances of the BackgroundManager and GameMenu classes to manage the background and game menu respectively.
"""

import pygame
import os

from ui.background_manager import BackgroundManager
from ui.constants import GAME_VERSION, GAME_NAME
from ui.game_menu import GameMenu
from settings import Settings
from ui.utilities import preload_button_image_transparent, preload_button_image_solid, preload_button_image_hover

# Initialize pygame
pygame.init()

# Screen setup
os.environ['SDL_VIDEO_CENTERED'] = '1'  # Center the game window on the screen
screen = pygame.display.set_mode((800, 600))  # Set the screen resolution to 800x600
pygame.display.set_caption(f"{GAME_NAME} {GAME_VERSION}")  # Set the window caption to include the game name and version
clock = pygame.time.Clock()  # Create a clock object to manage the frame rate

# Initialize background managers
background_manager = BackgroundManager(screen.get_size(), slideshow=False)  # Background manager for the main game
background_manager_loading = BackgroundManager(screen.get_size())  # Background manager for the loading screen

button_image = preload_button_image_transparent()
button_image_solid = preload_button_image_solid()
loaded_hover_image_list = preload_button_image_hover()

if __name__ == '__main__':
    GameMenu(screen, clock, Settings(),
             background_manager, background_manager_loading,
             button_image, button_image_solid, loaded_hover_image_list)

import pygame
import os

from ui.background_manager import BackgroundManager, LOADING_IMAGE_PATH_LIST
from ui.constants import GAME_VERSION, GAME_NAME
from ui.game_menu import game_menu
from settings import Settings

# Initialize pygame
pygame.init()

# Screen setup
os.environ['SDL_VIDEO_CENTERED'] = '1'  # Window centravimas
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(f"{GAME_NAME} {GAME_VERSION}")
clock = pygame.time.Clock()

background_manager = BackgroundManager(screen.get_size())
background_manager_loading = BackgroundManager(screen.get_size(),image_path_list=LOADING_IMAGE_PATH_LIST)

if __name__ == '__main__':
    game_menu(screen, clock, Settings(), background_manager, background_manager_loading)
import pygame
import os

from ui.background_manager import BackgroundManager
from ui.constants import GAME_VERSION, GAME_NAME
from ui.game_menu import GameMenu
from settings import Settings

# Initialize pygame
pygame.init()

# Screen setup
os.environ['SDL_VIDEO_CENTERED'] = '1'  # Window centravimas
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(f"{GAME_NAME} {GAME_VERSION}")
clock = pygame.time.Clock()

background_manager = BackgroundManager(screen.get_size(), slideshow=False)
background_manager_loading = BackgroundManager(screen.get_size())

if __name__ == '__main__':
    GameMenu(screen, clock, Settings(), background_manager, background_manager_loading)

import pygame

# Constants
RESOLUTIONS = [(800, 600), (1024, 768), (1280, 720), (1600, 900), (1920, 1080)]
FPS = 60

USER_NAME = 'Player'

# Game meta
GAME_VERSION = '0.0.1'
GAME_NAME = 'Sludge Faktorius'

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
GRAY = (200, 200, 200)

# Image paths
BACKGROUND_IMAGE_PATH = 'resources/background/'
first_list = [BACKGROUND_IMAGE_PATH + str(img) + '.jpg' for img in range(1, 42)]
second_list = [BACKGROUND_IMAGE_PATH + str(img) + '.jpg' for img in range(40, 1, -1)]
BACKGROUND_IMAGE_PATH_LIST = first_list + second_list
MAP_IMAGE_PATH = 'path/to/your/map_image.jpg'
BUTTON_FILE_PATH = 'resources/button_hover/'
LOADING_IMAGE_PATH_LIST = ['resources/loading_screens/' + str(img) + '.png' for img in range(1, 3 + 1)]

# Fonts
FONT_PATH = 'resources/pixel-azure-bonds.ttf'
TEXT_FONT_PATH = 'resources/arial.ttf'

# Character
CHARACTER_SPEED = 5
CHARACTER_WIDTH = 50
CHARACTER_HEIGHT = 50

# Map
NON_WALKABLE_AREAS = [
    pygame.Rect(100, 100, 200, 100),  # Example building 1
    pygame.Rect(400, 200, 200, 100),  # Example building 2
]


# Game states
class GameState:
    INPUT = 'INPUT'
    MENU = 'MENU'
    LOADING_SCREEN_1 = 'LOADING_SCREEN'
    SCENE_1 = 'SCENE 1'
    SCENE_2 = 'SCENE 2'
    SCENE_3 = 'SCENE 3'
    SCENE_4 = 'SCENE 4'
    SCENE_5 = 'SCENE 5'
    SCENE_6 = 'SCENE 6'
    SCENE_7 = 'SCENE 7'

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
BACKGROUND_PLACEHOLDER_IMAGE_PATH = 'resources/background/placeholder.jpg'
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
CHARACTER_WIDTH = 25
CHARACTER_HEIGHT = 50

# Character sprite
sprite_path = 'resources/character_assets/char_template'
SPRITE_PATH_LIST = [sprite_path + str(img) + '.png' for img in range(1, 4)]

# Map
NON_WALKABLE_AREAS = [
    pygame.Rect(56, 295, 68, 600),  # building 1
    pygame.Rect(292, 274, 80, 600),  # building 2
    pygame.Rect(529, 263, 75, 600),  # building 3
    pygame.Rect(691, 145, 28, 100),  # building 4
    pygame.Rect(677, 2, 120, 63),  # building 5
    pygame.Rect(735, 299, 65, 88),  # building 6
    pygame.Rect(624, 80, 30, 70),  # building 7
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
    WORLD_MOVEMENT = 'WORLD_MOVEMENT'

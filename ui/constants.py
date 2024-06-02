import pygame

# Constants
RESOLUTIONS = [(800, 600), (1024, 768), (1280, 720), (1600, 900), (1920, 1080)]
FPS = 60

# Player name
USER_NAME = 'Player'

# Game meta
GAME_VERSION = '0.0.1'
GAME_NAME = 'Koshmaras'

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
BUTTON_FILE_PATH = 'resources/button/'
LOADING_IMAGE_PATH_LIST = ['resources/loading_screens/' + str(img) + '.png' for img in range(1, 3 + 1)]

# Fonts
FONT_PATH = 'resources/fonts/pixel-azure-bonds.ttf'
TEXT_FONT_PATH = 'resources/fonts/arial.ttf'

# Character variables
CHARACTER_SPEED = 5
CHARACTER_WIDTH = 25
CHARACTER_HEIGHT = 50

# Character sprites
sprite_path = 'resources/character_assets/char_template'
SPRITE_PATH_LIST = [sprite_path + str(img) + '.png' for img in range(1, 4)]

# Main map
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
    INTRO_INPUT = 'INPUT'
    MENU = 'MENU'
    LOADING_SCREEN = 'LOADING_SCREEN'
    INTRO_SCENE_1 = 'INTRO_SCENE 1'
    INTRO_SCENE_2 = 'INTRO_SCENE 2'
    INTRO_SCENE_3 = 'INTRO_SCENE 3'
    INTRO_SCENE_4 = 'INTRO_SCENE 4'
    INTRO_SCENE_5 = 'INTRO_SCENE 5'
    INTRO_SCENE_6 = 'INTRO_SCENE 6'
    INTRO_SCENE_7 = 'INTRO_SCENE 7'
    BEDROOM_SCENE_1 = 'BEDROOM_SCENE 1'
    BEDROOM_SCENE_2 = 'BEDROOM_SCENE 2'
    BEDROOM_SCENE_3 = 'BEDROOM_SCENE 3'
    BEDROOM_SCENE_4 = 'BEDROOM_SCENE 4'
    BEDROOM_SCENE_5 = 'BEDROOM_SCENE 5'
    BEDROOM_SCENE_6 = 'BEDROOM_SCENE 6'
    BEDROOM_SCENE_7 = 'BEDROOM_SCENE 7'
    BEDROOM_SCENE_8 = 'BEDROOM_SCENE 8'
    BEDROOM_SCENE_9 = 'BEDROOM_SCENE 9'
    BALCONY_SCENE_1 = 'BALCONY_SCENE 1'
    BALCONY_SCENE_2 = 'BALCONY_SCENE 2'
    BALCONY_SCENE_3 = 'BALCONY_SCENE 3'
    BALCONY_SCENE_4 = 'BALCONY_SCENE 4'
    BALCONY_SCENE_5 = 'BALCONY_SCENE 5'
    BALCONY_SCENE_6 = 'BALCONY_SCENE 6'
    KITCHEN_SCENE_1 = 'KITCHEN_SCENE 1'
    KITCHEN_SCENE_2 = 'KITCHEN_SCENE 2'
    KITCHEN_SCENE_3 = 'KITCHEN_SCENE 3'
    KITCHEN_SCENE_4 = 'KITCHEN_SCENE 4'
    BATHROOM_SCENE_1 = 'BATHROOM_SCENE 1'
    BATHROOM_SCENE_2 = 'BATHROOM_SCENE 2'
    BATHROOM_SCENE_3 = 'BATHROOM_SCENE 3'
    BATHROOM_SCENE_4 = 'BATHROOM_SCENE 4'
    GAME_OVER = 'GAME_OVER'
    WORLD_MOVEMENT = 'WORLD_MOVEMENT'


CHOICED_GAME_STATE_LIST = [GameState.BALCONY_SCENE_1, GameState.BEDROOM_SCENE_3, GameState.BEDROOM_SCENE_5]

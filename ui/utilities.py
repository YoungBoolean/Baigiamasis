"""
utilities.py

This module contains the function when_character_in_specific_coords, it is responsbile for returning True if character
coordinates are the same as the specified ones.
"""
from .constants import BUTTON_FILE_PATH
import pygame


def when_character_in_specific_coords(width_scale, height_scale, character,
                                      coordinates_x: tuple, coordinates_y: tuple):
    """if character moves to a specific coordinate, return True"""
    if (coordinates_x[0] * width_scale < character.return_position()[0] <
            coordinates_x[1] * width_scale and
            coordinates_y[0] * height_scale < character.return_position()[1] <
            coordinates_y[1] * height_scale):
        return True
    else:
        return False


def preload_button_image_transparent():
    button_image = pygame.image.load(BUTTON_FILE_PATH + 'menu_button.png').convert_alpha()
    return button_image


def preload_button_image_solid():
    button_image = pygame.image.load(BUTTON_FILE_PATH + 'menu_button_solid.png').convert_alpha()
    return button_image


def preload_button_image_hover(image_count=18, file_path='resources/button/button_hover_animation/'):
    loaded_image_list = []
    for file_index in range(1, image_count+1):
        filename = f"{file_index}.png"
        image_load = pygame.image.load(file_path + filename).convert_alpha()
        loaded_image_list.append(image_load)
    return loaded_image_list

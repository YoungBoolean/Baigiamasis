"""
utilities.py

This module contains the function when_character_in_specific_coords, it is responsbile for returning True if character
coordinates are the same as the specified ones.
"""


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

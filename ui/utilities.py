def calculate_position(screen_width, screen_height, rel_x, rel_y):
    x = screen_width * rel_x
    y = screen_height * rel_y
    return x, y


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

def calculate_position(screen_width, screen_height, rel_x, rel_y):
    x = screen_width * rel_x
    y = screen_height * rel_y
    return x, y
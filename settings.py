from ui.constants import RESOLUTIONS


class Settings:

    def __init__(self):
        self.current_resolution_index = 0
        self.fullscreen = False

    @property
    def current_resolution(self):
        return RESOLUTIONS[self.current_resolution_index]

    def increase_resolution(self):
        self.current_resolution_index = (self.current_resolution_index + 1) % len(RESOLUTIONS)
        return self.current_resolution_index

    def decrease_resolution(self):
        self.current_resolution_index = (self.current_resolution_index - 1) % len(RESOLUTIONS)
        return self.current_resolution_index

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
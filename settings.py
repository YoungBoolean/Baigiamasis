"""
settings.py

This module contains the Settings class, which is responsible for managing game settings such as
resolution and fullscreen mode. It allows for increasing or decreasing the resolution and toggling
the fullscreen mode.
"""

from ui.constants import RESOLUTIONS


class Settings:
    """Settings class, responsible for managing game settings such as resolution and fullscreen mode."""
    def __init__(self):
        self.current_resolution_index = 0
        self.fullscreen = False
        self.language = 'Lietuvių'

    @property
    def current_resolution(self) -> tuple:
        """Get the current resolution based on current resolution index."""

        return RESOLUTIONS[self.current_resolution_index]

    def increase_resolution(self) -> int:
        """
        Increments the current_resolution_index to point to the next resolution in the RESOLUTIONS list.
        If the end of the list is reached, it wraps around to the start.
        """
        self.current_resolution_index = (self.current_resolution_index + 1) % len(RESOLUTIONS)
        return self.current_resolution_index

    def decrease_resolution(self) -> int:
        """
        Decrements the current_resolution_index to point to the previous resolution in the RESOLUTIONS list.
        If the start of the list is reached, it wraps around to the end.
        """
        self.current_resolution_index = (self.current_resolution_index - 1) % len(RESOLUTIONS)
        return self.current_resolution_index

    def toggle_fullscreen(self) -> None:
        """Toggles the fullscreen attribute between True and False."""
        self.fullscreen = not self.fullscreen

    def change_language(self) -> None:
        """Changes language"""
        self.language = 'English' if self.language == 'Lietuvių' else 'Lietuvių'

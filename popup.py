import ctypes
import pygame

class PopUp():
    def __init__(self):
        self.screen = pygame.display.get_surface()

    def PopUp(self, content: str, title: str, popUpStyle: int):
        return ctypes.windll.user32.MessageBoxW(0, content, title, popUpStyle)
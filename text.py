import pygame
import screen

class Text():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def writeTextOnScreen(self, text: str, color: int, font: str, fontSize: int, antialias: bool, posX: int, posY: int, italic: bool):
        text = pygame.font.SysFont(font, fontSize, italic=italic).render(text, antialias, color)
        textRect = text.get_rect(center=(posX, posY))
        return text, textRect

    def clientInput(self, text: str, color: int, fontSize: int, posX: int, posY: int):
        display = self.screen
        mediumFont = pygame.font.Font(None, fontSize)
        screen.Screen().setElementsOnScreen()
        textSurface = mediumFont.render(text, True, color)
        display.blit(textSurface, (posX,posY))
        pygame.display.flip()
        self.clock.tick()
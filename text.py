import pygame
import screen

class Text:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def writeTextOnScreen(self, text: str, color: int, font: str, fontSize: int, antialias: bool, posX: int, posY: int, italic: bool):
        display = self.screen
        text = pygame.font.SysFont(font, fontSize, italic=italic).render(text, antialias, color)
        textRect = text.get_rect(center=(posX, posY))
        display.blit(text, textRect)
        pygame.display.update()

    def clientInput(self, text: str, color: int, fontSize: int, posX: int, posY: int):
        display = self.screen
        mediumFont = pygame.font.Font(None, fontSize)
        screen.Screen().setBasicElementsOnScreen()
        textSurface = mediumFont.render(text, True, color)
        display.blit(textSurface, (posX,posY))
        pygame.display.flip()
        self.clock.tick()

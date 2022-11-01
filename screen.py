#import pygame
import object
import text
import pygame

class Screen():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.WIDTH = 700
        self.HEIGHT = 500
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GRAY = (77, 77, 77)
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.mouse = pygame.mouse.get_pos()
        self.bigFont = 42
        self.mediumFont = 32

    def setElementsOnScreen(self):
        screen = self.screen
        sendButtonImage = pygame.image.load("Assets/send_button.png").convert_alpha()
        inputBackgroundImage = pygame.image.load("Assets/input_background.png").convert_alpha()

        screen.fill((150,150,150))
        pygame.display.set_caption("Find The Number!")
        title = text.Text().writeTextOnScreen("Find the Number!", self.GRAY, None, self.bigFont, True, self.WIDTH/2, self.HEIGHT/4, False)
        explication = text.Text().writeTextOnScreen("A number has been randomly generated, and you need to find it. GL", self.GRAY, None, 30, True, self.WIDTH/2, self.HEIGHT/3, True)
        sendButton = object.Object().createObject(sendButtonImage, 525, self.HEIGHT/2, 0.3)
        inputBackground = object.Object().createObject(inputBackgroundImage, 175, self.HEIGHT/2, 0.3)

        screen.blit(sendButton[0], sendButton[1])
        screen.blit(inputBackground[0], inputBackground[1])
        screen.blit(title[0], title[1])
        screen.blit(explication[0], explication[1])

        pygame.display.update()
        
        return sendButton[1]

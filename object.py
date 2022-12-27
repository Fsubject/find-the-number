import pygame

class Object:
    def __init__(self):
        self.screen = pygame.display.get_surface()

    def createObject(self, objectImage, posX: int, posY: int, scale: float):
        display = self.screen
        width = objectImage.get_width()
        height = objectImage.get_height()
        objectImage = pygame.transform.scale(objectImage, (int(width * scale), int(height * scale)))
        objectRect = objectImage.get_rect(center=(posX, posY))
        display.blit(objectImage, objectRect)
        pygame.display.update()
        return objectRect
    
    def checkObjectCollision(self, objectName):
        mouse = pygame.mouse.get_pos()
        return True if objectName.collidepoint(mouse[0], mouse[1]) else False
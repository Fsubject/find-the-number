import pygame

class Object():
    def __init__(self):
        self.screen = pygame.display.get_surface()

    def createObject(self, objectImage: str, posX: int, posY: int, scale: float):
        width = objectImage.get_width()
        height = objectImage.get_height()
        objectImage = pygame.transform.scale(objectImage, (int(width * scale), int(height * scale)))
        objectRect = objectImage.get_rect(center=(posX, posY))
        return objectImage, objectRect
    
    def checkObjectCollision(self, objectName: str):
        mouse = pygame.mouse.get_pos()
        return True if objectName.collidepoint(mouse[0], mouse[1]) else False
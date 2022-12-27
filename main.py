# Imports
import random
from screen import Screen
import object
import text
import pygame


# Main function
def main():
    global rdmNumber
    rdmNumber = generateRandomNumber(100)
    game()

# Game function
def game():
    screen = Screen()
    sendButton = screen.setBasicElementsOnScreen()
    userInput = ""

    isRunning = True
    while isRunning is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    userInput = userInput[:-1]
                    text.Text().clientInput(userInput, (255,255,255), 52, 100, 238)
                else:
                    if len(userInput) >= 7:
                        pass
                    else:
                        userInput += event.unicode
                        text.Text().clientInput(userInput, (255,255,255), 52, 100, 238)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if object.Object().checkObjectCollision(sendButton):
                    if userInput == rdmNumber:
                        text.Text().writeTextOnScreen("You found the number! GG", screen.GREEN, None, screen.bigFont, True, screen.WIDTH/2, (screen.HEIGHT/3)*2, False)
                    elif userInput > rdmNumber:
                        text.Text().writeTextOnScreen("Your number is too high! Retry...", screen.RED, None, screen.bigFont, True, screen.WIDTH/2, (screen.HEIGHT/3)*2, False)
                    elif userInput < rdmNumber:
                        text.Text().writeTextOnScreen("Your number is too lower! Retry...", screen.RED, None, screen.bigFont, True, screen.WIDTH/2, (screen.HEIGHT/3)*2, False)
                    else:
                        text.Text().writeTextOnScreen("Something is wrong with your number...", screen.RED, None, screen.bigFont, True, screen.WIDTH/2, (screen.HEIGHT/3)*2, False)


# Generate random number function
def generateRandomNumber(number: int):
    n = number
    return str(random.randint(1, n))
    
if __name__ == "__main__":
    main()

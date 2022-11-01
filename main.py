# Imports
import random
from screen import Screen
import object
import text
import popup
import pygame

# Main function
def main():
    global rdmNumber
    rdmNumber = generateNumber(100)
    print(rdmNumber)
    game()

def game():
    screen = Screen()
    sendButton = screen.setElementsOnScreen()
    userInput = ""

    isRunning = True
    while isRunning == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if object.Object().checkObjectCollision(sendButton):
                    if userInput == rdmNumber:
                        popup.PopUp().PopUp("Right answer! GG", "Answer Pop-Up", 0)
                    elif userInput > rdmNumber:
                        popup.PopUp().PopUp("Your number is a little bit too high!", "Answer Pop-Up", 0)
                    elif userInput < rdmNumber:
                        popup.PopUp().PopUp("Your number is too lower!", "Answer Pop-Up", 0)
                    else:
                        popup.PopUp().PopUp("Ooh, wrong answer... The next try will be the good one!", "Answer Pop-Up", 0)
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

# Generate random number function
def generateNumber(number: int):
    n1 = 1
    n2 = number
    return str(random.randint(n1, n2))
    
if __name__ == "__main__":
    main()

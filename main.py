# Imports
import os
import time
import random

# Main function
def main():
    clear()

    print("Welcome, in this game you'll try to find a number who'll be generate by our program.\nBut first, you need to choose the limit of the number who'll be generated.")
    #wait(5)

    isChoosing = True
    while isChoosing == True:
        number = input("\nEnter the limit of the number who'll be generated (type: help, if you don't understand) -> ")

        if number == "help":
            print("\nType a number higher than 1, and this number will be the limit of the generated number, exemple:\n   If you type '50', the number will be generated between 1 and 50.")
        elif number <= str(1):
            print("\nPlease type a number higher than 1.")
        elif number > str(1):
            isChoosing = False
            generateNumber(int(number))
        else:
            print("\nPlease type a number.")
    
    game()

# Game function
def game():
    clear()
    print(rdmNumber)

    isPlaying = True
    while isPlaying == True:
        playerAnswer = int(input(f"Try to find the random number! (tips: the number has been generated between {n1} and {n2}) -> "))

        if playerAnswer == rdmNumber:
            clear()
            isPlaying = False
            print("GG, you win!")
            wait(3)
        elif playerAnswer > rdmNumber:
            print("Lower!\n")
        elif playerAnswer < rdmNumber:
            print("Higher!\n")

# Generate random number function
def generateNumber(number: int):
    global n1, n2, rdmNumber

    n1 = 1
    n2 = number
    rdmNumber = random.randint(n1, n2)

# Wait function
def wait(timer: float):
    time.sleep(timer)

# Clear terminal function
def clear():
    os.system("cls || clear")

def passL():
    print("\n")

if __name__ == "__main__":
    main()

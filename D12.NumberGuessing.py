import random
import os

def clear():
    """Clears the screen"""
    os.system('cls')

rndnum = random.randint(1, 100)
easy = 10
hard = 5
guess = 0

def GuessingGame():
    
    print("Welcome to number guessing game! \nI'm thinking of a number between 1 and 100")
    # print(f"<<Testing! it's {rndnum}>>")
    if input("Choose a difficulty: Type 'easy' or 'hard'\n") == "easy":
        attempts = easy
    else:
        attempts = hard
    print(f"You have {attempts} attempts remaining")

    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess > rndnum:
            print("Nah too high")
            attempts -= 1
            print(f"You have {attempts} attempts remaining")
        elif guess < rndnum:
            print("Nah too low")
            attempts -= 1
            print(f"You have {attempts} attempts remaining")
        else:
            print(f"You got this! the answer is {rndnum}")
            attempts = 0

while input("Hey Playa wanna play? Type 'yes' or 'no': ") == 'yes':
    clear()
    GuessingGame()
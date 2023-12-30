import os
import random
from D14Art import logo, versus
from D14GameData import GAME_DATA 

first_choice = random.choice(GAME_DATA)
second_choice = random.choice(GAME_DATA)


def clear():
    """Clears the screen"""
    os.system('cls')

def display_variants():
    print(f"{first_choice["celebrity"]}: {first_choice["description"]}")
    print(versus)
    print(f"{second_choice["celebrity"]}: {second_choice["description"]}")

def playerschoice():
    if input("Who has bigger following? Type 'a' or 'b' ") == 'a':
        return first_choice
    else:
        return second_choice

def compare():
     if first_choice["followers"] > second_choice["followers"]:
         return first_choice
     else:
         return second_choice
     

def game():
    score = 0
    gaming = True
    print(logo)
    while gaming == True:
        global first_choice
        global second_choice
        display_variants()
        players_choice = playerschoice()
        answer = compare()

        if answer == players_choice:
            score +=1
            print(f"You're right, score: {score}")
            first_choice = players_choice
            second_choice = random.choice(GAME_DATA)
        else:
            print(f"You lose with score: {score}")
            gaming = False
    


while input("Do you want to play? Type 'y' to play, or 'n' to exit. ") == 'y':
    game()
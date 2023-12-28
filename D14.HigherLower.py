import os
import random
from D14Art import logo, versus
from D14GameData import GAME_DATA 

bucket = []
first_choise = random.choice(GAME_DATA)
second_choise = random.choice(GAME_DATA)
players_choice = 0
score = 0


def clear():
    """Clears the screen"""
    os.system('cls')

def print_variants():
    print(first_choise["celebrity"],  "it's:",first_choise["description"])
    print(versus)
    print(second_choise["celebrity"],  "it's:",second_choise["description"])

def evaluate(first_choise, second_choise):
    input("Type in '1' for a first and '2' for second variant:\n")
    

def game():

    print(logo)
    print_variants()
# evaluate(first_choise, second_choise)
# 1.Logo
# 2.First CHoice, adding points. 
# 3.Save choice and never present it again

# print(versus)
# print(GAME_DATA[0]["searches"])

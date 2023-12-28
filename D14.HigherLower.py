import os
import random
from D14Art import logo, versus
from D14GameData import GAME_DATA 

bucket = []
first_choise = random.choice(GAME_DATA)
second_choise = random.choice(GAME_DATA)
score = 0


def clear():
    """Clears the screen"""
    os.system('cls')

def evaluate(first_choise, second_choise):
    input("Type in '1' for a first and '2' for second variant:\n")
    
    if first_choise["searches"] > second_choise["searches"]:
        print(first_choise["word"], "Wins! with ", first_choise["searches"])
    else:
        print(second_choise["word"], "Wins! with ", second_choise["searches"])

print(logo)
print(first_choise["word"],  "it's:",first_choise["description"])
print(versus)
print(second_choise["word"],  "it's:",second_choise["description"])

# 1.Logo
# 2.First CHoice, adding points. 
# 3.Save choice and never present it again

# print(versus)
# print(GAME_DATA[0]["searches"])

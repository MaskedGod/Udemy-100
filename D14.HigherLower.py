import os
import random
from D14Art import logo, versus
from D14GameData import GAME_DATA 

bucket = []
first_choice = random.choice(GAME_DATA)
second_choice = random.choice(GAME_DATA)
players_choice = 0
gaming = True

def clear():
    """Clears the screen"""
    os.system('cls')





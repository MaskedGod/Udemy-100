import random
import os


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playerhand =  []
comphand = []


def first_draw():
    dealer(playerhand)
    dealer(playerhand)
    dealer(comphand)
    dealer(comphand)

def dealer(list):
    rndcard = random.choice(cards)
    if sum(list) >= 20 and rndcard == 11:
        list.append(1)
    else:
        list.append(rndcard)

def winner():
    playersum = sum(playerhand)
    compsum = sum(comphand)
    if playersum > 21 or compsum > playersum:
        print("Computer wins!")
        game = False    
    elif compsum > 21 or playersum > compsum:
        print("You win!")
        game = False
    elif compsum + playersum > 42:
        print("It's a Draw!")
        game = False
    
        

def Blackjack():
    game = True
    first_draw()
    print(f"Your cards: {playerhand}")
    winner()
    while game == True:
        if input("Draw next card: 'yes' or 'no' ") == "no":
            game = False
        dealer(playerhand)
        dealer(comphand)
        winner()
    



Blackjack()
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
import os


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playerhand =  []
comphand = []
playersum = sum(playerhand)
compsum = sum(comphand)

def score():
    playersum = sum(playerhand)
    compsum = sum(comphand)

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
    score()
    if playersum == compsum and playersum + compsum == 42:
        print("Draw!")
        
    elif playersum > 21 and compsum > 21:
        print("Draw! you both over limit")
        
    elif playersum == 21 or compsum > 21:
        print("You won", playersum)
     
    elif compsum == 21 or playersum > 21:
        print("You lose! it's computers victory:", compsum)
        
        

    
    
    
       

def Blackjack():
    game = 0
    first_draw()
    print(f"Your cards: {playerhand}")
    playersum = sum(playerhand)
    compsum = sum(comphand)
    if playersum == 21:
        print("BlackJack!! You won", playersum)
        return
    elif compsum == 21:
        print("BlackJack! but not for you! it's computers victory:", compsum)
        return
    print(f"Your score is: {playersum}")
    print(f"test compscore {compsum}")
    while game < 1:
        playersum = sum(playerhand)
        compsum = sum(comphand)
        if compsum < 17:
            dealer(comphand)
        if input("Draw another card? 'yes' or  'no' \n") == "yes":
            dealer(playerhand)
            score
            print(playerhand, playersum)
            winner()

        else:
            winner()
            game = 1
    
    print(f"Aftermath hand:{playerhand}, score:{playersum}\nhand:{comphand}, score:{compsum}")
           
    
        



Blackjack()
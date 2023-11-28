import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer = random.choice([rock, paper, scissors])
player = int(input("Choose rock, paper or scissors, type 1, 2 or 3\n"))
if player == 1:
    player = rock
elif player == 2:
    player = paper
else:
    player = scissors 
print("Your choise: \n", player)
print("Computer's choise: \n", computer)
if player == computer:
    print("It's a draw!")
elif player == rock and computer == scissors:
    print("You Win!")
elif player == paper and computer == rock:
    print("You Win!")
elif player == scissors and computer == paper:
    print("You Win!")
else:
    print("Computer WIN!!!")
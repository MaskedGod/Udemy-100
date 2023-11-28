print("Welcome to Treasure Island. \nYour Misiion is to find the  \n    TREASURE!!!")

choice1 = input('Your are at crossroad. Where do you want to go? Type "left" or "right" ').lower()

if choice1 == "left":
  #Game Continue
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for boat. Type "swim" to swim across ').lower()
  if choice2 == "wait":
    #Game is continue
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")
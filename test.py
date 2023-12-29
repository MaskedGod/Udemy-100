def print_variants():

    print(f"{first_choice["celebrity"]}: {first_choice["description"]}")
    print(versus)
    print(f"{second_choice["celebrity"]}: {second_choice["description"]}")

def compare():
     if first_choice["followers"] > second_choice["followers"]:
         return first_choice
     else:
         return second_choice

def playerschoice():
    if input("Who has bigger following? Type 'a' or 'b' ") == 'a':
        return first_choice
    else:
        return second_choice

def evaluate(compared, players_choice, score):
    if compared == players_choice:
        print("Yeah")
        score += 1
    else:
        print("Dead")
    return score
def game():
    players_choice = ""
    compared = ""
    score = 0
    print(logo)
    
    # while gaming == True:
    print_variants()
    compared = compare()
    print(compared)
    players_choice = playerschoice()
    print(players_choice)
    updated_score = evaluate(compared, players_choice, score)
    


game()   
# while input("Do you want to play? Type 'y' to play, or 'n' to exit. ") == 'y':
#     game()
# while input("Do you want to play? Type 'y' to play, or 'n' to exit. ") == 'y':
#     game()
#1.Initialization:

# Initialize a score variable to keep track of the player's points.
# Show a welcome message and rules to the player.
#2. Game Setup:

# Generate a starting number or randomly select a card from a deck.
# Show the player the initial number or card.
#3. Game Rounds:

# Ask the player to predict if the next number/card will be higher or lower.
# Accept the player's input (higher/lower).
# Generate the next number/card.
# Compare the generated number/card with the previous one.
# If the player's prediction matches the comparison:
# Increment the score.
# Show a message indicating a correct prediction.
# If the player's prediction doesn’t match the comparison:
# End the game.
# Display the final score.
# Ask the player if they want to play again.
#4. Repeat or End:

# If the player wants to play again, start a new game from step 2.
# If the player doesn't want to continue, show a goodbye message and end the game.
# Optional Enhancements:

# Implement difficulty levels (e.g., changing the range of numbers or using different decks for cards).
# Incorporate a leaderboard to track high scores.
# Add lifelines or hints for the player.
# Game Loop:

# Continuously loop through steps 2-4 until the player decides to stop playing.
# The game essentially involves predicting whether the next number or card will be higher or lower than the current one. 
# The player's score increases with each correct prediction until they decide to stop or make an incorrect guess.
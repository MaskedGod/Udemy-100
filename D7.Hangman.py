import random as rnd
from D7HangmanMisc import art, guessing_word

end_of_game = False
word = rnd.choice(guessing_word).lower()
display = ["_" for i in range(len(word))]
lifes = 5
print(display)


while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #stop that madness 
    if guess == "stop":
        end_of_game = True
    #Check guessed letter
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            display[position] = letter
    # If you guessed wrong it's one life gone
    if guess not in word:
        print(f'{guess} not in word')
        lifes -= 1 
        print(art[lifes])

    print(display)

    # R ya winning son?
    if "_" not in display:
        end_of_game = True
        print("You win.")
    # Guess not(
    elif lifes == 0:
        end_of_game = True
        print("Ya hanged:(")
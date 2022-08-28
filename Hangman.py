from list_word import *
import random

five_or_less = list(filter(lambda x: len(x) <= 5, word))
six_to_nine = list(filter(lambda x: len(x) >= 6 and len(x) < 9, word))
nine_or_more = list(filter(lambda x: len(x) >= 9, word))

lives = 0
game_word = []

level = int(input("What level you want to play? (1 = easy ; 2 = medium ; 3= hard): "))

if level == 1:
    game_word = random.choice(five_or_less)
    lives = 10
elif level == 2:
    game_word = random.choice(six_to_nine)
    lives = 8
elif level == 3:
    game_word = random.choice(nine_or_more)
    lives = 6

wrong_guess = []
right_guess = []

#n_try = input("How many lives you want to have: )
word_size = int(len(game_word))

blank = ["_"] * word_size
print("_" * word_size)
print("\n Number of lives= ", lives)

def indices(game_word, guess):
    return [i for i, x in enumerate(game_word) if x == guess]

while True:
    guess = input("Guess a letter: ")
    if guess not in wrong_guess:
        if guess not in right_guess:
            if guess in game_word:
                if game_word.count(guess) > 1:
                    position = (indices(game_word, guess))
                    for i in range (game_word.count(guess)):
                        blank[position[i]] = guess
                        right_guess.append(guess)
                    print(''.join(blank).upper())
                else:
                    position = (indices(game_word, guess))
                    blank[position[0]] = guess
                    right_guess.append(guess)
                    print(''.join(blank).upper())
            else:
                print("\n *OH, WRONG LETTER*")
                lives = lives - 1
                print("\n Lives: ", lives)
                print(''.join(blank).upper())
                wrong_guess.append(guess)
                print("\n Wrong guesses: " , wrong_guess, "\n")


            if lives == 0:
                print("\n **I'M SORRY YOU LOST** \n")
                print("The right word was: " , game_word)
                break
            if "_" not in blank:
               print("\n **CONGRATULATIONS! YOU WON!**")
               break
        else:
            print("\nYou already tried this letter \n")
    else:
        print("\nYou already tried this letter \n")















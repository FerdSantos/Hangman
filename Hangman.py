from list_word import *
import random

five_or_less = list(filter(lambda x: len(x) <= 5, word))
six_to_nine = list(filter(lambda x: len(x) >= 6 and len(x) < 9, word))
nine_or_more = list(filter(lambda x: len(x) >= 9, word))

level = ()
lifes = 0
game_word = []

while True:
    level = input("What level you want to play? (1 = easy ; 2 = medium ; 3= hard): ")
    if level == "1" or level == "2" or level == "3":
        level = int(level)
        break
    else:
        print("\n**Please answer with either 1, 2 or 3**\n")


if level == 1:
    game_word = random.choice(five_or_less)
    lifes = 10
elif level == 2:
    game_word = random.choice(six_to_nine)
    lifes = 8
elif level == 3:
    game_word = random.choice(nine_or_more)
    lifes = 6

wrong_guess = []
right_guess = []

#n_try = input("How many lifes you want to have: )
word_size = int(len(game_word))

blank = ["_"] * word_size
print("_" * word_size)
print("\n Number of lifes= ", lifes)

def indices(game_word, guess):
    return [i for i, x in enumerate(game_word) if x == guess]

while True:
    guess = input("Guess a letter: ")
    if guess in letter:
        if guess not in wrong_guess:
            if guess not in right_guess:
                if guess in game_word:
                    if game_word.count(guess) > 1:
                        position = (indices(game_word, guess))
                        for i in range (game_word.count(guess)):
                            blank[position[i]] = guess
                            right_guess.append(guess)
                        print("\n",''.join(blank).upper(), "\n")
                    else:
                        position = (indices(game_word, guess))
                        blank[position[0]] = guess
                        right_guess.append(guess)
                        print("\n",''.join(blank).upper(), "\n")
                else:
                    print("\n *OH, WRONG LETTER*")
                    lifes = lifes - 1
                    print("\n Lifes: ", lifes, "\n")
                    print(''.join(blank).upper())
                    wrong_guess.append(guess)
                    print("\n Wrong guesses: " , wrong_guess, "\n")


                if lifes == 0:
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
    else:
        print("\n **Please, type letters in lower case or '-'** ")

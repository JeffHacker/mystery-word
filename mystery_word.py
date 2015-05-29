# You can figure this out.

# file input and random word

import random

# file input and random word

with open('/usr/share/dict/words', ) as temp_file:
    text_to_analyze = temp_file.read()
    text_to_analyze = text_to_analyze.lower().split()
    word = random.choice(text_to_analyze)
print(word)

#start the game
print("Would you like to play a game? \n")
print("Guess the word by selecting one letter at a time. \n")
print("Think carefully.  You only get 8 guesses \n")
print("The mystery word contains {} letters.".format(len(word)))


# input and check
def letter_input(letter):
    if len(letter) > 1:
        guessed_letter = input("Please guess only one letter...")
        return

letter_input(letter = input("Guess a letter...")) # letter







# display

game_word = len(word) * "-"
# print(word)
display = list(game_word)
display[0] = "c"
display[2] = "t"
print(' '.join(display)) # from Soren on the .join for nicer looking display

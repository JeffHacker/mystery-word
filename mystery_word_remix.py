# file input and random word
import random
with open('/usr/share/dict/words', ) as temp_file:
    text_to_analyze = temp_file.read()
    text_to_analyze = text_to_analyze.lower().split()
    word = random.choice(text_to_analyze)
print(word)
game_word = len(word) * "-"
word_list = game_word.split()

# start the game
print("Would you like to play a game? \n")
print("Guess the word by selecting one letter at a time. \n")
print("Think carefully.  You only get 8 guesses \n")
print("The mystery word contains {} letters.".format(len(word)))


# input and check for single entry
def letter_input(letter):
    if len(letter) > 1:
        letter = input("Please guess only one letter...")
        return letter
    return letter  # PJ helped me walk through this function while I solved

input_letter = list(letter_input(letter=input("Guess a letter...")))
print(input_letter)

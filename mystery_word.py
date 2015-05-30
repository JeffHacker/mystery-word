# file input and random word

import random

# file input and random word

with open('/usr/share/dict/words', ) as temp_file:
    text_to_analyze = temp_file.read()
    text_to_analyze = text_to_analyze.lower().split()
    word = random.choice(text_to_analyze)
print(word)
game_word = len(word) * "-"
word_list = game_word.split()
wrong_count = 0

#start the game
print("Would you like to play a game? \n")
print("Guess the word by selecting one letter at a time. \n")
print("Think carefully.  You only get 8 guesses \n")
print("The mystery word contains {} letters.".format(len(word)))


# input and check
def letter_input(letter):
    if len(letter) > 1:
        letter = input("Please guess only one letter...")
        return letter
    return letter # PJ helped me walk through this function while I solved

input_letter = list(letter_input(letter = input("Guess a letter...")))
print(input_letter)

# check letter against secret word
def check_letter(input_letter, word, word_list):

    if input_letter in word:
        for letter in word:
            counter = 0
            if input_letter == word_list[counter]:
                word_list[counter] = input_letter
                counter += 1
    wrong_count +=1

word_list = check_letter(input_letter, word_list, word)
print(word_list)



# print(word)

print(' '.join(word_list)) # from Soren on the .join for nicer looking display

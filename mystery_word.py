# file input and random word
import random
with open('/usr/share/dict/words', ) as temp_file:
    text_to_analyze = temp_file.read()
    text_to_analyze = text_to_analyze.lower().split()
    word = random.choice(text_to_analyze)
print(word)
game_word = len(word) * "-"
word_list = list(game_word)
print("word list {}".format(word_list))
wrong_list = []

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


# check letter against secret word
def check_letter(input_letter, word, word_list):
    if input_letter in word:
        counter = 0
        for letter in word:
            if input_letter == letter:  # Bekk
                word_list[counter] = input_letter
            counter += 1
        return word_list


input_letter = (letter_input(letter=input("Guess a letter...")))
print(input_letter)

# call function to populate the word_list for display
word_list = check_letter(input_letter, word, word_list)
print("word_list {}".format(word_list))


# print(word)
# print(' '.join(word_list))  # from Soren on the .join for nicer looking display

# You can figure this out.

# file input and random word

import random

with open('/usr/share/dict/words', ) as temp_file:
    text_to_analyze = temp_file.read()
    text_to_analyze = text_to_analyze.lower()
#    list_to_analyze = text_to_analyze.split()
print(text_to_analyze)










# display: working through it
word = ('cat')
game_word = len(word) * "-"
# print(word)
display = list(game_word)
display[0] = "c"
display[2] = "t"
print(' '.join(display)) # from Soren on the .join for nicer looking display

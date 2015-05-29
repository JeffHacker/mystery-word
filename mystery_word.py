# You can figure this out.

# file input and random word

import random

# file input and random word

with open('/usr/share/dict/words', ) as temp_file:
    text_to_analyze = temp_file.read()
    text_to_analyze = text_to_analyze.lower().split()
    word = random.choice(text_to_analyze)
print(word)
# print(text_to_analyze)









# display: working through it
# word = ('cat')  #this no longer needed due to file input logic
game_word = len(word) * "-"
# print(word)
display = list(game_word)
display[0] = "c"
display[2] = "t"
print(' '.join(display)) # from Soren on the .join for nicer looking display

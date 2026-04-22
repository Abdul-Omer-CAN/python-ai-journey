## Chooses heads or tails using 'random'##

# import random

# coin = random.choice(["heads", "tails"])
# print(coin)


## OR ##

# from random import choice

# coin = choice(["heads", "tails"])
# print(coin)

## using '.shuffle' ##

# import random

# cards = ["jack", "queen", "king"]
# random.shuffle(cards)
# for card in cards:
#     print(card)


## Import sys ##

# import sys
# try:
#     print("hello, my name is", sys.argv[1])
# except:
#     print("Too few arguments")

## Looping w/ len() & 'for in' ##

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for name in sys.argv[1:-1]:                 # over here '1:' slices the first part of the user input and give us the rest
    print("hello, my name is", name)      # if name is put in "" e.g "Abdulrehman Omer" then output will give us one line answer

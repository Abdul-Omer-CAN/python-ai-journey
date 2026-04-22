import sys

from CS50P5sayings import hello

if len(sys.argv) == 2:  # sys.arg is the list of everything you type in the terminal. your name is index 1 in the terminal hence
    hello(sys.argv[1])  # it prints your name when types after python CS50Psay.py
# also ==2 check that there are exactly 2 words in the terminal e.g 'cs50say.py' is word 1 and 'Abdul' is word 2

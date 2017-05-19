import random
'''
    This file is meant to test knowledge of string manipulation and lists
    
'''

WORDLIST_FILENAME = 'falloutdict.txt'


def get_words():
    """
    Reads all hacking words to a list, then shuffles it
    :returns a list words, containing all fallout hacking words (shuffled): 
    """

    with open(WORDLIST_FILENAME, 'r') as file:
        print('Loading words from', WORDLIST_FILENAME)
        words = file.readlines()
        print('Words loaded.')
        words = words[0].split(' ')
        random.shuffle(words)

    return words

def pick_secret_word():
    """
    Given that the function "get_words()" will return a list of shuffled words, pick_secret_word() gets a random
    selection from said list, to be the secret_word
    :returns secret_word: a randomly selected word  
    """
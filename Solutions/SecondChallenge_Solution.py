import random
'''
    ToDO: Add to me
    
'''

WORDLIST_FILENAME = 'falloutdict.txt'
ADDITIONAL_WORDS_NUM = 8


def get_words():
    """
    Reads all hacking words to a list, then shuffles it
    :returns a list words, containing all fallout hacking words (shuffled): 
    """
    with open(WORDLIST_FILENAME, 'r') as file:
        print('-------------------')
        print('Loading words from', WORDLIST_FILENAME)
        words = file.readlines()
        print('Words loaded.')
        print('-------------------\n')
        words = words[0].split(' ')
        random.shuffle(words)

    return words

WORDS = get_words()  # The shuffled list of words from falloutdict.txt


def pick_secret_word():
    """
    Given that the function "get_words()" will return a list of shuffled words; pick_secret_word() should get a random
    selection from said list to be the secret_word
    
    :returns secret_word: a randomly selected word from the WORDS word list
    """
    # Solution
    secret_word = random.choice(WORDS)
    return secret_word


def get_additional_words(secret_word):
    """
    Notice that at the top of this file is written some constants in all caps. One of these constants is
    ADDITIONAL_WORDS_NUM. This is the amount of words to be printed along with the secret_word.
    
    :returns additional_words: A list of ADDITIONAL_WORDS_NUM randomly selected words from the
    falloutdict.txt word list. This list DOES NOT include the secret_word.
    
    Remember that all of the randomly selected words are stored in WORDS
    """
    # Solution
    additional_words = []
    for word in range(ADDITIONAL_WORDS_NUM):
        additional_words.append(random.choice(WORDS))

        if additional_words[word] == secret_word:
            while additional_words[word] == secret_word:
                additional_words[word] = random.choice(WORDS)

    return additional_words




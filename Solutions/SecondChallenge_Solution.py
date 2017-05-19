import random
'''
    ToDO: Add to me, finish assembly, all words should have the same length as secret_word (function: get_additional_words)
'''

WORDLIST_FILENAME = 'falloutdict.txt'
ADDITIONAL_WORDS_NUM = 8
NUM_OF_GUESSES = 5


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
        print('-------------------')
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


def word_display(secret_word, additional_words):
    """
    Prints out the words returned by the get_additional_words() function, along with the secret_word, in a random order.
    There is no test in the test file for this function.
    """
    # Solution
    all_words = additional_words
    all_words.append(secret_word)
    random.shuffle(all_words)
    print("Words: ")
    for word in all_words:
        print("\t" + word)
    print('-------------------')


def is_valid_guess(user_entry, secret_word, additional_words):
    """
    Verifies that the user entered in a valid guess entry. A valid guess entry is one that matches with at least one
    value in the additional_words list or secret_word. The user's guess is stored in user_entry.
    
    :returns True: if the guess is valid
    :returns False: if the guess is invalid
    """
    user_entry = user_entry.strip().upper()
    all_words = additional_words.copy()
    all_words.append(secret_word)
    return True if user_entry in all_words else False


def compare_user_entry(user_entry, secret_word):
    """
    Now the game logic needs to be handled. First consider what has happened so far up to this point:
        1. The word list has been shuffled
        2. A secret word and some additional words have been chosen from this word list
        3. The secret word and additional words have been displayed to the user
        4. The user has entered in his guess as to what the secret word might be.
    The user's guess from the words shown to him is stored in user_entry.
    
    Now we need to compare user_entry with the secret_word, to let the user know how much of his guess is correct.
    
    :returns num_correct: The number of letters in user_entry that match with secret_word. A letter in user_entry
    'matches' if the same letter occurs in the same position in secret_word.
    """
    # Solution
    num_correct = 0

    for letterA, letterB in user_entry, secret_word:
        if letterA == letterB:
            num_correct += 1
    return num_correct


# ------------------------------------------- Assembly -------------------------------------------
if __name__ == '__main__':
    secret_w = pick_secret_word()
    additional_w = get_additional_words(secret_w)
    word_display(secret_w, additional_w)
    print("Guess? ")
    for g in NUM_OF_GUESSES:
        guess = input()
        if is_valid_guess(guess, secret_w, additional_w):
            pass  # Come back to me!
        else:
            while not is_valid_guess(guess, secret_w, additional_w):
                print("Your guess is invalid!")
                print("Try again: ")
                guess = input()



# ----------------------------------------- End of Assembly --------------------------------------

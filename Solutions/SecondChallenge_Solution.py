import random, sys
'''
    I think you'll really enjoy this one!
    Basically I want you to recreate the hacking game that you play in the Fallout games!
    If you aren't sure what that is, or what to do, check out the docx / pdf file that came along with this file,
    there's a lot of information I hope you'll find helpful in there...
    And remember I'm only a message a way! (seriously, message me for like anything)
'''

WORDLIST_FILENAME = 'falloutdict.txt'
ADDITIONAL_WORDS_NUM = 8
NUM_OF_GUESSES = 5

#  ------ Helper function! You can skip this code... ------
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
# --------- End of Helper function ---------

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
    falloutdict.txt word list. Each word should have the same amount of letters as the secret_word.
    This list DOES NOT include the secret_word.
    
    Remember that the list of all words in the dictionary is stored in WORDS.
    """
    # Solution
    additional_words = []
    for word in range(ADDITIONAL_WORDS_NUM):
        while True:
            word_to_add = random.choice(WORDS)
            if len(word_to_add) == len(secret_word) and word_to_add != secret_word:
                additional_words.append(word_to_add)
                break

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
    
    Does not mutate the list additional_words.
    
    :returns True: if the guess is valid
    :returns False: if the guess is invalid
    """
    # Solution
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

    for letterA, letterB in zip(user_entry, secret_word):
        if letterA == letterB:
            num_correct += 1
    return num_correct


# ------------------------------------------- Assembly -------------------------------------------

if __name__ == '__main__':
    secret_w = pick_secret_word()
    while len(secret_w) < 2:
        # Make sure that no single / two character word lists are created
        secret_w = pick_secret_word()
    additional_w = get_additional_words(secret_w)
    word_display(secret_w, additional_w)
    print("Guess? ")
    for g in range(NUM_OF_GUESSES):
        guess = input().strip().upper()
        if is_valid_guess(guess, secret_w, additional_w):
            pass
        else:
            while not is_valid_guess(guess, secret_w, additional_w):
                print("Your guess is invalid!")
                print("Try again: ")
                guess = input().strip().upper()
        # handle game logic
        print(str(compare_user_entry(guess, secret_w)) + "/" + str(len(secret_w)) + " Correct.")
        if compare_user_entry(guess, secret_w) == len(secret_w):
            print("The secret word was:", secret_w)
            sys.exit("You won!")
        else:
            print(str(NUM_OF_GUESSES - g - 1), "guesses left.")
            if NUM_OF_GUESSES - g - 1 == 0:
                print("The secret word was:", secret_w)
                sys.exit("You lost!")


# ----------------------------------------- End of Assembly --------------------------------------

from SecondChallenge import *

# Note! If this file does not run in pycharm, go to the folder containing this file, right click,
# select "Mark Directory as" and then "Sources Root" . Things should start working from there.


def test_pick_secret_word():
    # Function does not test, only troubleshoots
    test_arr = []
    for w in range(5):
        test_arr.append(pick_secret_word())
    print('Five test cases: ')
    for num, val in enumerate(test_arr):
        if type(val) is not str:
            print("pick_secret_word failed!")
            print("The secret_word should be returned as a string.")
            print("Instead " + str(type(val)), "was returned.")
            return
        print("{}: {}".format(str(num+1), str(val)))

    print("Each secret_word in the previous test cases should be random")
    # Returns nothing


def test_get_additional_words():
    secret_word_test_values = ["MAYVILLE", "BUILDING", "MEMBERS", "INVESTIGATES", "QUITE", "ALTERNATIVELY"]

    for val in secret_word_test_values:
        test_li = get_additional_words(val)
        if len(test_li) != ADDITIONAL_WORDS_NUM:
            print("get_additional_words failed!")
            print("Expected: {} \nGot: {}".format("List of length " + ADDITIONAL_WORDS_NUM,
                                                  "List of length " + str(len(test_li))))
            


def test_is_valid_guess():
    pass

def test_compare_user_entry():
    pass


# Assembly
print("---------------------------------------")
print("Testing pick_secret_word()....")
test_pick_secret_word()
print("---------------------------------------")
print("Testing get_additional_words()....")
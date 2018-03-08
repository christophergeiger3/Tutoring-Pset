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

    print("pick_secret_word is successful if each of the previous test cases (each secret word) is random")
    # Returns nothing


def test_get_additional_words():
    secret_word_test_values = ["MAYVILLE", "BUILDING", "MEMBERS", "INVESTIGATES", "QUITE", "ALTERNATIVELY", "MIDST",
                               "INFESTATION", "SPILL", "BLUE"]

    for val in secret_word_test_values:
        test_li = get_additional_words(val)

        if test_li is None:
            print("get_additional_words() not yet implemented!")
            print("Returned: None")
            return
        elif len(test_li) != ADDITIONAL_WORDS_NUM:
            print("get_additional_words failed!")
            print("Expected: {} \nGot: {}".format("List of length " + ADDITIONAL_WORDS_NUM,
                                                  "List of length " + str(len(test_li))))
            return
        for v in test_li:
            if len(v) != len(val):
                print("get_additional_words failed!")
                print("Test case: " + val)
                print("Expected: {}".format("Additional words of length " + str(len(val))))
                print("Got list: {}".format(test_li))
                return
            elif val in test_li:
                print("get_additional_words failed!")
                print("Test case: " + val)
                print("Expected: {}".format("List that doesn't contain secret word"))
                print("Got: {}".format(test_li))
                return
    print("get_additional_words() was successful!")


def test_is_valid_guess():
    secret_word = "BUILDING"
    additional_words = ["MAYVILLE", "MEMBERS", "INVESTIGATES", "QUITE", "ALTERNATIVELY", "MIDST",
                        "INFESTATION", "SPILL", "BLUE"]
    user_entry_set = ["mayvill", "members", "investagates", "quote", "alternative", "midst", "building", "blow"]
    answer_set = [False, True, False, False, False, True, True, False]

    for inp, ans in zip(user_entry_set, answer_set):
        is_valid_guess(inp, secret_word.upper(), additional_words)
        if secret_word in additional_words:
            print("is_valid_guess() failed!")
            print("The additional_words list was mutated after running is_valid_guess()")
            print("Got: {} \nExpected: {}".format(additional_words, str(["MAYVILLE", "MEMBERS", "INVESTIGATES", "QUITE",
                                                                        "ALTERNATIVELY", "MIDST",
                                                                        "INFESTATION", "SPILL", "BLUE"])))
            print("Hint: Lookup the copy() command in Python for lists, and see why it's important")
            return
        if is_valid_guess(inp, secret_word.upper(), additional_words) == ans:
            continue
        else:
            if is_valid_guess(inp, secret_word, additional_words) is None:
                print("is_valid_guess() not yet implemented!")
                print("Returned: None")
                return
            print("is_valid_guess() failed!")
            print("Test case:\n\tSecret Word: " + secret_word + "\tAdditional Words: " + str(additional_words))
            print("Expected: {} \nGot: {}".format(ans, '"' + str(is_valid_guess(inp, secret_word, additional_words)
                                                                 + '"')))
            return

    print("is_valid_guess() was successful!")


def test_compare_user_entry():
    user_entry_set = ["DOG", 'CAT', 'BEANS', 'FIRE', 'PIZZA', 'DINGDONG', 'ANTAGONISTS', 'PROTAGONIST']
    secret_word_set = ['FOG', 'TAP', 'TREAT', 'PIER', 'THREE', 'HONGKONG', 'PROTAGONIST', 'ANTAGONISTS']
    answer_set = [2, 1, 0, 1, 0, 5, 0, 0]
    for u_e, s_w, ans in zip(user_entry_set, secret_word_set, answer_set):
        if compare_user_entry(u_e, s_w) == ans:
            continue
        else:
            print("compare_user_entry() failed!")
            print("Test case: \n\tUser entry: {}\n\tSecret Word: {}".format(str(u_e), str(s_w)))
            print("Expected: {} \nGot: {}".format(str(ans), str(compare_user_entry(u_e, s_w))))
            return
    print("compare_user_entry was successful!")


# Assembly
print("---------------------------------------")
print("Testing pick_secret_word()....")
test_pick_secret_word()
print("---------------------------------------")
print("Testing get_additional_words()....")
test_get_additional_words()
print("---------------------------------------")
print("Testing is_valid_guess()....")
test_is_valid_guess()
print("---------------------------------------")
print("Testing compare_user_entry()....")
test_compare_user_entry()
print("---------------------------------------")
sys.exit()

"""
1. Unlike Java, vars in Python can hold any value
2. The assignment operator -- Only works in one direction
    spam = 42
    42 = spam # Error
3. Invalid names:
    my variable # No spaces
    42_forty_two # Can't start with a number
    $$$money$$$ # No special characters like $$$ signs
    apostrophe' # No apostrophes (single-quotes) or double-qoutes
    my-variable # No hyphens
4. Storing to a variable
    spam = 10
    spam = 12 # The value 10 is now lost
    spam = 'spam' # The value 12 is now lost
    spam = spam + ' can' # The value within var spam is 'spam can'
5. Useful functions
    input() stops the program until the user hits enter
    len() gets the length of a string or a list
    range() creates an iterator up to a number -- more on that later
    print() shows something to the user and skips to the next line (\n)
    
"""
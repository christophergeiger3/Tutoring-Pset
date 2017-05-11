"""
    Hi Pablo!
    This is Christopher talking from beyond the grave. Spooky, right?
    Ok, but for real.
    This is your first challenge! You'll notice that in Python 3 notes can be written with triple double quotes (")
    or triple single quotes (')
    
    What I've laid out for you here is a test of your new-found python skills. Basically all I want you to do is follow
    the instructions written before each function to solve each problem.
    By the way: Any code that has the comment:
        # Helper Function! You don't need to understand this code!
    is something that I wrote to help the problem along. You don't need to understand it.
    
    I really hope you enjoy this, I've put a lot of effort into these problems, and if you ever need anything I'm only
    a message away. Like seriously. I'm pretty lonely actually.
    
    P.S.
    Keep the file labeled FirstChallenge.py in the same folder with test_firstchallenge.py, and do the same with all
    other challenge files, otherwise the test files won't work!
"""


def prompt_user():
    """
    The goal of this function is to print out several lines to the screen in the following format:
    1 - Add
    2 - Subtract
    3 - Multiply
    4 - Divide
    5 - Modulus
    
    After printing out these lines, the program should also return the user's choice as an integer.
    
    :returns selection: An integer selection, the user's selection.
    """
    # Write your code on the following lines!


    pass  # Remove this line when you are ready to test your function!


#  --- Helper function! You can skip this code... ---
def route(selection):
    """
    Given a user's selection, routes the code to the correct function.
    Passes to said function its necessary parameters.
    
    :param selection:
    """
    pass

def clear():
    """Clears out the console to make stuff in the final product easier to read"""
    print('\n'*100)

# --- End of Helper function ---

def add(n, k):
    """
    Given two integers, n and k, returns an integer ans, the sum of n and k
    
    :param n: An integer
    :param k: Another integer
    :returns ans: Your answer, as an integer
    """

    pass  # Remove this line when you are ready to test your function!

def subtract(n, k):
    """
    This problem is pretty similar to the last one!
    
    :param n: An integer
    :param k: Another integer
    :return ans: Your answer, ( n - k), as an integer
    """

    pass  # Remove this line when you are ready to test your function!

def multiplication(n, k):
    """
    Whoa! These are all easier than you thought they'd be, I bet!
    This one is almost the same as the others!
    
    :param n: An integer
    :param k: Another integer
    :return: Your answer, an integer
    """

    pass  # Remove this line when you are ready to test your function!

def division(n, k):
    """
    By now you've got the hang of it!
    
    :param n: An integer
    :param k: Another integer
    :return: Your answer, an integer
    """

    pass  # Remove this line when you are ready to test your function!

def modulus(n):
    """
    Alright, for this one we're going to switch things up. (Didn't want things to get to easy!)
    For this function I want you to return something different from just simply an integer.
    This time I want you to return True or False !
    
    
    :param n: An integer n that will be checked if even or odd 
    :returns: True if n is even (if n mod 2 is equal to zero)
    :returns: False if n is odd (if n mod 2 is equal to one)
    """

    pass  # Remove this line when you are ready to test your function!


# --- Assembly, you don't have to understand this part yet ---
while True:
    qwe = prompt_user()
    clear()
    route(qwe)
# --- End of Assembly ---

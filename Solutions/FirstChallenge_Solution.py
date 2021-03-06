"""
    This is your first challenge! You'll notice that in Python 3 notes can be written with triple double quotes (")
    or triple single quotes (')

    What I've laid out for you here is a test of your new-found python skills. Basically all I want you to do is follow
    the instructions written before each function to solve each problem.
    By the way: Any code that has the comment:
        # Helper Function! You don't need to understand this code!
    is something that I wrote to help the problem along. You don't need to understand it.

    I really hope you enjoy this, I've put a lot of effort into these problems, and if you ever need anything I'm only
    a message away.

    P.S.
    Keep the file labeled FirstChallenge.py in the same folder with test_firstchallenge.py, and do the same with all
    other challenge files, otherwise the test files won't work!
"""
import random

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
    print('1 - Add\n2 - Subtract\n3 - Multiply\n4 - Divide\n5 - Modulus')
    return int(input())


#  --- Helper function! You can skip this code... ---


def route(selection):
    """
    Given a user's selection, routes the code to the correct function.
    Passes to said function its necessary parameters.

    :param selection:
    """
    if selection == 1:
        print('Enter two integers n, k to add together: ')
        n, k = input().strip().split()
        print(add(int(n), int(k)))
        input("Press anything to continue...")

    elif selection == 2:
        print('Enter two integers n, k to subtract (n - k): ')
        n, k = input().strip().split()
        print(subtract(int(n), int(k)))
        input("Press anything to continue...")

    elif selection == 3:
        print('Enter two integers n, k to multiply them: ')
        n, k = input().strip().split()
        print(multiplication(int(n), int(k)))
        input("Press anything to continue...")

    elif selection == 4:
        print('Enter two integers n, k to divide them (n / k): ')
        if random.randint(0, 10) == 5:
            print("psst. What'd'ya think would happen if you divided by zero?")
        n, k = input().strip().split()
        print(division(int(n), int(k)))
        input("Press anything to continue...")

    elif selection == 5:
        print('Enter a single number, n, to determine if it is even or odd')
        n = int(input().strip())
        print("Even!" if modulus(n) else "Odd!")
        input("Press anything to continue...")

    else:
        print("That's not a valid input...")


def clear():
    """Clears out the console to make stuff in the final product easier to read"""
    print('\n' * 100)


# --- End of Helper function ---

def add(n, k):
    """
    Given two integers, n and k, returns an integer ans, the sum of n and k

    :param n: An integer
    :param k: Another integer
    :returns ans: Your answer, as an integer
    """
    return n+k


def subtract(n, k):
    """
    This problem is pretty similar to the last one!

    :param n: An integer
    :param k: Another integer
    :return ans: Your answer, ( n - k), as an integer
    """

    return n - k


def multiplication(n, k):
    """
    Whoa! These are all easier than you thought they'd be, I bet!
    This one is almost the same as the others!

    :param n: An integer
    :param k: Another integer
    :return: Your answer, an integer
    """

    return n*k


def division(n, k):
    """
    By now you've got the hang of it!

    :param n: An integer
    :param k: Another integer
    :return: Your answer, an integer
    """

    return n/k


def modulus(n):
    """
    Alright, for this one we're going to switch things up. (Didn't want things to get to easy!)
    For this function I want you to return something different from just simply an integer.
    This time I want you to return True or False !
    This function should return True if the given n is an even number, otherwise it should return False!
    Note: In Python, True and False are always denoted with an uppercase first letter.

    :param n: An integer n that will be checked if even or odd 
    :returns: True if n is even (if n mod 2 is equal to zero)
    :returns: False if n is odd (if n mod 2 is equal to one)
    """

    return True if n % 2 == 0 else False

# --- Assembly, you don't have to understand this part yet ---
if __name__ = "__main__":
    while True:
        clear()
        qweewq = prompt_user()
        clear()
        route(qweewq)
    
# --- End of Assembly ---

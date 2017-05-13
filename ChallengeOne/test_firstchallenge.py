from FirstChallenge import *

# Note! If this file does not run in pycharm, go to the folder containing this file, right click,
# select "Mark Directory as" and then "Sources Root" . Things should start working from there.

# ToDO: Implement test file; work on other challenges


# Addition
def test_add():
    test_cases = [(1, 2), (2, 3) , (3, 4) (0, 0) (10, 19)]
    for s in test_cases:
        if add(s[0], s[1]) == s[0] + s[1]:
            continue
        else:
            return False
    return True


# Subtraction
def test_sub():
    test_cases = [(1, 2), (2, 3), (3, 4)(0, 0)(10, 19)]
    for s in test_cases:
        if subtract(s[0], s[1]) == s[0] - s[1]:
            continue
        else:
            return False
    return True


# Multiplication
def test_mult():
    test_cases = [(1, 2), (2, 3), (3, 4)(0, 0)(10, 19)]
    for s in test_cases:
        if multiplication(s[0], s[1]) == s[0] * s[1]:
            continue
        else:
            return False
    return True


# Division
def test_div():
    test_cases = [(1, 2), (2, 3), (3, 4)(0, 0)(10, 19)]
    for s in test_cases:
        if division(s[0], s[1]) == s[0] + s[1]:
            continue
        else:
            return False
    return True


# Modulus
def test_mod():
    test_cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30]
    for num in test_cases:
        flag = True if num%2 == 0 else False
        if flag == modulus(num):
            continue

    return True

# Assembly
print("Testing add()....")
print("add() passed!") if test_add() else print("add() failed.")
print("Testing subtract()....")
print("subtract() passed!") if test_sub() else print("subtract() failed.")
print("Testing multiplication()....")
print("multiplication() passed!") if test_mult() else print("multiplication() failed.")
print("Testing division()....")
print("division() passed!") if test_div() else print("division() failed.")
print("Testing modulus()....")
print("modulus() passed!") if test_mod() else print("modulus() failed.")
"""
This part is very important for your practice problems!

Functions are like small programs within your main program that serve some purpose. One of the biggest strengths of
using functions is that when you use them, you don't have to duplicate code!
Example:
    # This code can be replaced with more concise code:
    print("Please select a number")
    num = int(input())
    if num == 1:
        print("Good morning number one")
    if num == 2:
        print("Hello number two")
    if num == 3:
        print("Greetings, number three")
    if num == 4:
        print("Welcome, number four")
    ...
    
    print("Now select another number")
    num = int(input())
    if num == 1:
        print("Good morning number one")
    if num == 2:
    ...
    
    
    # That code could be replaced with this:
    def greetings(n):
        # The function name is greetings() and n is its parameter
        if n == 1:
            print("Good morning number one")
        ...
        
    # The main program
    print("Please select a number")
    num = int(input())
    greetings(num) # The num variable is an argument passed to the function. The function then runs and returns here.
    print("Now select another number")
    num = int(input())
    greetings(num)
    
    
    So basically the same code from function is ran twice, but it only needed to be written once. This can be used in
    very clever ways. Example:
    # Function that determines if a number is even or odd.
    def isEven(n):
        if n%2 == 0:
            print( str(n) + " is even!" )
        else:
            print( str(n) + " is odd!" )
    
    for i in range(1, 21):
        isEven(i)

    
Challenge: Make a mathematical function for "to the power of two."
Example output:
    Enter a number to be squared: 3
    9
    
Bonus: Use your program to print all of the squares from 1 to 10.

Challenge: Create a mathematical function that models the following line:
    f(x) = 2x + 1
    Then ask the user for x values and print the corresponding y values.

"""
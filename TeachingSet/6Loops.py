"""
1. While loops:
    An infinite loop that keeps running until the statement given turns False
    Example:
        # Print all the numbers from 1-20
        x = 1
        while x <= 20:
            print(x)
            x += 1 # This is the same as saying x = x+1
        
        
        # Meet in the middle
        x, y = 1, 5
        while x != y: # Same as saying not x == y
            print(x)
            print(y)
            x += 1
            y -= 1
        print( 'x and y have the same value!' )
        
2. For loops
    Works somewhat differently than Java for loops
    Basically for loops run until they iterate completely through a list
    Also, they create a temporary variable where these values from the list are stored
    Example:
        # Print all the numbers from 0-10
        for i in range(11):
            print(i)
        
    The range() function produces a range from 0 to a number. You can also give the range() function more information
    so it loops differently.
    Example:
        range(1, 10) # Creates a loop from 1 to 10
        range(1, 10, 2) # Creates a loop from 1 to 10, counting by two
        range(10, 1, -1) # Creates a loop from 10 to 1, counting backwards by one
    
    Remember that range() does not print the 'stop' value given, for example, range(11) will give the values from 0 to
    10. This is because range() creates 11 values, starting from zero.
    
# Challenge:
    Create a loop that prints out "I am Pablo, hear me roar! (n)" where 'n' is replaced with how many times the phrase
    has been repeated. Example output:
        I am Pablo, hear me roar! (1)
        I am Pablo, hear me roar! (2)
        I am Pablo, hear me roar! (3)
        ...
    
    Create a dice roller. The program would first ask the user how many times to roll a six-sided die, then would
    generate that many values in the 1-6 range. Example:
        Roll a die how many times? 5
        1
        3
        3
        2
        6   
"""
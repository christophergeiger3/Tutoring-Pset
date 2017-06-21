"""
1. if someBooleanValueIsTrue:
        # Do this
    else:
        # Do that
    
    Note:
        The indented line
        The lack of a value for the else statement
        else is dependent on if

Examples from basic programs:
    1.
        print("Please enter the password: ")
        password = input()
        if password == 'hunter1':
            print("Access granted!")
        else:
            print("Access denied.")
    
    2.
        bankAccountBalance = 10
        print("Banco Popular:")
        print("Please enter the password for your account: ")
        password = input()
        if password == 'hunter1':
            print("Access granted!")
            if bankAccountBalance < 50:
                print("That's not a lot of money in your account')
            if bankAccountBalance > 50:
                print("Wow! That's a lot of money in your account!')
    
Challenges for Pablo:
    carSpeed = 50 # mph
    speedLimit = 60 # mph
    
    Create a program that given two variables: carSpeed and speedLimit, checks if the car is speeding or not. If the
    car is speeding, print a message that says it is, otherwise print a message that says it isn't
    
    Create a program that gets two inputs from the user and adds them together. Tell the user if the sum of the two
    numbers is greater than 100.
    
The elif statement:
    Like the else statement, but checks something first.
    Example:
        if name == 'Christopher':
            # do something
        elif name == 'Pablo':
            # do something
        elif name = 'Shrek':
            # do something
        else:
            print("Name not found")
        
    
"""
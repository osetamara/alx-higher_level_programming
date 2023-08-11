#!/usr/bin/python3

if __name__ == "__main__":
    # This block of code is executed when the script is run directly, not when imported.
    
    # Import the 'add' function from the 'add_0' module.
    from add_0 import add

    # Define the values of variables 'a' and 'b' for the addition operation.
    a = 1
    b = 2

    # Calculate the sum of 'a' and 'b' using the imported 'add' function.
    result = add(a, b)

    # Print the formatted output showing the addition operation and result.
    print("{} + {} = {}".format(a, b, result))

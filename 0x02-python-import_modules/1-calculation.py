#!/usr/bin/python3

if __name__ == "__main__":
    # This block of code is executed when the script is run directly, not when imported.

    # Import necessary functions from the calculator_1 module.
    from calculator_1 import add, sub, mul, div

    # Define the values of the variables a and b.
    a = 10
    b = 5

    # Print the sum of a and b.
    print("{} + {} = {}".format(a, b, add(a, b)))

    # Print the difference of a and b.
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # Print the product of a and b.
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # Print the quotient of a and b.
    print("{} / {} = {}".format(a, b, div(a, b)))

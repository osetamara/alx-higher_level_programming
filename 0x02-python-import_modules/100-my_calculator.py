#!/usr/bin/python3

if __name__ == "__main__":
    # This block of code is executed when the script is run directly, not when imported.

    # Import necessary functions and module from the standard library.
    from sys import argv
    from calculator_1 import add, sub, mul, div
    
    # Retrieve the number of command-line arguments.
    argc = len(argv)
    
    # Check if the correct number of arguments is provided.
    if argc != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)
    
    # Define a dictionary of operators and corresponding functions.
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    
    # Check if the provided operator is valid.
    if argv[2] in ops:
        num1 = int(argv[1])
        num2 = int(argv[3])
        op = ops[argv[2]]
        result = op(num1, num2)
        print('{:d} {:s} {:d} = {:d}'.format(num1, argv[2], num2, result))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    
    # Exit the script with a success code.
    exit(0)

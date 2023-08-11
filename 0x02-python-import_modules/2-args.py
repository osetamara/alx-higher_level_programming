#!/usr/bin/python3
# This script prints the number of and the list of its command-line arguments

if __name__ == "__main__":
    # This block of code is executed when the script is run directly, not when imported.
    
    import sys

    # Retrieve the list of command-line arguments.
    arg = sys.argv
    # Calculate the number of arguments provided.
    size = len(arg) - 1

    # Check the number of arguments and print appropriate messages.
    if size > 1:
        # If more than one argument is present.
        print("{} arguments:".format(size))
        for i in range(1, size + 1):
            # Print each argument's position and value.
            print("{}: {}".format(i, arg[i]))

    elif size == 0:
        # If no arguments are provided.
        print("{} arguments.".format(size))

    else:
        # If only one argument is provided.
        print("{} argument:".format(size))
        # Print the position and value of the single argument.
        print("{}: {}".format(size, arg[1]))

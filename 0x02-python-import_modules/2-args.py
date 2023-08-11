#!/usr/bin/python3

if __name__ == "__main__":
    # This block of code is executed when the script is run directly, not when imported.

    # Import the sys module, which provides access to command-line arguments.
    import sys

    # Calculate the number of command-line arguments.
    count = len(sys.argv) - 1

    # Check how many arguments were passed and print appropriate message.
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Iterate through the arguments and print their position and value.
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

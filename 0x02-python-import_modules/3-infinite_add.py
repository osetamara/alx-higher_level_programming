#!/usr/bin/python3

if __name__ == "__main__":
    # This block of code is executed when the script is run directly, not when imported.
    
    # Import the sys module to access command-line arguments.
    import sys

    # Initialize a variable to store the sum of arguments.
    total = 0

    # Iterate through the command-line arguments (excluding the script name).
    for i in range(len(sys.argv) - 1):
        # Convert each argument to an integer and add it to the total.
        total += int(sys.argv[i + 1])

    # Print the calculated total of all arguments.
    print("{}".format(total))

#!/usr/bin/python3

def add_arg(argv):
    # Function to add command-line arguments and print the sum
    
    # Calculate the number of command-line arguments.
    n = len(argv) - 1
    
    if n == 0:
        # If no arguments are provided.
        print("{:d}".format(n))
        return
    else:
        i = 1
        add = 0
        while i <= n:
            # Sum up the integer values of the arguments.
            add += int(argv[i])
            i += 1
        # Print the total sum.
        print("{:d}".format(add))

if __name__ == "__main__":
    # This block of code is executed when the script is run directly, not when imported.
    
    import sys
    # Call the add_arg function with command-line arguments.
    add_arg(sys.argv)

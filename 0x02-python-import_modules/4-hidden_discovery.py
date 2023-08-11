#!/usr/bin/python3

if __name__ == "__main__":
    # This block of code is executed when the script is run directly, not when imported.
    
    # Import the 'hidden_4' module to access its names.
    import hidden_4

    # Get a list of all names defined in the 'hidden_4' module.
    names = dir(hidden_4)

    # Iterate through the names and print those that are not private (don't start with '__').
    for name in names:
        if name[:2] != "__":
            # Print the non-private name.
            print(name)

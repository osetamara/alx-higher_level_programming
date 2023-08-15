#!/usr/bin/python3
# This script defines a function to print a matrix of integers.

def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers.    
    Args:matrix (list of lists): matrix be printed list represents row of integers.
               Defaults to an empty matrix if not provided.
    """
    # Loop through each row in the matrix
    for row in matrix:
        # Loop through each element in the current row
        for col in row:
            # Print each element with proper formatting,use a space separate elements  row
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        # Print a new line to move to the next row
        print()

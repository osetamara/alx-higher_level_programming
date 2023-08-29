#!/usr/bin/python3
class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize a square with a given size.
        
        Args:
            size (int): Size of the square's side. Default is 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


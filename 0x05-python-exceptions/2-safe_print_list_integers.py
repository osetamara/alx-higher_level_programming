#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
 """first element of a list and only integers

   Args:
      my_list(list): list to print elements from 
      x(int): number of element to my_list to print.

  Returns:
       real number of integer printed.
"""
  ret = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)

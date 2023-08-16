#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set(my_list)#create a set of unique
    num = 0#initialize a variable to store the sum
    for i in unique_list:#iterate through each unique number
        num += i
    return (num)

#!/usr/bin/env python 3
import random
"""Defines three functions:

1. get_requirements()
2. get_list_size()
3. create_list()
4. sort_list()
"""


def get_requirements():
    """Accepts 0 args. Displays program requirements."""
    print("Developer: Keith Faunce")
    print("Pseudo-Random Number Lists!")
    print("\nProgram Requirements:\n"
          + "1. Create pseudo-random list of numbers.\n"
          + "2. Sort pseudo-random list of numbers.\n"
          + "3. Must perform data and range validation.\n")
    
    print("***Resource(s)***\n"
          + "Generate pseudo-random numbers: https://docs.python.org/3/library/random.html\n"
          + "for loop with range() function: https://www.freecodecamp.org/news/python-for-loop-for-i-in-range,\n")
    
    print("Input:")

# Input/Process/Output: IPO


def get_list_size():
    """Accepts 0 args. Prompts for list size returns user-entered value. With data validation!"""
    # test valid int and w/in range
    while True:
        try:
            # intialize
            size = 0 

            # prompt size num
            size = int(input("Enter list size: "))

            is_within_range = False
            while not is_within_range:
                if size >= 1 and size <= 10:
                    is_within_range = True
                else:
                    print("List size must be between 1 and 10.\n")
                    size = int(input("Enter list size: "))

        except ValueError:
            print("Not an int! Try again.\n")
            continue
        else: return size


def create_list(size):
    """Accepts 1 args. Returns pseudo-random number list-no duplicates!"""
    # range() func syntax:
    # range(stop) # stop value madatory
    # range(start, stop[, step]) # start & stop values optional

    my_list = []
    for my_iterator in range(size):
        while True:
            # here, randint() returns int between 1 and size
            number = random.randint(1, size)
            # no duplicates
            if not number in my_list:
                my_list.append(number)
                break
    return my_list


def sort_list(test_list):
    """Accepts 1 args. Returns original and sorted number lists."""
    print("\nOriginal pseudo-random number list: ", test_list)

    test_list.sort()
    print("Sorted list (asc): ", test_list)

    test_list.sort(reverse=True)
    print("Sorted list (desc):", test_list)
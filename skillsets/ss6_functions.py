#!/usr/bin/env pyhton3
"""Defines four functions:

1. get_requirements()
2. get_list_size()
3. create_list()
4. get_sep_num()
5. get_list()
"""

def get_requirements():
    """Accepts 0 args, Displays program requirements."""
    print("Developer: Keith Faunce")
    print("Lists-***With Data Validation and Iteration!***")
    print("\nProgram Requirements:\n"
          + "1. Write a porgram that prints all elements of user-entered list, equal to and less than, or equal to and greater than user-entered value.\n"
          + "2. Must perform data validation.\n")
    
    print("***Resources***\n"
          + "Lists: https://docs.python.org/3.12/tutorial/datastructures.html\n")

    print("Input:")

def get_list_size():
    """Accepts 0 args. Prompts for list size, returns user entered value. With Data validation!"""
    # test valid int and w/in range
    while True:
        try:
            # intialize variable
            size = 0

            # prompt user for list size
            size = int(input("Enter list size: "))

            is_within_range = False
            while not is_within_range:
                if size >= 1 and size <= 10:
                    is_within_range = True
                else:
                    print("List length must be between 1 and 10.\n")
                    size = int(input("Enter list size: "))

        except ValueError:
            print("Not an integer! Try again.\n")
            continue
        else:
            return size
        

def create_list(length): 
    """Accepts 1 arg. Prompts user for list integers, based on list size. With Data Validation!"""
    # test valid int and w/in range
    # create empty list
    my_list = []

    while True:
        try:
            while len(my_list) < length:
                element = int(input("\nAdd number to list: "))
                my_list.append(element)
                print("Your number list:", my_list)

        except ValueError:
            print("Not an integer! Try again.\n")
            continue
        else:
            return my_list
        

def get_sep_num():
    """Accepts 0 args. Prompts for sperating number, returns user entered value. With Data Validation"""
    # test valid int and w/in range
    while True:
        try:
            # intialize variables
            number = 0

            # prompt user for separting integer
            number = int(input("\nEnter seperating number: "))

        except ValueError:
            print("Not an integer! Try again.\n")
            continue
        else:
            return number


def get_list(your_list, number):
    """Accepts 2 args. Returns list of user entered values based upon value entered."""
    # test seperating integer against list
    print("List numbers equal to and below sperating number: ", [
        my_int for my_int in your_list if my_int <= number
    ]) 


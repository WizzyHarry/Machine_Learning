#!/usr/bin/env python 3
import random
"""Defines four functions:

1. get_requirements()
2. get_lower()
3. get_higher()
4. play_game()
"""


def get_requirements():
    """Accepts 0 args. Displays program requirements."""
    print("Developer: Keith Faunce")
    print("Guessing Game!")
    print("\nProgram Requirements:\n"
          + "1. Create guessing game based upon pseudo-random numbers.\n"
          + "2. Must perform data and range validation.\n")
    
    print("***Resource(s):***\n"
          + "Generate psuedo-random numbers: https://docs.python.org/3/library/random.html\n")
    
    print("Input:")
# Input/Process/Output: IPO


def get_lower():
    """Accepts 0 args. Prompts for lower number, returns user-entered value. With data validation!"""
    # test valid int and w/in range
    while True:
        try:
            # intialzie variable(s)
            lower = 0

            # prompt lower number
            lower = int(input("Enter lower number: "))

            is_within_range = False
            while not is_within_range:
                if lower >= -1000 and lower <= 1000:
                    is_within_range = True
                else:
                    print("Lower must be between -1000 and 1000.\n")
                    lower = int(input("Enter lower: "))

        except ValueError:
            print("Not an int! Try again.\n")
            continue
        else:
            return lower


def get_upper():
    """Accepts 0 args. Prompts for upper number, returns user-entered value. With data validation!"""
    # test valid int and w/in range
    while True:
        try:
            # intialize
            upper = 0

            # prompt upper num
            upper = int(input("Enter upper number: "))

            is_within_range = False
            while not is_within_range:
                if upper >= -1000 and upper <= 1000:
                    is_within_range = True
                else:
                    print("Upper must be between -1000 and 1000.\n")
                    upper = int(input("Enter upper: "))

        except ValueError:
            print("Not an int! Try again.\n")
            continue
        else:
            return upper


def play_game(lower, upper):
    """Accepts 2 args. Creates psuedo-random number based upon user-entered values, and prompts user to guess."""
    # intialize
    count = 0
    rand_int = random.randint(lower, upper)

    while True:
        count += 1
        guess = int(input("\nEnter guess: "))

        if guess < rand_int:
            print("Too low!")
        elif guess > rand_int:
            print("Too high!")
        else:
            print("Bingo! Number of tries:", count)
            break
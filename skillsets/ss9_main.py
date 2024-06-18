#!/usr/bin/env python 3
import ss9_functions as f

def main():
    """Program entry. Calling enviornment to user-defined functions."""
    # intialize 
    low_num = 0
    high_num = 0

    # function calls
    f.get_requirements()
    low_num = f.get_lower()
    high_num = f.get_upper()

    # unit test
    # Note: In practice, test each function call individually

    while low_num > high_num:
        print("Lower number must be less than or equal to upper number! Try again!\n")
        low_num = f.get_lower()

    f.play_game(low_num, high_num)



if __name__ == "__main__":
    main()
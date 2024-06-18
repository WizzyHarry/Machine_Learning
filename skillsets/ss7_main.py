#!/usr/bin/env python 3
import ss7_functions as f


def main():
    """Program entry. Calling enviornment to user-defined functions."""
    # intialize
    size = 0
    your_list = [] # empty list

    # function calls
    f.get_requirements()
    size = f.get_list_size()
    your_list = f.create_list(size)
    # print(your_list) # check psuedo
    f.sort_list(your_list)




if __name__ == "__main__":
    main()

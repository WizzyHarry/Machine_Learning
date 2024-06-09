#!/usr/bin/env python3
import ss6_functions as f


def main():
    """Program entry. Calling environment to user defined functions"""
    # intialize variable
    size = 0
    num = 0
    your_list = [] # create empty list

    # functions calls
    f.get_requirements()
    size = f.get_list_size()
    your_list = f.create_list(size)
    num = f.get_sep_num()
    f.get_list(your_list, num)





if __name__ == "__main__":
    main()

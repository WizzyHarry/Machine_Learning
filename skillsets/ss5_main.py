#!/usr/bin/env python3
import ss5_functions as f


def main():
    # intialize variables
    h = 0.0
    w = 0.0

    # call funcs
    f.get_requirements()
    h = f.get_height()

    while w != -1:
        w = f.get_weight()
        f.calculate_bmi(h, w)


if __name__ == "__main__":
    main()
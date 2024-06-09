#!/usr/bin/env python3
import functions as f

def main():
    h = 0.0
    w = 0.0

    f.get_requirements()
    h = f.get_height()
    w = f.get_weight()

    f.calculate_bmi(h, w)


    if __name__ == "__main__":
        main()
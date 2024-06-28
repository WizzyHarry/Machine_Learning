#!/usr/bin/env python3
import ss10_functions as f

def main():
    """Program entry. Calling environment to user-defined functions."""

    # create empty lists
    your_items = []
    your_costs = []

    # func calls
    f.get_requirements()
    your_items = f.add_items()

    # use for testing return values
    # print(len(your_items), your_items)

    if len(your_items) == 0:
        print("No shopping cart items.")
    else:
        your_costs = f.get_items_cost(your_items)
        f.get_cart(your_items, your_costs)


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""Defines four functions:

1. get_requirements()
2. add_items()
3. get_items_cost()
4. get_cart()
"""


def get_requirements():
    """Accepts 0 args. Displays program requirements."""
    print("Developer: Keith Faunce")
    print("Simple Shopping Cart!")
    print("\nProgram Requirements:\n"
          + "1. Capture user-entered shopping items.\n"
          + "2. Retrieve cost for each item.\n"
          + "3. Print items, cost, and total of all items.\n"
          + "4. Must perform data and range validation.\n")
    
    print("***Resource(s)***\n"
          + "Prompt user until valid response: https://www.python-engineer.com/posts/ask-user-for-input/\n"
          + "Print tabular data: \n"
          + "\thttps://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data\n"
          + "\thttps://www.educba.com/python-print-table/\n")
    
    print("Input:")

def add_items():
    """Accepts 0 args. Prompts for item names, returns user-entered values, including item count. With data validation!"""
    # test string input

    print("Enter -1 to stop program.\n")

    # intialize variables
    name = ""
    count = 0
    my_items = []

    while name != "-1":
        try:
            # prompt for item name
            print("{0}{1} {2}".format(
                "Enter item", count + 1, "name: "), end="")
            
            name = input()
            name[0] # test for input

            # stop loop with flag value
            if name == "-1":
                print("Stopping list!\n")
                break

            count += 1 # increment counter variable
            my_items.append(name)

        except IndexError as e:
            # print(e) only used to print generated error msg
            print("No item name entered! Try again.\n")
            continue


    # use for testing logic
    return my_items


def get_items_cost(items_list):
    """Accepts 0 args. Prompts for item amount, returns user-entered value. With data validation!"""
    # test valid float and w/in range

    # intialize variables
    i = 0
    my_cost = []

    for my_iterator in range(len(items_list)):
        while True:
            try:
                #intialize
                cost = 0.0

                # prompt for item cost
                print("{0} {1} {2}".format(
                    "Enter", items_list[i], "cost: $"), end="")
                
                cost = float(input())

                is_within_range = False
                while not is_within_range:
                    if cost >= 1 and cost <= 100:
                        is_within_range = True
                    else:
                        print("Item cost must be between $1 and $100.\n")
                        print("{0} {1} {2}".format(
                            "Enter", items_list[i], "cost: $"), end="")
                        
                        cost = float(input())

                i += 1
                my_cost.append(cost)
                break

            except ValueError:
                print("Not a float! Try again.\n")
                continue

    return my_cost


def get_cart(items, costs):
    # intialize variables
    j = 0 
    total = 0.0

    print()

    # display table header
    print("{0:<10s} {1:<12s}".format("Item", "Cost"))

    while j < len(items):
        print("{0:<10s} {1:>6.2f}".format(items[j], costs[j]))
        total = total + costs[j] # accumlate total
        j += 1


    # display total
    print("\nTotal: ${0:.2f}".format(total))


    
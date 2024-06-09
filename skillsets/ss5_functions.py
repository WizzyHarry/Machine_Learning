#!/usr/bin/env pyhton3
"""Defines four functions:

1. get_requirements()
2. get_height()
3. get_weight()
4. calculate_bmi

"""

def get_requirements():
    """Accepts 0 args, Displays program requirements."""
    print("Developer: Keith Faunce")
    print("BMI Calculator-***With Data Validation and Iteration!***")
    print("\nProgram Requirements:\n"
          + "1. Research: BMI *English System* formula.\n"
          + "2. Must use float data type for user input and calculation.\n"
          + "3. Format and round conversion to two decimal places.\n")
    
    print("***Resources***\n"
          + "Accessing Your Weight and Health Risk: https://www.nhlbi.nih.gov/health/educational/lose_wt/risk.htm\n"
          + "Body Mass Index Tables: https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi_tbl.htm\n"
          + "Evaluate calculation: https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html\n"
          + "Data Validation: https://easypythondocs.com/validation.html\n")
    
    print("Input:")


def get_height():
    """Accepts 0 args, Prompts for height, returns user-entered value. With Data validation"""
    # test valid float and w/in range
    while True:
        try:
            # intialize variables
            height = 0.0 

            # get height
            height = float(input("Enter height (inches): "))

            is_within_range = False
            while not is_within_range:
                if height >= 45 and height <= 80:
                    is_within_range = True
                else:
                    print("Height must be between 45 and 80 inches.\n")
                    height = float(input("Enter height (inches): "))

        except ValueError:
            print("Not a float! Try again.\n")
            continue
        else:
            return height


def get_weight():
    """Accepts 0 args, Prompts for height, returns user-entered value. With Data validation"""
    # test valid float and w/in range
    while True:
        try:
            #intialize variables
            weight = 0.0

            # get weight
            weight = float(input("Enter weight (lbs) (Enter -1 to stop program): "))

            is_within_range = False
            while not is_within_range:
                if weight == -1:
                    return weight
                
                elif weight >= 80 and weight <= 400:
                    is_within_range = True

                else:
                    print("Weight must be between 80 and 400 pounds.\n")
                    weight = float(input("Enter weight (lbs): "))

        except ValueError:
            print("Not a float! Try again.\n")
            continue
        else:
            return weight


def calculate_bmi(height, weight):
    """Accepts 2 args. Calculates BMI, and prints output."""

    if weight == -1:
        print("Thank you for using the BMI program!")
    else:
        bmi = weight / height**2 * 703

        print("\nOutput:")
        print("{0} {1:,.2f} {2} {3:,.2f} {4} {5:,.2f}".format("height(inches) =", height, "| weight(lbs) =", weight, "| BMI =", bmi))
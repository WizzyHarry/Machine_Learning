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
    print("BMI Calculator-***No Data Validation!***")
    print("\nProgram Requirements:\n"
          + "1. Research: BMI *English System* formula.\n"
          + "2. Must use float data type for user input and calculation.\n"
          + "3. Format and round conversion to two decimal places.\n")
    
    print("***Resources***\n"
          + "Accessing Your Weight and Health Risk: https://www.nhlbi.nih.gov/health/educational/lose_wt/risk.htm\n"
          + "Body Mass Index Tables: https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi_tbl.htm\n"
          + "Evaluate calculation: https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html\n")
    
    print("Input:")
        

def get_height():
    """Accepts 0 args, Prompts for height, returns user-entered value. No Data validation"""
    # intialize variables
    height = 0.0

    # get height
    height = float(input("Enter height (inches): "))
    return height
    

def get_weight():
    """Accepts 0 args, Prompts for weight, returns user-entered value. No Data validation"""
    #intialize variable
    weight = 0.0

    # get weight
    weight = float(input("Enter weight (lbs): "))
    return weight
    

def calculate_bmi(height, weight):
    """Accepts 2 args, Calculates BMI and prints output"""
    bmi = weight / height**2 * 703

    print("\nOutput:")
    print("{0} {1:,.2f} {2} {3:,.2f} {4} {5:,.2f}".format("height(inches) =", height, "| weight(lbs) =", weight, "| BMI =", bmi))
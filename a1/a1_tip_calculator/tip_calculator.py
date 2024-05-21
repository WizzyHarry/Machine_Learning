Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Program requirements:
... print("Tip Calculator")
... 
... # Developer: Keith Faunce
... 
... # Course: LIS4930
... 
... # Semester: Summer 2024
... 
... print("\nProgram Requirements:\n"
...      + "1. Must use float data type for user input (except, \"Party Number\").\n"
...      + "2. Must round calculations to two decimal places.\n"
...      + "3. Must format currency with dollar sign, and two decimal places.")
... 
... print("\nUser Input:")
... meal_cost = float(input("Cost of meal: "))
... tax_percent = float(input("Tax percent: "))
... tip_percent = float(input("Tip percent: "))
... people_num = int(input("Party number: "))
... 
... # calculate tax, tip and total amount
... tax_amount = round(meal_cost * (tax_percent / 100), 2) # convert to percentage
... due_amount = round(meal_cost + tax_amount, 2)
... tip_amount = round((due_amount) * (tip_percent / 100),
...              2) # percentage of cost + tax
... total = round(meal_cost + tax_amount + tip_amount, 2)
... split = round(total / people_num, 2)
... 
... # display results
... # Formatting:
... # NEW!: https://realpython.com/pyhton-f-strings/
... # https://docs.python.org/3/library/string.html#format-specification-mini-language
... # https://docs.python.org/3/library/string.html#formatexamples
... # https://mkaz.blog/code/python-string-format-cookbook/
... print("\nProgram Output:")
print("Subtotal:\t", "${0:,.2f}".format(meal_cost)) # subtotal
print("Tax:\t\t", "${0:,.2f}".format(tax_amount))
print("Amount Due:\t", "${0:,.2f}".format(due_amount))
print("Gratuity:\t", "${0:,.2f}".format(tip_amount))
print("Total:\t\t", "${0:,.2f}".format(total))
print("Split" + "(" + str(people_num) + "):\t", "${0:,.2f}".format(split))


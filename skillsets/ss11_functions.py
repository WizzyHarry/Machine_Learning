#!/usr/bin/env python3
"""Defines five functions:

1. get_requirements()
2. add_emails()
3. get_phones()
4. create_contact()
"""


def get_requirements():
    """Accepts 0 args. Displays program requirements."""
    print("Developer: Keith Faunce")
    print("Working with lists, dictionaries, and user-entered values.")
    print("\nProgram Requirements:\n"
          + "1. Write a program that prints all elements of a user-entered contact list. \n"
          + "2. Must perform data validation.\n"
          + "3, Dictionary key *must* be user's e-mail address.\n")
    
    print("***Resource(s):***\n"
          + "Dictionaries:\n"
          + "https://www.codeacademy.com/learn/learn-python-3/modules/learn-python3-dictionaries/cheatsheet\n"
          + "https://www.pythoncheatsheet.org/cheatsheet/dictionaries\n")
    
    print("Input:")


def add_emails():
    """Accepts 0 args. Prompts for emails, returns user-entered values, including email count. With data validation"""
    # test string input

    print("Enter -1 to stop adding e-mails.\n")

    # intialize variables
    email = ""
    count = 0
    my_emails = []

    # Note: -1 flag value
    while email != "-1":
        try:
            # prompt for email
            print("{0} {1}{2}".format(
                "Enter email", count + 1, ": "), end="")
            
            email = input()
            # test for input (access first character)
            email[0]

            # stop loop w flag value
            if email == "-1":
                print("Stopping list!")
                break

            count += 1 # increment counter
            my_emails.append(email)

        except IndexError as e:
            print("No email entered! Try again/\n")
            continue

    return my_emails



def get_phones(emails_list):
    """Accepts 1 arg. Prompts for phone numbers, based upon emails, returns user-entered values. With Data Validation"""
    # intialize variables
    phone = ""
    i = 0
    my_phones = []

    for my_iterator in range(len(emails_list)):
        while True:
            try:
                # prompt for phone 
                print("\n{0}{1}".format(emails_list[i],", phone:"))

                phone = input()

                # test for input
                phone[0]

                i += 1 # increment
                my_phones.append(phone)
                break

            except IndexError as e:
                print("No phone entered! Try again.")
                continue

    return my_phones



def create_contact(keys, values):
    """Accepts 2 args. Creates dictionary based upon two list parameters. Displays dictionary elements"""
    my_dictionary = {}

    my_dictionary = dict(zip(keys, values))


    """
    -
    Following three functions returned through dictionary object:
    .keys() returns keys
    .values() returns values
    .items() returns both keys and values
    """

    print("\nPrinting dictionary:\n", my_dictionary)

    print("\nPrinting dictionary keys:\n", my_dictionary.keys())

    print("\nPrinting dictionary values:\n", my_dictionary.values())
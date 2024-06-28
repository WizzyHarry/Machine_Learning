#!/usr/bin/env python3
import ss11_functions as f


def main():
    """Program entry. Calling enviornment to user-defined functions."""
    # intialize variables
    your_emails = []
    your_phones = []

    # func calls
    f.get_requirements()
    your_emails = f.add_emails()


    if len(your_emails) == 0:
        print("No emails!")
    else:
        your_phones = f.get_phones(your_emails)


    f.create_contact(your_emails, your_phones)



if __name__ == "__main__":
    main()
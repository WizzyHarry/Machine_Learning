#!/usr/bin/env python3
import ss12_functions as f


def main():
    """Program entry. Calling enviornment to user-defined functions."""
    # func calls
    f.get_requirements()

    while True:
        f.get_menu() # display cwd and menu b4 each command
        command = f.get_command()

        if command != "7":
            f.run_command(command)
        else:
            print("\nStopping program!")
            break




if __name__ == "__main__":
    main()
#!/usr/bin/env python3
import os
import os.path

"""Defines nine functions:

1. get_requirements()
2. get_menu()
3. run_command()
4. list_dir()
5. move_up()
6. move_down()
7. num_files()
8. num_bytes()
9. find_files()
"""


def get_requirements():
    """Accepts 0 args. Displays program requirements."""
    print("Developer: Keith Faunce")
    print("Program provides file system navigation and information")
    print("\nProgram Requirements:\n"
          + "1. Write a program functions that navigate and display file system information. \n"
          + "2. Create and display program menu. \n"
          + "3. Must prevent incorrrect command input.\n")
    
    print("***Resource***\n"
          + "Python os package: https://docs.python.org/3/library/os.html\n")
    
    print("Input:")


# create constants
COMMANDS = ('1', '2', '3', '4', '5', '6', '7')
MENU = """1 List
2 Up
3 Down
4 Count
5 Size
6 Search
7 Quit"""


def get_menu():
    """Accepts 0 args. Prints current working directory (pwd), and displays menu items."""
    print("\nCurrent working directory:\n", os.getcwd(),"\n")
    print("MENU:\n", MENU, sep="")


def get_command():
    """Accepts 0 args. Returns command num or error msg"""
    while True:
        command = input("\nEnter command: ")
        if not command in COMMANDS:
            print("Incorrect command!")
        else:
            return command
        

def run_command(command):
    """Accepts 1 arg. Runs command based upon user-entered value."""
    if command == '1':
        list_dir(os.getcwd()) # lists cwd and all folders
    elif command == '2':
        move_up()
    elif command == '3':
        move_down(os.getcwd())
    elif command == '4':
        print("Total files:",
              num_files(os.getcwd()))
    elif command == '5':
        size = num_bytes(os.getcwd())

        print("{0}{1: ,d} {2}{3: ,.2f} {4}{5: ,.2f} {6}{7: ,.4f} {8}".format("\nTotal size:\n", size, "bytes\n", size / 1000, "KB\n", size / 1000000, "MB\n", size / 1000000000, "GB")) # error here

    elif command == '6':
        my_file = input("Enter file name: ")
        file_list = find_files(my_file, os.getcwd())
        if not file_list:
            print("File not found")
        else:
            # list found file in cwd and subdir
            print("\nFile paths for ", my_file, ":", sep="")
            for f in file_list:
                print(f)


def list_dir(dir_name):
    """Accepts 1 arg. List all files and dictionaries in cwd"""
    print("\nAll files and directories in ", "", dir_name, ":", sep="") # error here
    my_list = os.listdir(dir_name)
    for element in my_list:
        print(element)


def move_up():
    """Accepts 0 args. Move up to parent directory"""
    os.chdir("..")


def move_down(cur_dir):
    """Accepts 1 arg. Move down to named subdir if exists"""
    my_dir = input("Enter directory name: ")
    if os.path.exists(cur_dir + os.sep + my_dir) and \
        os.path.isdir(my_dir):
        os.chdir(my_dir)
    else:
        print("Incorrect dictionary name!")


def num_files(path):
    """Accepts 1 arg. Returns file count of cwd and subdir"""
    count = 0
    my_list = os.listdir(path)
    for element in my_list:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += num_files(os.getcwd())
            os.chdir("..")
    return count


def num_bytes(path):
    """Accepts 1 arg. Returns number of bytes in cwd and subdir"""
    size = 0
    my_list = os.listdir(path)
    for element in my_list:
        if os.path.isfile(element):
            size += os.path.getsize(element)
        else:
            os.chdir(element)
            size += num_bytes(os.getcwd())
            os.chdir("..")
    return size


def find_files(my_file, path):
    """Accepts 2 args. Returns list of file names in cwd and subdir"""
    files = []
    my_list = os.listdir(path)
    for element in my_list:
        if os.path.isfile(element):
            if my_file in element:
                files.append(path + os.sep + element)
        else:
            os.chdir(element)
            files.extend(find_files(my_file, os.getcwd()))
            os.chdir("..")
    return files

# File: list_maker.py - creates lists
# Author; Dustin Lamperts
# Created: 9 October 2018
# Last Edit:  2019


user_list = []
user_lists = {}


def new_list():
    """ Creates a new list for the user. """

    list_name = input('What is the title of your list? ')
    user_lists[list_name] = []


def print_lists():
    """ Shows all user list titles. """

    for key in user_lists.keys():
        print(key)


def remove_list():
    ''' Allows a user to delete a list.'''

    # Select list to remove
    to_remove = input('Which list do you want to delete? ')

    # Remove selected list
    del user_lists[to_remove]


def add_item():
    """ Allows user to add an item to the list. """

    # Select list to add item to
    list_to_edit = input('Which list do you want to add an item to? ')

    # Input item to be added
    user_item = input('Item to add to list: ')

    # Add item to chosen list
    user_lists[list_to_edit].append(user_item)


def print_items():
    """ Allows users to print out the list. """

    # Select list to print
    list_to_print = input('Which list do you want to print? ')

    # Print list title
    print(list_to_print.upper())
    print('=========\n')

    # Print items in list
    for item in user_lists[list_to_print]:
        print('  * ' + item)


def remove_item():
    """ Allows users to remove items from list. """

    # Choose list to remove item from
    list_to_edit = input('Which list would you like to remove an item from? ')

    # Choose item to remove
    user_item = input('Item to remove from list: ')

    # Remove selected item
    user_lists[list_to_edit].remove(user_item)


def print_menu():
    """ Prints out menu options for users. """
    
    print('Options'.upper())
    print('=======\n')
    print('  n: new list')
    print('  l: print lists')
    print('  d: delete list')
    print('  a: add item')
    print('  p: print items')
    print('  r: remove item')
    print('  q: quit')
    print()


# User Menu Loop

print_menu()
user_choice = input('Select a menu option: ')

while user_choice != 'q':
    if user_choice == 'n':
        new_list()
        print()
    elif user_choice == 'l':
        print_lists()
        print()
    elif user_choice == 'd':
        remove_list()
        print()
    elif user_choice == 'a':
        add_item()
        print()
    elif user_choice == 'p':
        print_items()
        print()
    elif user_choice == 'r':
        remove_item()
        print()
    
    print_menu()
    user_choice = input('Select a menu option: ')
    print()

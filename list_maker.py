#
# File: list_maker.py - creates lists
# Author; Dustin Lamperts
# Created: 9 October 2018
#

user_list = []

def add_item():
    user_item = input('Item to add to list: ')
    user_list.append(user_item)


def print_list():
    print('User List'.upper())
    print('=========\n')
    for item in user_list:
        print('  * ' + item)


def remove_item():
    user_item = input('Item to remove from list: ')
    user_list.remove(user_item)


def print_menu():
    print('Options')
    print('a: add item')
    print('p: print list')
    print('r: remove item')
    print('q: quit')
    print()


# User Menu Loop

print_menu()
user_choice = input('Select a menu option: ')

while user_choice != 'q':
    if user_choice == 'a':
        add_item()
        print()
    elif user_choice == 'p':
        print_list()
        print()
    elif user_choice == 'r':
        remove_item()
        print()
    
    print_menu()
    user_choice = input('Select a menu option: ')
    print()

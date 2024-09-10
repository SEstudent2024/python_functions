# 2. The Shopping List Maker
# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.

def add_item(shopping_list):
    item = input("What item would you like to add? ")
    shopping_list.append(item)
    print(f"{item} has been added to your shopping list.")

# Task 2: Include a function to remove items from the list.

def remove_item(shopping_list):
    item = input("What item would you like to remove from the shopping list?" )
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your sshopping list.")
    else:
        print(f"{item} is not in your shopping list.")

# Task 3: Add a function that prints out the entire list in a formatted way.
# Note: The goal of this is to be a program. The recommendation is to use a while loop that will 
# allow the user to continue to add, remove, and print off their shopping list until they decide to "quit", 
# also known as breaking the loop.

def print_list(shopping_list):
    if shopping_list:
        print("\n Your Shopping List: ")
        for i, item in enumerate(shopping_list, start = 1):
            print(f"{i}. {item}")
    else:
        print('\n Your Sshopping list is empty.')

def shopping_list_maker():
    shopping_list = []
    while True:
        print("\n Options: ")
        print("1 - Add Item: ")
        print("2 - Remove Item: ")
        print("3 - Print Shopping List: ")
        print("4 - Quit: ")
       
        choice = input("Choose a number: 1/2/3/4: ")
        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            print_list(shopping_list)
        elif choice == "4":
            print("Thank you for using the Shopping List Maker! Have a great day!")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    shopping_list_maker()
    
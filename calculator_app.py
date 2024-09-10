# 1. The Calculator App
# Objective: The aim of this assignment is to build a basic calculator that can perform addition, 
# subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.

def add (a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

# Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, 
# there is error handling set up to prevent an error from showing in the console.

def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero not valid."


# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

def calculator_app():
    print("Select an operation:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")

    while True:
        choice = input("Select a number: 1/2/3/4: ")
        if choice in ['1', '2,', '3', '4']:
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                if choice == '1':
                    print(f"The result is: {add(num1, num2)}")
                elif choice == '2':
                    print(f"The result is: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"The result is: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"The result is: {divide(num1, num2)}")
            except ValueError:
                print("Invalid Input. Please try again!")

        else:
            print("invalid choice. Please select a valid operation.")

        next_calculation = input("Would you like to try again? (yes or no): ")
        if next_calculation.lower() != "yes":
            break
calculator_app()
               


# TODO-1: Write out the other 3 functions - subtract, multiply and divide.
# TODO-2: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
# TODO-3: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
"""
Functionality
- Program asks the user to type the first number.
- Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
- Program asks the user to type the second number.
- Program works out the result based on the chosen mathematical operator.
- Program asks if the user wants to continue working with the previous result.
- If yes, program loops to use the previous result as the first number and then repeats the calculation process.
- If no, program asks the user for the first number again and wipes all memory of previous calculations.
- Add the logo from art.py
"""

import os 
import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    print(art.logo)
    n1 = float(input("What's the first number: "))

    while True:
        operator = input("+\n-\n*\n/\nChoose an operation: ")
        n2 = float(input("What's the second number: "))

        result = operations[operator](n1, n2)

        print(f"{n1} {operator} {n2} = {result}")

        continue_calculation = input(f"Type 'y' if you want to continue calculating with {result}, or type 'n' if you want to restart: ")

        if continue_calculation == "y":
            n1 = result
        else:
            os.system("cls")
            calculator()

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

calculator()
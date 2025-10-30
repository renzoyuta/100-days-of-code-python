# Task: PyPassword Generator
# 1. The program will ask how many letters, numbers and symbols would you like in your password
# 2. Generate the password
# 3. Easy: Generate the password in order: LettersNumbersSymbols
# 4. Hard: Generate the password in a random order: NumbersSymbolsLetters

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '+', '-', '*', '/']

print("Welcome to the PyPassword Generator!")
letters_count = int(input("How many letters would you like in your password?\n: "))
numbers_count = int(input("How many numbers would you like in your password?\n: "))
symbols_count = int(input("How many symbols would you like in your password?\n: "))

# Easy Version:

password = ""
for i in range(letters_count + numbers_count + symbols_count):
    if i < letters_count:
        password += random.choice(letters)
    elif i < numbers_count + letters_count:
        password += random.choice(numbers)
    elif i < symbols_count + letters_count + numbers_count:
        password += random.choice(symbols)

print("Your generated easy password is:", password)

# Hard Version:

password = list(password)
random.shuffle(password)

print("Your generated hard password is:", "".join(password))
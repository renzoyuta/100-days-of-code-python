# Task: Tip Calculator
# 1. Create a tip calculator that receives the total bill, the percentage tip and number of people
# 2. Return the bill with tip of each person

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n$"))
tip = int(input("What percentage tip would you like to give? 10 12 15\n"))
people = int(input("How many people to split the bill?\n"))

total_bill = bill + (tip / 100 * bill)
bill_per_person = round(total_bill / people, 2)

print(f"Each people should pay: ${bill_per_person}")
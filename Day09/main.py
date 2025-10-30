# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import os
import art

def find_highest_bidder(bids):
    winner_name = ""
    winner_bid = 0.0

    for key in bids:
        if bids[key] > winner_bid:
            winner_name = key
            winner_bid = bids[key]

    print(f"The winner of this blind auction is {winner_name} with a bid of ${winner_bid}")

bids = {}

print(art.logo)
print("Welcome to the secret auction program.")

while True:
    name = input("Type your name: ")
    bid = float(input("Type your bid: $"))

    bids[name] = bid

    continue_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if continue_bid == "no":
        break

    os.system("cls")

os.system("cls")
find_highest_bidder(bids)

import random
import os

import art
from game_data import data

continue_playing = "y"

while continue_playing == "y":
    score = 0

    game_over = False
    account_b = random.choice(data)

    while not game_over:
        os.system("cls")
        print(art.logo)

        account_a = account_b
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {account_a["name"]}, {account_a["description"]}, from {account_a["country"]}")
        print(art.vs)
        print(f"Against B: {account_b["name"]}, {account_b["description"]}, from {account_b["country"]}")
        
        comparisson = input("Who has more followers? Type 'A' or 'B': ").upper()

        follower_count_a = account_a["follower_count"]
        follower_count_b = account_b["follower_count"]

        if comparisson == 'A' and follower_count_a > follower_count_b:
            score += 1
            account_b = account_a
            print(f"You're right! Current score: {score}")

        elif comparisson == 'B' and follower_count_b > follower_count_a:
            score += 1
            print(f"You're right! Current score: {score}")

        else:
            os.system("cls")
            print(art.logo)
            print(f"You're wrong! Final Score: {score}")
            game_over = True
    
    continue_playing = input("Do you want play again? Type 'y' or 'n': ").lower()

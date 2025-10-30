# Task: Rock Paper Scissors
# Create a rock paper scissors game where first you choose between rock, paper and scissors
# Then, the computer randomly chooses between rock, paper and scissors

import random

def showdown(player_win):
    print(f"You chose:\n{rts_ascii[player]}")
    print(f"Computer chose:\n{rts_ascii[computer]}")
    if player_win:
        return print("You Win.")
    else:
        return print("You lose.")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rts_ascii = [rock, paper, scissors]
computer = random.randint(0, 2)
player = int(input("What do you choose? Type '0' for rock, '1' for paper and '2' for scissors: "))

if player == computer:
    print(f"You chose:\n{rts_ascii[player]}")
    print(f"Computer chose:\n{rts_ascii[computer]}")
    print("Draw.")

elif player == 0:
    if computer == 1:
        showdown(False)

    else:
        showdown(True)

elif player == 1:
    if computer == 0:
        showdown(True)
    
    else:
        showdown(False)

elif player == 2:
    if computer == 0:
        showdown(False)
    
    else:
        showdown(True)

else:
    print("You didn't chose a valid option.")
import random
import art

EASY_DIFFICULTY_ATTEMPTS = 10
HARD_DIFFICULTY_ATTEMPTS = 5

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        attempts = EASY_DIFFICULTY_ATTEMPTS
    else:
        attempts = HARD_DIFFICULTY_ATTEMPTS

    return attempts

def check_guess(guess):
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("You win!")

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("The game is simple, I will think of a number between 1 and 100 and you have to guess the number.")

attempts = set_difficulty()

number = random.randint(1, 100)

guess = 0
while guess != number:
    print(f"You have {attempts} attempts left.")
    guess = int(input("Make a guess: "))
    
    attempts -= 1
    
    if attempts == 0:
        print("You lost!")
        break

    check_guess(guess)
    
print("The number was:", number)
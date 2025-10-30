import random

word_list = ["prison", "nurse", "rain", "expert", "quack", "view", "paste", "friendly", "square", "energetic", "expand", "float", "cloudy", "game", "cracker", "chivalrous", "smell", "contribute", "harsh"] 

chosen_word = random.choice(word_list)

print(f"Chosen word: {chosen_word}")

# TODO-1: Use a while loop to let the user guess again.
correct_letters = []
game_over = False

while not game_over:
    display = ""
    guess = input("Guess a letter of the word: ").lower()

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.
    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if "_" not in display:
        game_over = True
import random

word_list = ["prison", "nurse", "rain", "expert", "quack", "view", "paste", "friendly", "square", "energetic", "expand", "float", "cloudy", "game", "cracker", "chivalrous", "smell", "contribute", "harsh"] 

chosen_word = random.choice(word_list)

print(f"Chosen word: {chosen_word}")

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = "_" * len(chosen_word)

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
guess = input("Guess a letter of the word: ").lower()

display = ""
for letter in chosen_word:
    if letter == guess:
        display += guess
    else:
        display += "_"
        
print(display)
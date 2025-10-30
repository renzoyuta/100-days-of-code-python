import random

word_list = ["prison", "nurse", "rain", "expert", "quack", "view", "paste", "friendly", "square", "energetic", "expand", "float", "cloudy", "game", "cracker", "chivalrous", "smell", "contribute", "harsh"] 

# TODO-1 Randomly chooses a word from the word_list and assign it into a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(f"Chosen word: {chosen_word}")

# TODO-2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter of the word: ").lower()

# TODO-3 Check if the letter the user guessed (guess) is one of the letter in the chosen_word. Print "Right" if it, "Wrong" if it's not.
for letter in chosen_word:
    if letter == guess:
        print("Right!")
    else:
        print("Wrong!")
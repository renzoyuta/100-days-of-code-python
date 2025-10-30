import random

word_list = ["prison", "nurse", "rain", "expert", "quack", "view", "paste", "friendly", "square", "energetic", "expand", "float", "cloudy", "game", "cracker", "chivalrous", "smell", "contribute", "harsh"] 

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)

print(f"Chosen word: {chosen_word}")

correct_letters = []
game_over = False

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.
lives = 6

while not game_over:
    display = ""
    guess = input("Guess a letter of the word: ").lower()

    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in display:
        lives -= 1

    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
    print(display)

    if "_" not in display:
        game_over = True
        print("You Win.")

    elif lives == 0:
        game_over = True
        print("You Lose.")


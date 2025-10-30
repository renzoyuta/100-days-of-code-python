import random

import hangman_art
import hangman_words

word_list = hangman_words.word_list

lives = 6

print(hangman_art.logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letter = []
stages = hangman_art.stages

while not game_over:
    print(
        f"****************************{lives}/6 LIVES LEFT****************************"
    )

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letter:
            print("You've already guessed this letter, try another one")
            print(f"Guessed letters: {', '.join(guessed_letter)}")
            print()

        else:
            break

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    guessed_letter.append(guess)

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

            print("***********************YOU LOSE**********************")
            print(f"The correct word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])

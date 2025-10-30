import os
import random
import art

def sum_cards(cards):
    """Take a list of cards and return the sum

        Convert High cards into their respective number
    """
    cards_sum = 0
    for card in cards:
        if card == "A":
            cards_sum += 11
        elif card in ["J", "Q", "K"]:
            cards_sum += 10
        else:
            cards_sum += card

    if cards_sum > 21 and "A" in cards:
        cards_sum -= 10
        return cards_sum
    return cards_sum

def blackjack_check(player_cards, computer_cards, player_sum_cards, computer_sum_cards):
    if player_sum_cards == 21 and computer_sum_cards == 21:
        print(f"You got a blackjack with {player_cards}!")
        print(f"The computer got a blackjack with {computer_cards}!")
        print("Draw!")
        return True

    elif player_sum_cards == 21:
        print(f"You got a blackjack with {player_cards}! You win!")
        return True
    
    elif computer_sum_cards == 21:
        print(f"The computer got a blackjack with {computer_cards}! You lose!")
        return True
    
    return False

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

continue_playing = True

while continue_playing:
    os.system("cls")

    print(art.logo)
    print("Welcome to the Blackjack game. Dealer draw to 16 and stand on 17.")

    player_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]

    player_sum_cards = sum_cards(player_cards)
    computer_sum_cards = sum_cards(computer_cards)
    
    player_bust_stand = blackjack_check(player_cards, computer_cards, player_sum_cards, computer_sum_cards)

    while not player_bust_stand:
        print(f"Your cards: {player_cards}, current score: {player_sum_cards}")
        print(f"Computer's hand: {computer_cards[0]}")

        hit_or_stand = input("Type 'y' to hit another card, type 'n' to stand: ").lower()

        if hit_or_stand == "y":
            os.system("cls")

            card_hit = random.choice(cards)
            player_cards.append(card_hit)
            player_sum_cards = sum_cards(player_cards)
            print(f"You chose to hit. Card drawn: {card_hit}")

            if player_sum_cards > 21:
                player_bust_stand = True
                print(f"You busted. Your final hand: {player_cards}, your final score: {player_sum_cards}")
                print("You went over 21. You lose!")

        elif hit_or_stand == "n":
            os.system("cls")

            player_bust_stand = True
            print(f"You chose to stand. Your final hand: {player_cards}, your final score: {player_sum_cards}")

            computer_bust_stand = False

            while not computer_bust_stand:
                card_hit = random.choice(cards)
                computer_cards.append(card_hit)
                computer_sum_cards = sum_cards(computer_cards)

                print(f"Computer's hand: {computer_cards}, his score: {computer_sum_cards}")

                if computer_sum_cards >= 17:
                    if computer_sum_cards > 21:
                        print(f"Computer busted. His final hand: {computer_cards}, His final score: {computer_sum_cards}")
                        print("Computer went over 21. You Win!")

                    else:
                        print(f"Computer's final hand: {computer_cards}, computer final score: {computer_sum_cards}")

                        if player_sum_cards > computer_sum_cards:
                            print("You Win!")

                        elif computer_sum_cards > player_sum_cards:
                            print("You lose!")

                        else:
                            print("You Draw!")

                    computer_bust_stand = True

    continue_playing = input("Do You want to continue playing? Type 'y' or 'n': ").lower()

    if continue_playing == "n":
        continue_playing = False
    else:
        print("Thanks for playing!")
        continue_playing = True

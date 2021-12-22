from replit import clear
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal(num_cards):
    tempCards = []
    for card in range(num_cards):
        tempCards.append(random.choice(cards))
    return tempCards


user_cards = []
computer_cards = []

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    continueGame = True
else:
    continueGame = False

while continueGame:
    clear()
    print(logo)

    continueRound = True
    # deal cards
    user_cards = deal(2)
    computer_cards = deal(2)
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    # check for blackjack
    if sum(user_cards) == 21:
        print("Blackjack! You won!")
        continueGame = False
    elif sum(computer_cards) == 21:
        print("Blackjack! The computer won!")
        continueGame = False

    # users turn
    while continueRound:
        if input(f"Type 'y' to get another card, type 'n' to pass: ") == 'y':
            user_cards.append(deal(1)[0])
            # check if the user bust
            if sum(user_cards) > 21:
                # if they bust check for an eleven and replace with an 1
                if 11 in user_cards:
                    for index, card in enumerate(user_cards):
                        if card == 11:
                            user_cards[index] = 1
                else:
                    continueRound = False
                    continueGame = False
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")
        else:
            continueRound = False

            # computers turn
    while sum(computer_cards) < 17:
        computer_cards.append(deal(1)[0])
    print(f"Your final hand: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score {sum(computer_cards)}")

    # toal it up
    if sum(computer_cards) > 21:
        print("The computer went over. You won!")
    elif sum(user_cards) > 21:
        print("You went over. You lose.")
    elif sum(user_cards) > sum(computer_cards):
        print("You won!")
    elif sum(user_cards) == sum(computer_cards):
        print("It's a push!")
    else:
        print("You lose!")

    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        continueGame = True
    else:
        continueGame = False

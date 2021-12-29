import random
import art
import random
import game_data
from replit import clear

dataDB = game_data.data
unusedDataSeeds = []
continueGame = True


def getData():
    global unusedDataSeeds
    seed = random.choice(unusedDataSeeds)
    unusedDataSeeds.remove(seed)
    return dataDB[seed]


def formatData(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


for i in range(0, len(dataDB)):
    unusedDataSeeds.append(i)

score = 0
print(art.logo)

while continueGame:
    account_a = getData()
    account_b = getData()

    print(f"Compare A: {formatData(account_a)}.")
    print(art.vs)
    print(f"Against B: {formatData(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(art.logo)
    if is_correct and len(unusedDataSeeds) > 0:
        score += 1
        print(f"You're right! Current score: {score}.")
    elif len(unusedDataSeeds) == 0:
        continueGame = False
        print(f"You're right! No more questions! You win the game! Final score: {score}.")
    else:
        continueGame = False
        print(f"Sorry, that's wrong. Final score: {score}")


import random
from art import logo

def check_guess(num_guessed):
    # Using a global varible in a function
    # bad practice but wanting to use what was learned today
    global isWinner
    if num_guessed == NUMBER:
        result = f"You got it! The answer was {NUMBER}."
        isWinner = True
    elif num_guessed < NUMBER:
        result = "Too low."
    elif num_guessed > NUMBER:
        result = "Too high."
    else:
        result = "Cannot compute."
    return result

NUMBER = random.randint(1, 100)
isWinner = False
count = 0

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    number_of_guesses = 10
else:
    number_of_guesses = 5

while count < number_of_guesses and not isWinner:
    print(f"You have {number_of_guesses - count} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    print(check_guess(guess))
    count += 1

if count == number_of_guesses and not isWinner:
    print("You've run out of guesses, you lose.")

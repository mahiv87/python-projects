import random

print("Welcome to the Number Guessing Game!")

# Global variables
EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5
def start_game():
    print("I'm thinking of a number between 1 and 100.")

    # Ask user to choose difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    # Generate a random number between 1 and 100
    number = random.randrange(0, 100, 1)
    is_correct = False

    # Conditional to set guess attempts
    attempts = 0
    if difficulty == "easy":
        attempts = EASY_DIFFICULTY
    else:
        attempts = HARD_DIFFICULTY

    # Loop to check guessed number
    while attempts != 0 and not is_correct:
        guess = int(input("Make a guess: "))

        if guess > number:
            print("Too high. \nGuess again.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining")
        elif guess < number:
            print("Too low. \nGuess again.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining")
        else:
            print(f"You guess the correct number! The answer was {number}")
            is_correct = True

    if attempts == 0:
        print(f"You ran out of attempts... The answer was {number}")

# Init game
start_game()

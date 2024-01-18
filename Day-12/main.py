import random

print("Welcome to the Number Guessing Game!")


def start_game():
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    number = random.randrange(0, 100, 1)
    is_correct = False
    attempts = 5
    if difficulty == "easy":
        attempts += 5

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


start_game()

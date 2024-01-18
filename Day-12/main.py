print("Welcome to the Number Guessing Game!")

def start_game():
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    attempts = 5
    if difficulty == "easy":
        attempts += 5

    print(attempts)


start_game()
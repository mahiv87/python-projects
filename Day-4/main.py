import random

print("Let's play Rock, Paper, Scissors!")

question = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

# Convert input to int
response_to_int = int(question)

# List of options to compare against input
options = [0, 1, 2]

# Randomly generate cpu choice
cpu_choice = random.randint(0, 2)

# Conditionals for results
if options[response_to_int] == options[0] and cpu_choice == options[2]:
    print(f"Computer chose: {cpu_choice}. You win!")
elif options[response_to_int] == options[0] and cpu_choice == options[1]:
    print(f"Computer chose: {cpu_choice}. You lose...")
elif options[response_to_int] == options[1] and cpu_choice == options[0]:
    print(f"Computer chose: {cpu_choice}. You win!")
elif options[response_to_int] == options[1] and cpu_choice == options[2]:
    print(f"Computer chose: {cpu_choice}. You lose...")
elif options[response_to_int] == options[2] and cpu_choice == options[0]:
    print(f"Computer chose: {cpu_choice}. You lose...")
elif options[response_to_int] == options[2] and cpu_choice == options[1]:
    print(f"Computer chose: {cpu_choice}. You win!")
else:
    print(f"Computer chose: {cpu_choice}. Draw!")
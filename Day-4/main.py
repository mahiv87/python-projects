import random

print("Let's play Rock, Paper, Scissors!")

question = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

response_to_int = int(question)

options = [0, 1, 2]

cpu_choice = random.randint(0, 2)


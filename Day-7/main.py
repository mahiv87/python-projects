# Step 1
import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# print(chosen_word)
guess = input("Guess a letter: \n").lower()
# print(guess)

display = []

for index in range(len(chosen_word)):
    display += "_"
print(display)

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)


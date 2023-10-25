import random
print("Welcome to the PyPassword Generator")

# Strings of options
letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
numbers = '1 2 3 4 5 6 7 8 9 0'
symbols = '! @ # $ % ^ & *'

# Convert strings to Lists
letters_array = letters.split()
numbers_array = numbers.split()
symbols_array = symbols.split()

# Get user input
letter_input = int(input("How many letters would you like in your password?\n"))
symbols_input = int(input("How many symbols would you like?\n"))
numbers_input = int(input("How many numbers would you like?\n"))

password_list = []
password = ''

# Loop through Letters and push to password_list
for char in range(1, letter_input + 1):
    password_list.append(random.choice(letters_array))

# Loop through Numbers and push to password_list
for n in range(1, numbers_input + 1):
    password_list.append(random.choice(numbers_array))

# Loop through Symbols and push to password_list
for i in range(1, symbols_input):
    password_list.append(random.choice(symbols_array))

# Shuffle the password_list so that the password isnt in input order
random.shuffle(password_list)

# Loop through password_list to convert to String
for char in password_list:
    password += char

print(password)


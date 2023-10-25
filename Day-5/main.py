import random
print("Welcome to the PyPassword Generator")

letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
numbers = '1 2 3 4 5 6 7 8 9 0'
symbols = '! @ # $ % ^ & *'

letters_array = letters.split()
numbers_array = numbers.split()
symbols_array = symbols.split()

letter_input = int(input("How many letters would you like in your password?\n"))
symbols_input = int(input("How many symbols would you like?\n"))
numbers_input = int(input("How many numbers would you like?\n"))

password_list = []
password = ''

for char in range(1, letter_input + 1):
    password_list.append(random.choice(letters_array))

for n in range(1, numbers_input + 1):
    password_list.append(random.choice(numbers_array))

for i in range(1, symbols_input):
    password_list.append(random.choice(symbols_array))

random.shuffle(password_list)

for char in password_list:
    password += char

print(password)


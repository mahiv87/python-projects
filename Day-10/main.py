# # Functions with Outputs
# def format_name(f_name, l_name):
#     """Take a first and last name and return the title case version of the name."""
#     return f"{f_name.title()} {l_name.title()}"
#
# print(format_name("marcus", "herrera"))

# Py-Calculator ==================================================
print("Let's calculate!")

# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    return x / y

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("Whats the first number?: "))
num2 = int(input("Whats the second number?: "))




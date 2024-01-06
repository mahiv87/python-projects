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
for op in operations:
    print(op)
should_continue = True

while should_continue:
    operation_selection = input("Pick an operation: ")
    num2 = int(input("Whats the next number?: "))
    calc = operations[operation_selection]
    answer = calc(num1, num2)

    print(f"{num1} {operation_selection} {num2} = {answer}")
    proceed = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")

    if proceed == "y":
        num1 = answer
    else:
        should_continue = False





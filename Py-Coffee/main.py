MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 3.0
    }
}

profit = 0
resources = {
    "water": 800,
    "milk": 400,
    "coffee": 200
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins(drink_cost):
    print(f"Please insert ${drink_cost}")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"${change} returned")
        global profit
        profit += drink_cost
        return True
    else:
        print("Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Your {drink_name} is ready. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like to order? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins(drink["cost"])
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
# Dictionaries ==========================================================
# programming_dictionary = {
#     "Bug": "Definition for Bug",
#     "Function": "Definition for Function",
# }
#
# # Retrieving items from dictionary
# # print(programming_dictionary)
#
# # Adding new items to dictionary
# programming_dictionary["Loop"] = "Defintion for a Loop"
# # print(programming_dictionary)
#
# # Create an empty dictionary
# empty_dictionary = {}
#
# # Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)
#
# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "An error in a program that prevents the program from running as expected."
# # print(programming_dictionary)
#
# # Loop through a dictionary
# for key in programming_dictionary:
#     # print key
#     print(key)
#     # print value
#     print(programming_dictionary[key])

# # Nesting =================================================================
# capitals = {
#     "France": "Paris",
#     "USA": "Washington DC",
#     "Germany": "Berlin",
# }
#
# # Nesting a List in a Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }
#
# # Nesting a Dictionary in a Dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
# }
#
# # Nesting a Dictionary in a List
# travel_log = [
#     {
#      "country": "France",
#      "cities_visited": ["Paris", "Lille", "Dijon"],
#      "total_visits": 12
#     },
#     {
#      "country": "Germany",
#      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#      "total_visits": 5
#     }
# ]

# Secret Auction =================================================================
import os

print("Welcome to the Secret Auction")

bids = {}
finished = False


def clear():
    os.system('cls')


def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        amount = bidding_record[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not finished:
    name = input("What is your name?")
    bidding_price = int(input("What is your bid? $"))
    bids[name] = bidding_price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'")
    if should_continue == "no":
        finished = True
        highest_bidder(bids)
    elif should_continue == "yes":
        clear()

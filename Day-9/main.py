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

# Nesting =================================================================
capitals = {
    "France": "Paris",
    "USA": "Washington DC",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting a Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

# Nesting a Dictionary in a List
travel_log = [
    {"country": "France", "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    {"country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
]
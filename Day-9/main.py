programming_dictionary = {
    "Bug": "Definition for Bug",
    "Function": "Definition for Function",
}

# Retrieving items from dictionary
# print(programming_dictionary)

# Adding new items to dictionary
programming_dictionary["Loop"] = "Defintion for a Loop"
# print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "An error in a program that prevents the program from running as expected."
# print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    # print key
    print(key)
    # print value
    print(programming_dictionary[key])
programming_dictionary = {
    "bug" : "an erro in a program",
    "function" : "a piece of code",
}

print(programming_dictionary["bug"])

#Adding a new dictionary
programming_dictionary["loop"] = "the action of doing"

#creationg a empty dictionary
empty_dictionary = {}

#wipe an existing sictionary
programming_dictionary = {}
print(programming_dictionary)

#edit a dictionary
programming_dictionary["bug"] = "yabadabadooooo"

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
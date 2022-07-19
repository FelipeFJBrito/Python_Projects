#Write a Python program to iterate over dictionaries using for loops
d = {'x': 10, 'y': 20, 'z': 30} 
for dict_key, dict_value in d.items(): # items() Return the dictionary's key-value pairs:
    print(dict_key,'->',dict_value)
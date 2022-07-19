#Write a Python script to check whether a given key already exists in a dictionary. 

dictionary = {
    1: 256
}

for key in dictionary:
    test_key = int(input("Enter a interger key: "))
    if key == test_key:
        print(f"{key}")
    else:
        print(f"key is not in the dictionary, the keys that are available are {key}")

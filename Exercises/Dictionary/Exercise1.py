# Write a Python script to add a key to a dictionary.
dictionary  = {
        0: 10,
        1: 20,
}
check = True
while check:

    print(dictionary)
    key = int(input("Enter a Key number: "))
    value = int(input("Enter a Value number: "))
    dictionary[key] = value

    if input(f"Continue type 'y' or 'n' ") == "n":
        check = False
print(dictionary)


#Write a program that reads a 10-character vector, and tells you how many consonants were read. Print the consonants.

consonant = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

data_word = []
word = []
for i in range(0, 5):
    data = input("Enter your words: ")
    data_word.append(data)

for char in data_word:
    for cher in  consonant:
        if char == cher:
            word.append(char)

qt_consonant = len(word)
print(f"We have: {qt_consonant} consonants, and it is {word}")           


          
import random

input("which side do you want head or tail ?: ").lower()

number =  random.randint(1,2)
if number == 1:
    print("head is the winner")
else:
    print("tail is the winner")
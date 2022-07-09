import random

#name_string = input("Give me everybody's names separated by a comma. ")
#names = name_string.split(", ")
#print(names)
#winner = random.choice(names)
#print(f"{winner} is going to pay the meal")


name_string = input("Give me everybody's names separated by a comma. ")

names = name_string.split(", ")

num_itens = len(names)

random_choice = random.randint(0, num_itens -1)
winner  = names[random_choice]
print(f"{winner} is going to pay the meal")
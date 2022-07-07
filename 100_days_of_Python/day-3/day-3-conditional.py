print("Welcome to the rollercoaster!")
height =  int(input("What is your height in cm? "))
bill = 0

if height >=120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("please pay $5.")
    elif age <=18:
        bill = 7
        print("please pay $7.")     
    else:
        bill = 12
        print("please pay $12.")

    wants_photo = input("Whould you like a photo? Y or N. ")
    if wants_photo == "Y" or "y":
        bill += 3
        print(f"Final bill is: ${bill} ") 
    elif wants_photo == "N" or "n":
        print("see you next time ")    
else:
    print("Sorry you have to grow taller before you can ride.")            
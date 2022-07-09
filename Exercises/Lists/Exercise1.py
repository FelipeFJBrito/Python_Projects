#Write a program that reads an array of 5 integers and displays them.

list= [] # first we have to create a list 
print("Enter Numbers")
for n in range(0 , 5):  
    data = int(input())#Make a for data will recive the numbers
    list.append(data)#and the list.append will add the data inside the list
print(list)
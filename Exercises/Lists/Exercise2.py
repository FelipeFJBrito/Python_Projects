#Write a program that reads an array of 10 real numbers and displays them in reverse order.

list = []
print("Enter the numbers")
for n in range(0,3):
    data = float(input())
    list.append(data)

#two methods to reverse the lis 
list.reverse()#using function reverse()
reverse_list = list[::-1]#using Slicing operator()

print(f"Method one {list}")
print(f"Method two {reverse_list}")


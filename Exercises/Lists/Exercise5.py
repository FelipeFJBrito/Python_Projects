

list_number = []
list_even = []
list_odd = []
print("Enter the numbers")

for i in range(0,5):
    data = int(input())
    list_number.append(data)
print(list_number)    

for i in list_number:
    if i % 2 == 0:
        list_even.append(i)
    else:
        list_odd.append(i)

print(list_even)
print(list_odd)
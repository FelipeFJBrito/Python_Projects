#Make a Program that reads 4 grades, shows the grades and the average on the screen.

import statistics


grades_list= []
print("Enter the grades")

for i in range(0,4):
    data = float(input())
    grades_list.append(data)
print(grades_list)


#First method
total_grades = 0
for i in grades_list:
    total_grades  = total_grades  + i

print(total_grades )
media = total_grades  / len(grades_list)
print(f"Media with the first method: {media}")

#Second method with median() function
media2 = statistics.median(grades_list)
print(f"Media with the Second method: {media2}")

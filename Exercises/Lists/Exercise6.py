#Make a program that asks for the four grades of 3 students, calculate and store the average of each student in a vector, print the number of students with an average greater than or equal to 7.0.

student1 = []
student2 = []
student3 = []
students_average = []


students = [student1, student2, student3]

print("Enter the grades of the student one")
for x in range(0, 4):
    grade_student1 = float(input())
    student1.append(grade_student1)   
sum_student1 = sum(student1)
average_student1 = round(sum_student1 / len(student1))
student1.clear()
student1.append(average_student1)

print("Enter the grades of the student two")
for x in range(0, 4):
    grade_student2 = float(input())
    student2.append(grade_student2)   
sum_student2 = sum(student2)
average_student2 = round(sum_student2 / len(student2))
student2.clear()
student2.append(average_student2)

print("Enter the grades of the student three")
for x in range(0, 4):
    grade_student3 = float(input())
    student3.append(grade_student3)   
sum_student3 = sum(student3)
average_student3 = round(sum_student3 / len(student3))
student3.clear()
student3.append(average_student3)


for i in range(0,1):
    for i in student1:
        if i >= 7:
            students_average.append(i) 
    for i in student2:
        if i >= 7:
            students_average.append(i)
    for i in student3:
        if i >= 7:
            students_average.append(i) 

print(f"These are the average grades of the students who passed: {students_average}")
student_score = {
    "Harry" : 81,
    "Ron"   : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}


student_grades = {}

for student in student_grades:
    score = student_grades[student]
    if score > 90:
        student_grades[student] = "Outstending"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 80:
        student_grades[student] = "Acceptable" 
    else:
        student_grades[student] = "Fail"       
print(student_score)
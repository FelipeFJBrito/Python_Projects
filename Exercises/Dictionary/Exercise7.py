#Write a Python script to merge two Python dictionaries.

dictionary1={
    1:10, 2:20
    }
dictionary2={
    3:30, 4:40
    }
dictionary3 = dictionary1.copy()
dictionary3.update(dictionary2)
print(dictionary3)
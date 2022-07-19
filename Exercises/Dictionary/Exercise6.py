#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.

def script(n):
    key = 1
    value = 0
    dictionary = {
        key: value,
    }
    for x in range(1,n+1):
        key = x 
        value = key*key
        dictionary[key] = value  
    print(dictionary)    

script(n = 15)
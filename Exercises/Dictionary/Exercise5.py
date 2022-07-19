#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
key = 0 
value =0

dictionary = {
    key: value,
}

n = int(input("Enter a number: "))

for x in range(1,n+1):
    key = x 
    value = key*key
    dictionary[key] = value  
    print(dictionary)

#Given an array of ones and zeroes, convert the equivalent binary value to an integer.
#Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.



def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)








#------------------------------------------------------------------------ JOIN() --------------------------------------------------------------------------

#join() is an inbuilt string function in Python used to join elements of the sequence separated by a string separator. 
# This function joins elements of a sequence and makes it a string.

list1 = ['1','2','3','4']
 
s = "-"
# joins elements of list1 by '-'
# and stores in string s
s = s.join(list1)
 
# join use to join a list of
# strings to a separator s
print(s)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------ MAP() --------------------------------------------------------------------------

#The map function will apply a function to each item in a list of items, that is, 
# it is a for with a function call to apply it to each item in your list.

#The map function return a MAP object so you have to put it insid a list

# list(map(function, List)) =>  list(map(str, arr))         or if it is a string             " ".join(map(function, List)) =>  " ".join(map(str, arr))

arr = [1200, 1000, 1443, 1433]

def add_tax(arr):
    return arr * 1.1

price_tax = []
price_tax = list(map(add_tax , arr))
print(price_tax)
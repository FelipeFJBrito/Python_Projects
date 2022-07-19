#Write a Python script to concatenate following dictionaries to create a new one.
dictionary1={
    1:10, 2:20
    }
dictionary2={
    3:30, 4:40
    }
dictionary3={
    5:50,6:60
    }
dictionary4 = {

}
for d in (dictionary1, dictionary2, dictionary3): 
    dictionary4.update(d)
print(dictionary4)
print("Welcome to tip calculator!")
bill =  float(input("what was the total bill? $"))
tip =  int(input("what percentage tip would you like to give? 10, 12, 15? "))
split =  int(input("How many people to split the bill? "))

bill_Tip  = bill + (bill * (tip/100))
total_value = bill_Tip / split
total_value = round(total_value,2)
total_value = "{:.2f}".format(total_value)
print(f"Each person should pay: ${total_value}")
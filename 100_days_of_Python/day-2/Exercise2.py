#Underweight: BMI < 18.5
#Normal weight: BMI 18.5-25
#Overweight: BMI 25-30
#Obese: BMI > 30


from http.client import SWITCHING_PROTOCOLS


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


new_height = float(height)
new_weight = float(weight)

result = int(new_weight / (new_height **2))

print(result)

if result < 18.5:
    print("You are underweight")
elif result >= 18.5 and result <= 25:
    print("You are normal weight")
elif result > 25 and result <= 30:
    print("You are overweight")
else:
    print("you are obese")        
    
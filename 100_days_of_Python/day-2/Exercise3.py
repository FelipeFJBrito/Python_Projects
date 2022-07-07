age = input("What is your current age?")

new_age  = int(age)
max_years = 90 - new_age
max_days = max_years * 365
max_month = max_years * 12
max_weeks = max_years * 52

print(f"You have {max_days} days, {max_weeks} weeks, and {max_month} months left.")
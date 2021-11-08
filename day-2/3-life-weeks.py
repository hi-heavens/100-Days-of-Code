# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_to_find = 90 - int(age)

remaining_months = age_to_find * 12
remaining_weeks = age_to_find * 52
remaining_days = age_to_find * 365

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")

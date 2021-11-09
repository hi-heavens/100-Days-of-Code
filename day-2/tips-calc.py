#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

tips = (tip_percent / 100) * total_bill
bill_plus_tips = total_bill + tips

to_share = int(input("How many people to split the bill? "))

each_person = round(bill_plus_tips / to_share, 2)
final_amount = "{:.2f}".format(each_person)

print(f"Each person should pay: ${final_amount}")

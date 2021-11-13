# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
# names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

num_of_names = len(names) - 1
random_num = random.randint(0, num_of_names)

random_name = names[random_num]

print(f"{random_name} is going to buy the meal today!")


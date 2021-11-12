# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined = (name1 + name2).lower()

T = combined.count('t')
R = combined.count('r')
U = combined.count('u')
E = combined.count('e')
true = str(T + R + U + E)

L = combined.count('l')
O = combined.count('o')
V = combined.count('v')
E = combined.count('e')
love = str(L + O + V + E)

love_score = int(true + love)

if love_score < 10 or love_score > 90:
        print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
        print(f"Your score is {love_score}, you are alright together.")
else:
        print(f"Your score is {love_score}.")

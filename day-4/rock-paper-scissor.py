import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Papaer or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
        print("You entered an invalid number, you lose!")
else:
        game_list = [rock, paper, scissors]
        print(game_list[user_choice])

        computer_choice = random.randint(0, len(game_list) - 1)

        print("Computer chose:")
        print(game_list[computer_choice])

        if game_list[user_choice] == game_list[computer_choice]:
                print("It's a draw")
        elif computer_choice == 0 and user_choice == 2:
                print("You lose")
        elif computer_choice == 1 and user_choice == 0:
                print("You lose")
        elif computer_choice == 2 and user_choice == 1:
                print("You lose")
        else:
                print("You win!")

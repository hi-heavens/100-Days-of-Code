from random import choice
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = choice(word_list)

print(logo)

# print(f'Pssst, the solution is {chosen_word}.')

lives = 6
display = []
for letter in chosen_word:
  display.append("_")

check = True
while check:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print("You have already quessed {:s}".format(guess))
    continue

  for position in range(0, len(chosen_word)):
      letter = chosen_word[position]

      if letter == guess:
          display[position] = letter
  
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life")
    lives -= 1
    if lives == 0:
      check = False
      print("You lose.")
    
  print(display)

  if "_" not in display:
    check = False
    print("{}".format("You win."))
  print(stages[lives])

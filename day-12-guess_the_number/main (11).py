#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
print(logo)
correct_answer = random.randint(1, 100)

print(f"""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Pssst, the correct answer is {correct_answer}
""")
difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficult == "hard":
  print("You have 5 attempts remaining to guess the number.")
  attempts = 5
elif difficult == "easy":
  print("You have 10 attempts remaining to guess the number.")
  attempts = 10
else:
  attempts = 5

def user_guess (user_attempts):
  is_end_game = False  
  while is_end_game == False and user_attempts > 0:
    guess = int(input("Make a guess: "))
    if guess < correct_answer:
      print("Too low.")
      user_attempts -= 1
    elif guess > correct_answer:
      print("Too high.")
      user_attempts -= 1
    else:
      print(f"You got it! The answer was {correct_answer}.")
      is_end_game = True
      return is_end_game
    if user_attempts <= 0:
      print("You've run out of guesses, you lose.")
    else:
      print(f"Guess again.\nYou have {user_attempts} attempts remaining to guess the number.")
      
user_guess(attempts)
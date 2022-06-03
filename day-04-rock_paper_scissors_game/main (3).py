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

#Write your code below this line 👇
import random
choice = [rock, paper, scissors]

person_chose_index = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if person_chose_index >= 3 or person_chose_index < 0:
  print("\n")
else:
  person_chose = choice[person_chose_index]
  print(person_chose)

print("Computer chose:\n")
computer_chose_index = random.randint(0,2)
computer_chose = choice[computer_chose_index]
print(computer_chose)

row1 = ["It's a Draw", "You win", "You lose"]
row2 = ["You lose", "It's a Draw", "You win"]
row3 = ["You win", "You lose", "It's a Draw"]
map = [row1, row2, row3]

if person_chose_index < 3 and person_chose_index > 0:
  print(map[computer_chose_index][person_chose_index])
else:
  print("You type an invalid number, you lose!")

# if person_chose_index == 0 and computer_chose_index == 1:
#   print("You lose")
# elif person_chose_index == 0 and computer_chose_index == 2:
#   print("You win")
# elif person_chose_index == 1 and computer_chose_index == 0:
#   print("You win")
# elif person_chose_index == 1 and computer_chose_index == 2:
#   print("You lose")
# elif person_chose_index == 2 and computer_chose_index == 0:
#   print("You lose")
# elif person_chose_index == 2 and computer_chose_index == 1:
#   print("You win")
# else:
#   print("It's a draw")
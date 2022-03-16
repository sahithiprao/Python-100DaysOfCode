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

#Write your code below this line 👇
game_image = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  print(game_image[user_choice]) # index range error hence this line move here 
# if (user_choice == 0):
#   print(rock)
# elif (user_choice == 1):
#   print(paper)
# else:
#   print(scissors)
  
computer_choice = random.randint(0,2)
print("Computer chose: ")
print(game_image[computer_choice])
# if (computer_choice == 0):
#   print("Computer chose:\n", rock)
# elif (computer_choice == 1):
#   print("Computer chose:\n",paper)
# else:
#   print("Computer chose:\n", scissors)

# if(user_choice == computer_choice):
#   print("Tie")
# elif (user_choice == 0):
#   if(computer_choice == 2):
#     print("You win")
#   else:
#     print("You lose")
# elif (user_choice == 1):
#   if (computer_choice == 0):
#     print("You win")
#   else:
#     print("You lose")
# elif (user_choice == 2):
#   if (computer_choice == 1):
#     print("You win")
#   else:
#     print("You lose")

if user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

  

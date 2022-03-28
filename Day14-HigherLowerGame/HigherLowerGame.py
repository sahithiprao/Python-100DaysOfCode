# 1) import data and logo
# 2) randomly choose the compare A and B values
# 3) compare A and B 
#4) input - guess the followers highest- A/ B
# 5) if guess > other A/B then game continues else game ends with score display
#6) once guess is correct then, guess becomes A and choose B repeat 
import random
from replit import clear
from art import logo,vs
from game_data import data

def compare_values(guess, first_fcount, second_fcount):
  if first_fcount > second_fcount:
    return guess == "a"
  else:
    return guess == "b"

should_continue = True
score = 0
second_choice = random.choice(data)

while should_continue:

  first_choice = second_choice
  first_fcount = first_choice['follower_count']

  second_choice = random.choice(data)
  second_fcount = second_choice['follower_count']

  while first_choice == second_choice:
    second_choice = random.choice(data)
    
  print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}.")
  print(vs)
  print(f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}.")
  
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  compare_value = compare_values(guess, first_fcount, second_fcount)
  
  clear()
  print(logo)
  if compare_value:
    score += 1
    print(f"You're right! Current Score: {score}")
  else:
    should_continue = False
    print(f"You're wrong! Final Score: {score}")
  


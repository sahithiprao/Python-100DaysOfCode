from art import logo
import random


EASY_ATTEMPT = 10
HARD_ATTEMPT = 5


def check_difficulty():
  level_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level_choice == 'easy':
    return EASY_ATTEMPT
  else:
    return HARD_ATTEMPT


def number_check(guess, answer, turns):
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it. The answer is {answer}")

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.") 
  answer = random.randint(1, 100)

  turns = check_difficulty()


  guess = 0
  while guess != answer:
    print(f" You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = number_check(guess, answer, turns)

    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()
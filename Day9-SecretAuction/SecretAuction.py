from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction program")
bid_dict = {}
should_continue = True

def get_max_bid(bid_dict):
  highest_bid = 0
  winner =""
  for bidder in bid_dict:
    bid_amt = bid_dict[bidder]
    if bid_amt > highest_bid:
      highest_bid = bid_amt
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while should_continue:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  
  bid_dict[name] = bid

  repeat = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if repeat == "no":
    should_continue = False
    get_max_bid(bid_dict)
  elif repeat == "yes":
    clear()
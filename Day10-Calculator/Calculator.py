from art import logo

print(logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def calculator():
  n1 = float(input("What's the first number?: "))
  
  for ops in operations:
    print(ops)
  
  should_continue = True
  
  while should_continue:
    symbol = input("Pick an operation: ")
    n2 = float(input("What's the next number?: "))
    calculation_function = operations[symbol]
    answer = calculation_function(n1, n2)
    
    print(f"{n1} {symbol} {n2} = {answer}")
    
    repeat = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation.: ")
    
    if repeat == "y":
      n1 = answer
    else: 
      should_continue = False
      calculator()#recursive function

calculator()  
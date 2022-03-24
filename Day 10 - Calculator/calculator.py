from art import logo

# Calculator

# Addition
def add(n1, n2):
  return n1 + n2

# Substraction
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

# Dictionary 
operations = {"+": add, 
              "-": subtract, 
              "*": multiply, 
              "/": divide,
             }

def calculator():
  print(logo)
  n1 = float(input("What's the first number?: "))
  for operation in operations:
    print(operation)

  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation: ")
    n2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(n1, n2)
    print(f"{n1} {operation_symbol} {n2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == 'y':
      n1 = answer
    else:
      should_continue = False
      calculator()

calculator()

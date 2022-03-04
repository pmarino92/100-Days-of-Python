# Create a for loop in range from 1 - 100
# If a number is divisible by 3 and 5 replace that number with "Fizzbuzz"
# If a number is divisible by 3  replace that number with "Fizz"
# If a number is divisible by  5 replace that number with "Buzz"

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
    continue
  elif number % 3 == 0:
    print("Fizz")
    continue
  elif number % 5 == 0:
    print("Buzz")
    continue
  else:
    print(number)
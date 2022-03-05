import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create an empty string variable
password = ""

# Use for loops to iterate through our lists and add to our empty password string
# Use random.choice to select random characters throughout the list

# Letters
for i in range(0, nr_letters):
    password += random.choice(letters)

# Symbols
for i in range(0, nr_symbols):
    password += random.choice(symbols)

# Numbers
for i in range(0, nr_numbers):
    password += random.choice(numbers)

# Shuffle the password
# Make our string into a list
shuffled = list(password)

# Now we are able to shuffle the order
random.shuffle(shuffled)

# Turn our shuffled list back into a string
result = ''.join(shuffled)


print(f"Your password is: {result}")
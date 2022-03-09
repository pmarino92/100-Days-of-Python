# Step 2
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display
display = []

guess = input("Guess a letter: ").lower()

# Loop through each position in the chosen_word
# For each letter in the chosen_word, add a "_" to 'display'.
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.

for letter in chosen_word:
    if letter == guess:
        display.append(letter)
    else:
        display.append('_')
print(display)
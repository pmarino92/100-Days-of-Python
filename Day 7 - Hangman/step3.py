import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display
display = []

for _ in range(word_length):
    display += "_"

wordGuessed = False

while wordGuessed is False:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    print(display)

    if '_' not in display:
        print("Great job! You won!")
        wordGuessed = True




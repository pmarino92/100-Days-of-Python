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

choice = int(input("Rock, Paper, Scissors! Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
RPS =[rock, paper, scissors]
computer_choice = random.choice(tuple(RPS))

# Computer wins scenarios
if choice == 0 and computer_choice == paper:
  print(rock)
  print("Computer chose:")
  print(computer_choice)
  print("Computer wins")
elif choice == 1 and computer_choice == scissors:
  print(paper)
  print("Computer chose:")
  print(computer_choice)
  print("Computer wins")
elif choice == 2 and computer_choice == rock:
  print(scissors)
  print("Computer chose:")
  print(computer_choice)
  print("Computer wins")

#User wins scenarios
elif choice == 0 and computer_choice == scissors:
  print(rock)
  print("Computer chose:")
  print(computer_choice)
  print("You win!")
elif choice == 1 and computer_choice == rock:
  print(paper)
  print("Computer chose:")
  print(computer_choice)
  print("You win!")
elif choice == 2 and computer_choice == paper:
  print(scissors)
  print("Computer chose:")
  print(computer_choice)
  print("You win!")

# Draw Scenarios
elif choice == 0 and computer_choice == rock:
  print(rock)
  print("Computer chose:")
  print(computer_choice)
  print("DRAW")
elif choice == 1 and computer_choice == paper:
  print(paper)
  print("Computer chose:")
  print(computer_choice)
  print("DRAW")
elif choice == 2 and computer_choice == scissors:
  print(scissors)
  print("Computer chose:")
  print(computer_choice)
  print("DRAW")
else:
  print("Select 0, 1, or 2.")
  print("Click run at the top to restart.")

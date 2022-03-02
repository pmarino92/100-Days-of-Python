print("Welcome to Father.")
print("A catastrophic event has just occurred and you must survive.") 

print("You must get out of the city as quickly as you can")
first_move = input("Do you go right or left outside of your crumbling house?")

if first_move == "left":
  print("You happen across a father and his son who has broken his leg from some debris. ")
else:
  print("Your house collapses on top of you suddenly killing you instantly. Game Over.")


second_move = input("Do you decide to help the two? Enter Y or N: ")

if second_move == "Y":
  print("It was a trap! The father pulls a gun out and shoots you killing you instantly. Game Over")
else:
  print("You continue on from the pair feeling guilty and ashamed. However, you're alive.")
  
print("The hair on the back of your neck stands up as you feel as though you are being watched.")
print("You look behind and find a familiar father figure lurking behind from a distance")
print("You notice some abandoned cars in front of you. ")
final_move = input("Do you choose the red, yellow, or blue car?")

if final_move == "red":
  print("You can't enter the car as the door is jammed! The father closes in and snaps your neck. Game Over")
elif final_move == "yellow":
  print("The yellow car's door is open, but as you enter you notice there are no keys. The figure rips you out of the car and strangles you to death. Game Over.")
else:
  print("You frantically enter the blue car to luckily find the keys still in the ignition. You quickly turn the key and race off with the figure in your rearview mirror.")
  print("While you may not know what lies ahead, you follow your intution in hopes of escaping this nightmare of a reality you find yourself.")

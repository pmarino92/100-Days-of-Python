print("Welcome to the tip calculator!")
#Create a variable that contains user input on the total bill
#Convert the input into a float
bill = float(input("What was the total bill? $"))

#Create a variable that contains how much user wants to tip
#Convert to an int
tip = int(input("How much would you like to give? 10, 12, or 15?"))

#Create a variable that contains how many people are splitting the bill
people = int(input("How many to split the bill?"))

#First, calculate the tip as a percentage by dividing by 100
tip_as_percent = tip / 100

#Next, calculate the dollar amount of the tip by multiplying bill by percantage tip
total_tip_amount = bill * tip_as_percent

#Add the bill and total tip amount to get the total bill
total_bill = bill + total_tip_amount

#Calculate the bill per person by dividing the total bill amount by how many people are splitting
bill_per = total_bill / people

#Finally round the bill per person to two decimal places
final = round(bill_per, 2)
print(f"Each person should pay: ${final}")
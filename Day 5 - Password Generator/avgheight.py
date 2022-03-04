student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# CANT USE SUM OR LEN FUNCTIONS
# Create two variables to store the sum of the heights and a variable for how amount of heights
sum = 0
count = 0

# Loops through and for each height inputed adds one to calculate the total number
# Loops through and adds each height to the next storing inside our sum variable
for height in student_heights:
  count += 1
  sum += height

# Simple calculation to divide sum by count and rounding to the nearest whole number
avg = round(sum / count)
print(avg)
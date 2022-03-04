student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# CANT USE MAX FUNCTION
# Create a variable called max to hold student score in our list
max = student_scores[0]

# Loop through the list and if an individual score is greater than the last it becomes our new variable "max"
for scores in student_scores:
    if scores > max:
        max = scores

print(max)
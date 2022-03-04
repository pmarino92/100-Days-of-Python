
#Adds up only the even numbers from 1 to 100
even_total = 0
for even in range(1, 101):
  if even % 2 == 0:
    even_total += even
  
print(even_total)
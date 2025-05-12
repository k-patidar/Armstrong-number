'''with the help of sum

numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print("Sum of list elements:", total)'''

''' with the help of loop 
 numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Sum of list elements:", total) 
'''
'''with the help of factor 
from functools import reduce

numbers = [10, 20, 30, 40, 50]
total = reduce(lambda x, y: x + y, numbers)

print("Sum of list elements:", total)'''

# Get user input as a space-separated string of numbers
numbers = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of integers
num_list = list(map(int, numbers.split()))

# Calculate the sum of the list
total = sum(num_list)

# Display the result
print("Sum of the numbers:", total)


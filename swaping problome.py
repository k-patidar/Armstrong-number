# Get user input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swapping without using a third variable
a = a + b
b = a - b
a = a - b

# Display the swapped values
print("After swapping:")
print("First number:", a)
print("Second number:", b)

# Function to check if a number is an Armstrong number
def is_armstrong(num):
    # Convert number to string to get the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if sum is equal to the original number
    return sum_of_powers == num

# Input from user
num = int(input("Enter a number: "))

# Check and display result
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

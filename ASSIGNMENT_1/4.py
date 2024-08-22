# Get two numbers from the user
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'

# Check and print the result for both numbers
print(f'The first number ({num1}) is {check_even_odd(num1)}.')
print(f'The second number ({num2}) is {check_even_odd(num2)}.')

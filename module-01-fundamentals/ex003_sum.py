# Receive the first number from the user and convert it from string to integer
num1 = int(input('Enter the first number: '))

# Receive the second number from the user and convert it to integer
num2 = int(input('Enter the second number: '))

# Calculate the sum of the two numbers
sum_result = num1 + num2

# Display the result using modern string formatting (.format method)
print('The sum of {} and {} is: {}'.format(num1, num2, sum_result))
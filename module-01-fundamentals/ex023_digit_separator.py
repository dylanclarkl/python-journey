# Exercise 23: Make a program that reads a number from 0 to 9999 and displays each of its digits separately on the screen.

# Read an integer number from the user
number = int(input('Enter a number: '))

# Extract each digit mathematically using division and module operations
unit = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000 % 10

# Display the analysis results
print('Analyzing the number {}'.format(number))
print('Unit: {}'.format(unit))
print('Ten: {}'.format(ten))
print('Hundred: {}'.format(hundred))
print('Thousand: {}'.format(thousand))

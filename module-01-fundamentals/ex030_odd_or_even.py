# Exercise 30: Create a program that reads an integer number and displays on the screen whether it is EVEN or ODD.

# Read an integer number from the user
number = int(input('Enter a number: '))

# Check if the remainder of division by 2 is 0 (even) or not (odd)
if number % 2 == 0:
    print('The number {} is EVEN'.format(number))
else:
    print('The number {} is ODD'.format(number))

# Create a program that reads any real number from the keyboard and displays its integer portion on the screen.

from math import trunc

# Method 1: Using the trunc function from the math module
number = float(input('Type a real number: '))
print('The typed value was {} and its integer portion is {}'.format(number, trunc(number)))

# Method 2: Using the int type casting
number1 = float(input('Type a real number: '))
print('The typed value was {} and its integer portion is {}'.format(number1, int(number1)))

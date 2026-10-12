# Exercise 33: Make a program that reads three numbers and shows which one is the largest and which one is the smallest.

# Read three numbers from the user
number1 = int(input('First value: '))
number2 = int(input('Second value: '))
number3 = int(input('Thrid value: '))

# Assume number1 is the smallest, then check against the others
smallest = number1
if number2 < number1 and number2 < number3:
    smallest = number2
if number3 < number1 and number3 < number2:
    smallest = number3
print('The smallest value entered was {}'.format(smallest))

# Assume number1 is the largest, the check against the others
largest = number1
if number2 > number1 and number2 > number3:
    largest = number2
if number3 > number1 and number3 > number2:
    largest = number3
print('The largest value entered was {}'.format(largest))

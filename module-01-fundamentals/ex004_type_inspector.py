# Receive any value from the user via keyboard input
a = input('Type something: ')

# Display the primitive type of value
# Note: Every input() function returns a string by default in Python
print('The type of the value you entered is:', type(a))

# Check string characteristics using native Python methods
print('Is it just spaces? {}'.format(a.isspace()))
print('Is it a number? {}'.format(a.isnumeric()))
print('Is it alphabetic? {}'.format(a.isalpha()))
print('Is it alphanumeric? {}'.format(a.isalnum()))
print('Is it uppercase? {}'.format(a.isupper()))
print('Is it lowercase? {}'.format(a.islower()))
print('Is it capitalized? {}'.format(a.istitle()))
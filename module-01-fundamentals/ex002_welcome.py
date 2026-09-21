# Request the user's name via keyboard input
name = input('Enter your name: ')

# Old Python 2 output format style (legacy)
# print('Welcome,', name, '!')

# Modern output formatting style used by Python 3, employing the .format() method
# The curly braces {} are replaced by the value stored in the variable

print('Welcome, {}!'.format(name))

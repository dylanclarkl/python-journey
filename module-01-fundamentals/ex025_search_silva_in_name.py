# Exercise 25: Create a program that reads a person's name and tells whether or not they have 'Silva1' in their name.

# Read the full name from the user and remove unwanted outer spaces
full_name = str(input('What is your full name? ')).strip()

# Check if the string 'SILVA' exists within the uppercase version of the full name
print('Does your name have Silva? {}'.format('SILVA' in full_name.upper()))

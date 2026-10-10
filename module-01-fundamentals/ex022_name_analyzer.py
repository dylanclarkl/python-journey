# Exercise 22: Create a program that reads a person's full name and displays:
# - The name with all uppercase and lowercase letters
# - How many letters in total (excluding spaces)
# - How many letters the first name has

# Read the full name from user and remove unwanted outer spaces
full_name = str(input('Enter your full name: ')).strip()

print('Analyzing your name...')

# Display the name in all uppercase letters
print('Your name in uppercase is {}'.format(full_name.upper()))

# Display the name in all lowercase letters
print('Your name in lowercase is {}'.format(full_name.lower()))

# Calculate total letters by subtracting total spaces from total string length
print('Your name has a total of {} letters'.format(len(full_name) - full_name.count(' ')))

# Split the full name into a list of words ( first name, last name, etc.)
name_parts = full_name.split()

# Display the first name and count its letters
print('Your first name is {} and it has {} letters'.format(name_parts[0], len(name_parts[0])))
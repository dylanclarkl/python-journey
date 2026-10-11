# Exercise 27: Make a program that reads a person's full name, the displays the first and last name separately.

# Read the full name from the user and remove unwanted outer spaces
full_name = str(input('Enter your full name: ')).strip()

# Split the full name into a list of words/parts
name_parts = full_name.split()

# Display greeting and the separated names
print('Nice to meet you!')
print('Your first name is {}'.format(name_parts[0]))
print('Your last name is {}'.format(name_parts[len(name_parts) - 1]))

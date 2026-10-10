# Exercise 24: Create a program that reads the name of city and tells whether or not it starts with the name 'Santo'

# Read the city name from user and remove unwanted outer spaces
city = str(input('What city were you born in? ')).strip()

# Slice the first 5 characters, convert them to uppercase, and check if they equal 'SANTO'
print(city[:5].upper() == 'SANTO')

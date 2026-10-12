# Exercise 32: Make a program that reads any year and shows whether or not it is a leap year.

from datetime import date

# Read the year from user; use 0 to analyze the current year
year = int(input('What year do you want to analyze? Put 0 for the current year: '))

if year == 0:
    year = date.today().year

# Check the leap year mathematical conditions (divisible by 4 and not 100, or divisible by 400)
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('The year {} is a LEAP YEAR'.format(year))
else:
    print('The year {} is NOT a LEAP YEAR'.format(year))

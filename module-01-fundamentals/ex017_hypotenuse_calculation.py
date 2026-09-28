# Make a program that reads the length of the opposite and adjacent legs of a right triangle. Calculate and show the length of the hypotenuse.

# Approach 1: Calculating the hypotenuse using mathematical formula (Pythagorean theorem)
opposite = float(input('Length of the opposite leg: '))
adjacent = float(input('Length of the adjacent leg: '))
hypotenuse = (opposite ** 2 + adjacent ** 2) ** (1/2)
print('The hypotenuse will measure {:.2f}'.format(hypotenuse))

# Approach 2: Calculating the hypotenuse using the hypot fuction from the math module
from math import hypot

opposite_leg = float(input('Length of the opposite leg: '))
adjacent_leg = float(input('Length of the adjacent leg: '))
hypotenuse_lenght = hypot(opposite_leg, adjacent_leg)
print('The hypotenuse will measure {:.2f}'.format(hypotenuse_lenght))

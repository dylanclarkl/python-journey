# Make a program that reads any angle and displays the value of its sine, cosine, and tangent on the screen.

from math import radians, sin, cos, tan

# Read the angle from the user
angle = float(input('Enter the angle you want: '))

# Calculate and display the sine
sine = sin(radians(angle))
print('The angle of {} has a SINE of {:.2f}'.format(angle, sine))

# Calculate and display the cosine
cosine = cos(radians(angle))
print('The angle of {} has a COSINE of {:.2f}'.format(angle, cosine))

# Calculate and display the tangent
tangent = tan(radians(angle))
print('The angle of {} has a TANGENT of {:.2f}'. format(angle, tangent))

# Receive the wall width and height from the keyboard and covert them to float
width = float(input('Wall width: '))
height = float(input('Wall height: '))

# Calculate the total area of wall
area = width * height
print('Your wall has dimensions of {} x {} and its area is {}m².'.format(width, height, area))

# Calculate the amount of paint needed (knowing that 1 liter paints 2 square meters)
paint = area / 2
print('To paint this wall, you will need {}l of paint.'.format(paint))

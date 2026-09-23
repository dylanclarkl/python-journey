# Receive an integer number from the keyboard to generate its multiplication table from 1 to 10
num = int(input('Type a number to see its multiplication table: '))

# Print a decorative separator line
print('_' * 12)

# Calculate and display the multiplication table from 1 to 10
# Note: {:2} is used to align numbers properly on the screen
print('{} x {:2} = {}'.format(num, 1, num * 1))
print('{} x {:2} = {}'.format(num, 2, num * 2))
print('{} x {:2} = {}'.format(num, 3, num * 3))
print('{} x {:2} = {}'.format(num, 4, num * 4))
print('{} x {:2} = {}'.format(num, 5, num * 5))
print('{} x {:2} = {}'.format(num, 6, num * 6))
print('{} x {:2} = {}'.format(num, 7, num * 7))
print('{} x {:2} = {}'.format(num, 8, num * 8))
print('{} x {:2} = {}'.format(num, 9, num * 9))
print('{} x {:2} = {}'.format(num, 10, num * 10))

# Print a decorative closing line
print('_' * 12)
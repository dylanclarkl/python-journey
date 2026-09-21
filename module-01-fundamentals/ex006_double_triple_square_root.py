# Receive an integer number from the user via keyboard input
num = int(input('Type a number: '))

# Calculate and display the double, triple, and square root of the number
print('The double of {} is {}, \n the triple of {} is {} \n the square root of {} is {:.2f}'.format(num, (num*2), num, (num*3), num, (num**(1/2))))

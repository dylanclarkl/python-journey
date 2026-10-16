# Exercise 37: Write a Python program that reads any integer number 
# and asks the user to choose the conversion base: 
# 1 for binary, 2 for octal, and 3 for hexadecimal.

# Read an integer number from the user
number = int(input("Enter an integer number: "))

print(
    """Choose one of the bases for conversion:
[ 1 ] Convert to BINARY
[ 2 ] Convert to OCTAL
[ 3 ] Convert to HEXADECIMAL"""
)

# Read the user's conversion option
option = int(input("Your option: "))

# Perform the corresponding number base conversion using built-in Python functions
if option == 1:
    print("{} converted to BINARY is equal to {}".format(number, bin(number)[2:]))
elif option == 2:
    print("{} converted to OCTAL is equal to {}".format(number, oct(number)[2:]))
elif option == 3:
    print("{} converted to HEXADECIMAL is equal to {}".format(number, hex(number)[2:]))
else:
    print("Invalid option, please try again")
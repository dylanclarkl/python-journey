# Exercise 38: Write a program that reads two integer numbers and compares them,
# showing a message on the screen:
# – The first value is greater
# – The second value is greater
# – There is no greater value, both are equal

# Read two integer numbers from the user
number1 = int(input("First number: "))
number2 = int(input("Second number: "))

# Compare the numbers and display the appropriate message
if number1 > number2:
    print("The FIRST value is GREATER")
elif number2 > number1:
    print("The SECOND value is GREATER")
else:
    print("Both values are EQUAL")
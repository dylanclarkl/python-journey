# Exercise 29: Write a program that reads the speed of a car. If it exceeds 80 km/h, show a message saying that the driver has been fined. The fine will cost $7.00 for each km above the limit.

# Read the car's speed from the user
speed = float(input("What is the car's speed? "))

# Check if the speed exceeds the 80 km/h limit
if speed > 80:
    fine = (speed - 80) * 7
    print('FINED: You exceeded the permitted speed limit of 80 km/h')
    print('You have been fined ${:.2f}'.format(fine))

print('Have a nice day! Drive safely!')
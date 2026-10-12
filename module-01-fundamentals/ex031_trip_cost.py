# Exercise 31: Develop a program that asks for distance of a trip in km. Calculate the ticket price, charging $0.50 por km for trips up to 200 km and $0.45 for longer trips.

# Read the trip distance from the user
distance = float(input('What is the distance of your trip? '))

print('You are about to begin a trip of {:.1f} km'.format(distance))

# Calculate the price using a conditional expression (simplified condition)
price = distance * 0.50 if distance <= 200 else distance * 0.45

# Display the final ticket price
print('And the price of your ticket will be ${:.2f}'.format(price))

# Receive the number of days the car was rented from the keyboard and convert it to int
days = int(input('How many days was the car rented? '))

# Receive the number of kilometers driven from the keyboard and convert it to float
km = float(input('How many kilometes driven? '))

# Calculate the total price to pay (charging 60 per day and 0.15 per km driven)
total_payment = (days * 60) + (km * 0.15)

# Display the total amount to pay formatted with 2 decimal places
print('The total amount to pay is ${:.2f}'.format(total_payment))
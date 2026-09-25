# Receive the temperature in Celsius from the keyboard and convert it to float
celsius = float(input('Enter the temperature in °C: '))

# Convert Celsius to Fahrenheit
fahrenheit = celsius * 9 / 5 + 32

# Display the converted temperature
print('The temperature of {}°C corresponds to {}°F'.format(celsius, fahrenheit))
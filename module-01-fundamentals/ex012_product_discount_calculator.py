# Receive the product price from the keyboard and convert it to float
price = float(input('What is the product price? $'))

# Calculate the new price with a 5% discount
new_price = price - (price * 5 / 100)

# Display the original price and the new discounted price formatted with 2 decimal places
print('The product that cost ${:.2f}, on sale with a 5% discount will cost ${:.2f}'.format(price, new_price))
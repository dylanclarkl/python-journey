# Receive the amount of money in Brazilian Reais (BRL) from the keyboard and convert it to float
amount_brl = float(input('How much money do you have in your wallet? R$: '))

# Calculate how many US Dollars (USD) can be bought on a conversion rate and display it formatted
# Note: Conversion rate used it this exercise is fixed (e.g., 1 USD = 5.20 BRL)
print('With this amount of R${:.2f}, you can buy US${:.2f}'.format(amount_brl, amount_brl / 5.20))

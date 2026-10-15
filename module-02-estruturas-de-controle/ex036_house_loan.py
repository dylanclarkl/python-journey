# Exercise 36: Write a program to approve a bank loan for for buying a house. Ask for the house price, the buyer's salary, and how many years they will pay. The monthly installment cannot exceed 30% of the salary, or the loan will be denied.

# Read house value, buyer salary, and loan duration in years from the user
house_price = float(input('What is the house value: $ '))
buyer_salary = float(input("What is the buyer's salary: $ "))
years = int(input('How many years for the mortgage? '))

# Calculate monthly installment and the 30% salary threshold
installment = house_price / (years * 12)
minimum_limit = buyer_salary * 30 / 100

print('To pay for a house worth ${:.2f} in {} years, the installment will be ${:.2f}'.format(house_price, years, installment))

# Check if the monthly installment exceeds 30% of the buyer's salary
if installment <= minimum_limit:
    print('\033[0;32m LOAN APROVED! \033[m))')
else:
    print('\033[0;31m LOAN DENIED! \033[m')
# Receive the employee's salary from the keyboard and convert it to float
salary = float(input("What is the employee's salary? $"))

# Calculate the new salary with a 15% increase
new_salary = salary + (salary * 15 / 100)

# Display the original salary and the new increased salary formatted with 2 decimal places
print('An employee who earned ${:.2f} with a 15% increase, now starts to receive ${:.2f}'.format(salary, new_salary))

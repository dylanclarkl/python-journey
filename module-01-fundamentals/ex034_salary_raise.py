# Exercise 34: Write a program that asks for an  employee's salary and calculates the amount of their raise. For salaries higher than $1250.00, calculate a 10% raise. For lower or equal ones, the raise is 15%.

# Read the employee's salary from the user
salary = float(input("What is the employee's salary? $ "))

# Calculate the new salary based on the salary threshold condition
if salary <= 1250.00:
    new_salary = salary + (salary * 15 / 100)
else:
    new_salary = salary + (salary * 10 / 100)

# Display the result showing the old and new salaries
print('Who was earning ${:.2f} now starts earning ${:.2f}'.format(salary, new_salary))

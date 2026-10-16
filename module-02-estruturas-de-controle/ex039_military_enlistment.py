# Exercise 39: Make a program that reads a young person's birth year 
# and informs, according to their age, whether they still need to enlist 
# in military service, if it is the exact time to enlist, or if the deadline 
# has passed. Your program should also show how much time is left or has passed.

from datetime import date

# Read birth year and gender from the user
birth_year = int(input("Year of birth: "))
gender = str(input("Enter [ M ] for Male or [ F ] for Female: ")).upper()

current_year = date.today().year
age = current_year - birth_year

print("Who was born in {} is {} years old in {}".format(birth_year, age, current_year))

# Check enlistment status based on age and gender requirements
if age == 18 and gender == "M":
    print("You must enlist IMMEDIATELY!")
elif age < 18 and gender == "M":
    balance = 18 - age
    print("You still have {} year(s) left until enlistment".format(balance))
    enlistment_year = current_year + balance
    print("Your enlistment will be in {}".format(enlistment_year))
elif age > 18 and gender == "M":
    balance = age - 18
    print("You should have enlisted {} year(s) ago".format(balance))
    enlistment_year = current_year - balance
    print("Your enlistment was in {}".format(enlistment_year))
else:
    print("Military enlistment is mandatory for Men only")
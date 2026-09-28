# A teacher wants to randomly pick one of their four students to erase the chalkboard.
# Make a program that helps them by reading the studetns' names and displaying the chosen one on the screen.

from random import choice

# Read the names of the four students
student1 = input('Enter the name of the first student: ')
student2 = input('Enter the name of the second student: ')
student3 = input('Enter the name of the third student: ')
student4 = input('Enter the name of the fourth student: ')

# Store the students in a list and pick one randomly
students_list = [student1, student2, student3, student4]
chosen_student = choice(students_list)

# Display the result
print('The chosen student was {}'.format(chosen_student))

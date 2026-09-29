# Exercise 20: A teacher now wants to randomly sort the presentation order
# of their four students. Make a program that reads the names of four students and displays the randomized presentation order.

from random import shuffle

# Read the names of the four students
student1 = input('Enter the name of the first student: ')
student2 = input('Enter the name of the second student: ')
student3 = input('Enter the name of the third student: ')
student4 = input('Enter the name of the fourth student: ')

# Store the students in a list and shuffle their order
students_list = [student1, student2, student3, student4]
shuffle(students_list)

# Display the resulting order
print('The presentation order will be:')
print(students_list)

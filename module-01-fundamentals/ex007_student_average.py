# Receive the student's first grade from the keyboard and convert it to float
grade1 = float(input('First student grade: '))

# Receive the student's second from the keyboard and convert it to float
grade2 = float(input('Second student grade: '))

# Calculate the average and display in formatted to 1 decimal place
print('The average between {} and {} is equal to {:.1f}'.format(grade1, grade2, (grade1 + grade2) / 2))

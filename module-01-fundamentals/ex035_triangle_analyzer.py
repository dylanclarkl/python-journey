# Exercise 35: Develop a program that reads the length of three straight lines and tells user whether or not they can form a triangle.

print('-=-' * 20)
print('Triangle Analyzer')
print('-=-' * 20)

# Read the lengths of the three line segments from the user
segment1 = float(input('First segment: '))
segment2 = float(input('Second segment: '))
segment3 = float(input('Third segment: '))

# Check the triangle inequality theorem (each side must be less than the sum of the other two)
if segment1 < segment2 + segment3 and segment2 < segment1 + segment3 and segment3 < segment1 + segment2:
    print('The segments above CAN FORM a triangle')
else:
    print('The segments CANNOT FORM a triangle')

# Exercise 26: Make a program that reads a sentence from the keyboard and shows how many times the letter 'A' appears, what position it appears the first time, and what position it appears the last time.

# Read the sentence from the user, convert it to uppercase, and remove unwanted outer spaces
sentence = str(input('Enter a sentence: ')).upper().strip()

# Count how many times the letter 'A' appears in the sentence
print('The letter A appears {} times in the sentence.'.format(sentence.count('A')))

# Find the index of the first occurrence of 'A' and add 1 for 1-based positioning
print('The first letter A appeared at position {}.'.format(sentence.find('A') + 1))

# Find the index of the last occurence of 'A' and add 1 for 1-based positioning
print('The last letter A appeared at position {}.'.format(sentence.rfind('A') + 1))

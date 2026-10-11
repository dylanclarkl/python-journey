# Exercise 28: Write a program that makes the computer "think" of an integer between 0 and 5 and asks the user to try to guess which number the computer chose. The program should write on the screen whether the user won or lost.

from random import randint
from time import sleep

# Make the computer "think" of a random number between 0 and 5
computer_number = randint(0, 5)

print('-=-' * 20)
print('I am thinking of a number between 0 and 5. Try to guess...')
print('-=-' * 20)

# Player attempts to guess the number
player_guess = int(input('What number did I think of? '))

print('PROCESSING...')
sleep(3) # Make the computer waint for 3 seconds to build suspense

# Check if the player's guess matches the computer's choice
if player_guess == computer_number:
    print('CONGRATULATIONS! You managed to beat me!')
else:
    print('I WON! I thought of the number {} and not {}.'.format(computer_number, player_guess))
# Exercise 21: Write a Python program that opens and plays the audio from an MP3 file.

import pygame

# Initialize the pygame library
pygame.init()

# Load the MP3 audio file
pygame.mixer.music.load('ex021.mp3')

# Play the audio
pygame.mixer.music.play()

# Prevents the program from closing immediately before the music plays
input("Press Enter to stop the music...")
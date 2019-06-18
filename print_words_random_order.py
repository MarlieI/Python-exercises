# Challenge 1, chapter 5 python for the absolute beginner
# Program that prints a list of words in random order
# It prints all the words and does not repeat any

# Imports
import random

# Constants (tuple)
WORDS = ("Banana", "DVD", "Mobile", "Lipstick", "Spider", "CD", "Dog")

# The list of words that gets printed in random order
# Starts empty
list = []

# All the words have to get printed
# Computer picks a random word
# If the random word is already added to the list
# Then the word is skipped
while len(list) != len(WORDS):
    word = random.choice(WORDS)
    if word not in list:
        list.append(word)

# The list is printed
for i in list:
    print(i)

input("Press the enter key to exit the program.")
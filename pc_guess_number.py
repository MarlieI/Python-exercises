# Guess The Number Game
# Challenge 4, chapter 3 python for the absolute beginner
# The player has to pick a number (between 1 and 100).
# The computer has 10 chances to guess, otherwise the player wins.

import random

print("\t\t\t\t\t\tGuess the right number!")
print("\nChoose a number between 1 and 100.")
print("\nThe computer has 10 chances to get it right.\n")


# Initial value
guess = random.randint(1, 100)
tries = 1
number = int(input("Choose a number between 1 and 100: "))

while guess != number:
    if tries >= 10:
        print("\nThe computer didn't guess the right number in time, you won!")
        break
    elif guess > number:
        print(guess)
    elif guess < number:
        print(guess)
    guess = random.randint(1, 100)
    tries += 1

print(f"\nThe computer last guess was the number {guess} ({tries} tries)!")

input("\nPress enter to exit the program.")

# Guess The Number Game
# Challenge 3, chapter 3 python for the absolute beginner
# The player has to guess the number (between 1 and 30).
# The player has 5 chances to guess, otherwise he gets a chastising message.

import random

print("\t\t\t\t\t\tGuess the right number!")
print("\nChoose a number between 1 and 30.")
print("You have 5 chances to get it right.\n")

# Initial values
number = random.randint(1, 30)
guess = ""
tries = 0

while guess != number:
    guess = int(input("Guess the number: "))
    tries += 1
    if tries > 5:
        print("\nYou didn't guess the right number in time, you loser!")
        break
    elif guess > number:
        print("Lower...")
    elif guess < number:
        print("Higher...")

print(f"\nIt took you {tries} tries.")
print(f"The correct number was: {number}")

input("\nPress enter to exit the program.")

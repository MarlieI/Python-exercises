# This program pairs a random number between 1 and 5 with a fortune cookie.
# The fortune cookie that matches with the chosen number gets displayed to the player.
# Challenge 1, chapter 3 python for the absolute beginner

import random

messages = ["Pay attention to your family. Don't take them for granted.",
            "Your home will be filled with peace and harmony.",
            "Fall for someone who's not your type.",
            "Somebody appreciates the unique you.",
            "If you haven't got it, just fake it!"
            ]

print("Welcome to the 'fortune cookie game'.")
input("\nPress enter to get your fortune cookie of the day.\n")

print(messages[random.randint(0, len(messages)-1)])

input("\nPress enter to exit the program.")

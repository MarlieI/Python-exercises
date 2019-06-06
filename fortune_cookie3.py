# This program pairs a random number between 1 and 5 with a fortune cookie.
# The fortune cookie that matches with the chosen number gets displayed to the player.
# Challenge 1, chapter 3 python for the absolute beginner

import random
number = random.randint(1, 5)

print("Welcome to the 'fortune cookie game'.")
input("\nPress enter to get your fortune cookie of the day.")

if number == 1:
    print("Pay attention to your family. Don't take them for granted.")

elif number == 2:
    print("Your home will be filled with peace and harmony.")

elif number == 3:
    print("Fall for someone who's not your type.")

elif number == 4:
    print("Somebody appreciates the unique you.")

elif number == 5:
    print("If you haven't got it, just fake it!")

else:
    print("Illegal fortune cookie, error.")

input("\nPress enter to exit the program.")
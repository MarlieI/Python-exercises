# Challenge  2, chapter 3 python for the absolute beginner
# A program that flips a coin 100 times and then tells you the number of heads and tails.

import random

print("Welcome, this program will let you flip a coin 100 times.")
print("It will also show you the amount of heads and tails.")
input("\n\nPress enter to flip a coin a hundred times.")

# Initial values
coin = random.randint(1, 2)
count_tails = 0
count_heads = 0
flip = 0

# Flip the coin 100 times (loop)
while flip < 100:
    if coin == 1:
        count_tails += 1
        flip += 1
        coin = random.randint(1, 2)
        print("tails")
    elif coin == 2:
        count_heads += 1
        flip += 1
        coin = random.randint(1, 2)
        print("heads")
    else:
        print("error.")

print(f"\nTotal of {count_tails} tails and {count_heads} heads.")

input("\nPress enter to exit program.")
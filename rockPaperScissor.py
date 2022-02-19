# Inspired by "12 Beginner Python Projects - Coding Course" from FreeCodeCamp.
# Added input validation, games keeps replaying untill user types 'exit' (loop) &
# displays computer's pick to the player.

import random
import pyinputplus as pyip

def play():
    global user
    global computer
    print("Make your choice: 'r' for rock, 'p' for paper and 's' for scissors:")
    user = pyip.inputRegex(r'(r|p|s|exit)')
    computer = random.choice(['r','p','s'])

    if user == "exit":
        return "Thank you so much for playing!"

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You Won!"

    return "You lost!"

def is_win(player,opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
       or (player == "p" and opponent == "r"):
        return True

print("Welcome to 'Rock, Paper, Scissors!'")
print("You can quit anytime by typing 'exit'.\n")

user = ""
while True:
    print(play())
    if user == "exit":
        break
    if computer == 'r':
        print("The computer picked 'rock'.")
    if computer == 'p':
        print("The computer picked paper.")
    if computer == 's':
        print("The computer picked 'scissors'.")

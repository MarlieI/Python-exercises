# challenge 4, chapter 4 python for the absolute beginner
# computer picks a random word, which player has to guess
# the computer tells how many letters the word has
# then the player gets five chances to ask if a letter is in the word
# the  computer can only answer with 'yes' or 'no'
# then the player must guess the word

# import random module
import random

# tuple of words from which the computer is randomly going to select from
WORDS = ("television", "python", "radio", "baby", "computer", "buffy", "console", "banana")

# the computer picks a random word
word = random.choice(WORDS)

# welcome message
print("Welcome to the 'random word game'!")

print("\nThe computer picks a word and tells you the amount of letters it has.")
print("You get five chances to ask the computer if a certain letter is in the word.")
print("After that, you have ONE chance to guess the word.")
print("Good luck!")

input("\nPress the enter key to continue.\n")

# the amount of letters in the word gets displayed to the player
print(f"The word has {len(word)} letters.")

# the player has five chances to ask the computer whether a certain letter is in the word
for i in range(5):
    letter = input("Which letter do you want to check out if it's in the word or not?: ")
    if letter == "":
        print("You didn't type anything and lost a chance...")
    elif letter in word:
        print("Yes.")
    elif letter not in word:
        print("No.")

# the player has one chance to guess the word
guess = input("What is the word?: ")
if guess == word:
    print("\nYou guessed the right word! Congratulations, you won!")
else:
    print("\nYou lost. Better luck next time!")
    print(f"The correct word was '{word}'.")

input("\nPress the enter key to exit the program.")

# Challenge 3, chapter 4 python for the absolute beginner
# Word Jumble
# The computer picks a random word and then "jumbles" it
# The user has to guess the original word
# the user can ask for a hint
# The player had five chances

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

# each word has a hint
python = "Best programming language"
jumble = "Best programming language"
easy = "the opposite of 'difficult'."
difficult = "The opposite of 'easy'."
answer = "You ask, I..."
xylophone = "An instrument"

# pick one word randomly from the sequence
word = random.choice(WORDS)

# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
        Welcome to Word Jumble!

    Unscramble the letters to make a word.
    (Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

# each time the user asks for a hint or guesses the wrong number he loses a point.
# the user loses if she total score hits zero
# the score is five at the beginning, because the user has five chances
score = 5
print("\nYou have 5 chances to get it right. Good luck!")
print("Type 'hint' for a, you guessed it, hint")
guess = input("\nYour guess: ")
while guess != correct and guess != "" or guess == "hint":
    if guess == "hint":
        if correct == "python":
            print(python)
        elif correct == "jumble":
            print(jumble)
        elif correct == "easy":
            print(easy)
        elif correct == "difficult":
            print(difficult)
        elif correct == "answer":
            print(answer)
        elif correct == "xylophone":
            print(xylophone)
    print("Sorry, that's not it.")
    score -= 1
    print("score:", score)
    if score == 0:
        break
    guess = input("Your guess: ")

if guess == correct:
    print("\nThat's it! You guessed it!")

if score == 0:
    print("\nYou have 0 points left, you lost.")

elif score == 5:
    print("Wow, you guessed it right the first time!")

print("\nThanks for playing.")

input("\n\nPress the enter key to exit.")
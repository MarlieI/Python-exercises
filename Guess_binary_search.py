# user picks number between 1 and 100
# program has to guess the number by using binary search
# user tells program to guess higher or lower

# initial values
tries = 0
number = 0
min_num = 1
max_num = 100
hint = ""

print("The PC has to guess your number.")

# user picks a number between 1 and 100
while number < 1 or number > 100:
    try:
        number = int(input("Pick a number between 1 and 100:"))
    except ValueError:
        print("Please give a valid number.")
        continue
    else:
        continue

input("Let the guessing game begin.\n")

# program has to guess
guess = ""
while guess != number:
    tries += 1
    guess = (min_num + max_num)//2
    print(f"PC: is it number {guess}?")
    if guess == number:
        print(f"\nThe pc guessed the right number ({guess}), in {tries} tries")
        input("Press enter to exit the program.")

    
# program asks user to go higher or lower
    while guess != number:
        hint = input("Higher or lower?:")
        if hint.lower() not in ("higher", "lower"):
            print("Please correct spelling.")
        else:
            break
# program adjusts binary search
    if hint.lower() == "higher":
        print(f"You told the pc to guess {hint}.")
        min_num = guess + 1
    elif hint.lower() == "lower":
        print(f"You told the pc to guess {hint}.")
        max_num = guess - 1
    else:
        print("\nUnexpected error.")

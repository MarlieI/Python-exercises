print("This program explores the 'Collatz sequence'")
print("It will divide the current number by two if it is even and multiply it with three and add one if it is odd.")
print("It will stop if the function returns a value of 1.\n")


def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1
    else:
        print('Error.')


# input validation
pick = None
while not pick:
    print('Pick a number: ')
    try:
        pick = int(input())
    except ValueError:
        print('Please enter an integer: ')

while pick != 1:
    pick = (collatz(pick))
    print(pick)

input('Press the enter key to exit.')

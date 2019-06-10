# Challenge 1, chapter 4 python for the absolute beginner
# This program counts for the user.
# The user enters the starting number, ending number and the amount by which to count.

print("Welcome to the counting program.")

start = int(input("\nPlease choose the starting number: "))
end = int(input("Please choose the ending number: "))
step = int(input("Finally, please choose the amount by which to count: "))

print("\nYou have chosen the following numbers:")
print("Start:", start, "," " End:", end, ",", "Amount:", step, ".")

input("\nPress enter to start counting.")

# loop that prints out the numbers one by one until it reaches the end number
for count in range(start, end + 1, step):
    print(count)

input("\nPress the enter key to exit the program.")
# Challenge 2, chapter 4 python for the absolute beginner
# User inputs message
# Message gets printed backwards

print("Welcome! Choose a message you want to get printed backwards.")

# User inputs message
message = input("\nType your message: ")

# In order to print the word backwards, start and end position is needed
# To make sure the final character gets printed negative 9 has to become negative 10.
high = len(message)
low = (-len(message)-1)

# Prints the message backwards by counting backwards from the last position
# to the beginning position with -1
# This tells the function to go from the start point to the end point by adding -1 each time.
print(message[high:low:-1])

input("Press the enter key to exit.")




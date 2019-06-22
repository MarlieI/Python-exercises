# challenge 3, chapter 5 python for the absolute beginner
# this program let's the user enter the name of a male and produces the name of his father
# the user can add, replace, and delete son-father pairs
# dictionaries

# welcome
print("\t\t\tWelcome to the 'Who's Your Daddy''program.")
print("\t\t\tPlease write both the first and last name with a capital letter. ")
print("\t\t\tFor example: Ben Stiller.")

# father-son pair
father_son = {"Jaden Smith" :"Will Smith",
              "Ben Stiller": "Jerry Stiller",
              "Brooklyn Beckham": " David Beckham",
              "Charlie Sheen": "Martin Sheen",
              "Colin Hanks": "Tom Hanks",
              "Kiefer Sutherland": "Donald Sutherland",
              }
# loop
choice = None
while choice != "0":
    print(
    '''
                Choose an option:
                0 - Quit
                1 - Who's your daddy?
                2 - Add son-father pair
                3 - Replace the daddy
                4 - Delete son-father pair
    ''')
    choice = input("Choice: ")
    # 0 - quit the game
    if choice == "0":
        print("Thank you for playing 'Who's Your Daddy'.")
    #  1 - look up the father
    elif choice == "1":
        son = input("Type the name of a male who's daddy you want to find: ")
        if son in father_son:
            father = father_son[son]
            print("His daddy is:", father)
        else:
            print("Sorry, he doesn't have a daddy.")
    # 2 - add a new son-father pair
    elif choice == "2":
        son = input("The name of the son: ")
        if son not in father_son:
            father = input("The name of the father: ")
            father_son[son] = father
            print("You've added", son, "and his father", father)
        else:
            print("He's already in our database.")
    # 3 - replace the father
    elif choice == "3":
        son = input("Which son needs a new daddy? ")
        if son in father_son:
            father = input("Who's the real daddy? ")
            father_son[son] = father
            print(son, "his real daddy is", father)
        else:
            print("This male isn't a part of our database (yet).")
    # 4 - delete a father-son pair
    elif choice == "4":
        son = input("Which son doesn't have a father? ")
        if son in father_son:
            father = father_son[son]
            del father_son[son]
            print("Alright,", son, "and his father", father, "are deleted from our database.")
        else:
            print("The son isn't part of our database (yet).")
    # unknown choice
    else:
        print("\nInvalid choice, choose either 0,1,2,3 or 4.")

input("\n\nPress the enter key to exit.")
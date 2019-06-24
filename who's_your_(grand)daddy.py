# challenge 4, chapter 5 python for the absolute beginner
# this program let's the user enter the name of a male and produces the name of his (grand)father
# the user can add, replace, and delete son-father-grandfather pairs
# dictionaries

# welcome
print("\t\t\tWelcome to the 'Who's Your Daddy''program.")
print("\t\t\tPlease write both the first and last name with a capital letter. ")
print("\t\t\tFor example: Ben Stiller.")

# father-son_granddad pairs
father_son_granddad = {"Jaden Smith" : ["Will Smith", "Willard  Smith"],
              "Ben Stiller": ["Jerry Stiller", "William Stiller"],
              "Brooklyn Beckham": ["David Beckham", " Alan Beckham"],
              "Charlie Sheen": ["Martin Sheen", "Francisco Estévez"],
              "Colin Hanks": ["Tom Hanks", "Amos Hanks"],
              "Kiefer Sutherland": ["Donald Sutherland", "Frederick McLea Sutherland"],
              }
# loop
choice = None
while choice != "0":
    print(
    '''
                Choose an option:
                0 - Quit
                1 - Who's your daddy?
                2 - Who's your granddaddy?
                3 - Add son-father-grandfather pair
                4 - Replace the daddy
                5 - Replace the granddaddy
                6 - Delete son-father-grandfather pair
                7 - Show all the sons
    ''')
    choice = input("Choice: ")
    # 0 - quit the game
    if choice == "0":
        print("Thank you for playing 'Who's Your Daddy'.")
    #  1 - show the father
    elif choice == "1":
        son = input("Type the name of a male who's daddy you want to find: ")
        if son in father_son_granddad:
            father = father_son_granddad[son][0]
            print("His daddy is:", father)
        else:
            print("Sorry, he doesn't have a daddy.")
    #  2 - show the grandfather
    elif choice == "2":
        son = input("Type the name of a male who's granddaddy you want to find: ")
        if son in father_son_granddad:
            grandfather = father_son_granddad[son][1]
            print(son, "his grandfather is", grandfather)
    # 3 - add a new son-father-grandfather pair
    elif choice == "3":
        son = input("The name of the son: ")
        if son not in father_son_granddad:
            father = input("The name of the father: ")
            grandfather = input("The name of the grandfather: ")
            father_son_granddad[son] = [father, grandfather]
            print("You've added,", son, " his father", father, "and his grandfather", grandfather)
        else:
            print("He's already in our database.")
    # 4 - replace the father
    elif choice == "4":
        son = input("Which son needs a new daddy? ")
        if son in father_son_granddad:
            father = input("Who's the real daddy? ")
            father_son_granddad[son][0] = father
            print(son, "his real daddy is", father)
        else:
            print("This male isn't a part of our database (yet).")
    # 5 - replace the granddaddy
    elif choice == "5":
        son = input("Enter the name of the son: ")
        if son in father_son_granddad:
            grandfather = input("Who is the new grandfather? ")
            father_son_granddad[son][1] = grandfather
            print(son, "his new grandfather is", grandfather)
    # 6 - delete a father-son pair
    elif choice == "6":
        son = input("Enter the name of the son: ")
        if son in father_son_granddad:
            father = father_son_granddad[son][0]
            grandfather = father_son_granddad[son][1]
            del father_son_granddad[son]
            print("Alright,", son, ", his father", father, "and his grandfather", grandfather,
                  "are deleted from our database.")
        else:
            print("The son isn't part of our database (yet).")
    # 7 - show sons
    elif choice == "7":
        print(father_son_granddad.keys())
    # unknown choice
    else:
        print("\nInvalid choice, choose either 0,1,2,3 or 4.")

input("\n\nPress the enter key to exit.")
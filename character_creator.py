# challenge 2, chapter 5 python for the absolute beginner
# character Creator Program for a role-playing game
# player is given a pool of 30 points to spend on four attributes (strength, health, wisdom and dexterity)
# player can spend and take points from an attribute and put them back into pool

# initial values
choice = None
pool = 30
strength = ["STRENGTH", 0]
health = ["HEALTH", 0]
wisdom = ["WISDOM", 0]
dexterity = ["DEXTERITY", 0]

# intro screen
print(
'''
         , ; ,   .-'"""'-.   , ; ,
          \\|/  .'         '.  \|//
           \-;-/   ()   ()   \-;-/
           // ;               ; \\
          //__; :.         .; ;__\\
         `-----\'.'-.....-'.'/-----'
                '.'.-.-,_.'.'
        jgs       '(  (..-'
                    '-'
''')
# menu
# user must choose to either quit or add/remove points
# loops end if all 30 point have been spend and user chooses 0
while choice != "0":
    print(
        f'''
           Make your own character:
            0 - Exit character creation
            1 - Add points to attribute
            2 - Remove points from attribute

            Total points left: {pool}
            {strength}
            {health}
            {wisdom}
            {dexterity} 
        '''
    )
    choice = input("Choice: ")

    # faulty exit, user must have used all 30 points
    if choice == "0":
        if pool > 0:
            print(f"You still have {pool} points left.")
            choice = None
        elif pool < 0:
            print(f"You should have 0 points left.")
            choice = None

    # add points
    elif choice == "1":
        option = input("choose an attribute: ")
        option = option.upper()
        points = int(input("How many points would you like to add? "))
        if option == "STRENGTH":
            strength[1] += points
            pool -= points
            print("\n", strength)
        elif option == "HEALTH":
            health[1] += points
            pool -= points
            print("\n", health)
        elif option == "WISDOM":
            wisdom[1] += points
            pool -= points
            print("\n", wisdom)
        elif option == "DEXTERITY":
            dexterity[1] += points
            pool -= points
            print("\n", dexterity)
        else:
            print("Invalid choice, pick one of the attributes or check the spelling.")

    # remove points
    elif choice == "2":
        option = input("Choose an attribute: ")
        option = option.upper()
        points = int(input("How many points would you like to remove? "))
        if option == "STRENGTH":
            strength[1] -= points
            pool += points
            print("\n", strength)
        elif option == "HEALTH":
            health[1] -= points
            pool += points
            print("\n", health)
        elif option == "WISDOM":
            wisdom[1] -= points
            pool += points
            print("\n", wisdom)
        elif option == "DEXTERITY":
            dexterity[1] -= points
            pool += points
            print("\n", dexterity)
        else:
            print("Invalid choice, pick one of the attributes or check the spelling.")
    else:
        print("Invalid choice. Pick either 0,1 or 2.")

print("Thank you for making your character.")
# Automate the boring stuff, chapter 5 (3rd edition)
# Comma code
# Write a function that takes a list value as an argument
# and returns a string with all the items separated by
# a comma and a space, with and inserted before the last item.

def comma_list(change_list):
    if not change_list:
        print('The list is empty.')
    for i in range(len(change_list)):
        if change_list[i] == change_list[-1] and len(change_list) != 1:
            print('and ' + change_list[i] + '.')
        elif len(change_list) == 1:
            print(change_list[i])
        else:
            print(change_list[i], end=', ')
          
spam = ['apples', 'bananas', 'tofu', 'cats']
comma_list(spam)


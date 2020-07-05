def print_table(inputList):
    # initialize the list "colWidths" with zeroes equal to the length of the input list
    colWidths = [0] * len(inputList)
    # iterate over the input list to find the longest word in each inner list
    for i in range(len(inputList)):
        length = []
        for p in inputList[i]:
            length.append(len(p))
        length.sort(reverse=True)
        colWidths[i] = length[0]
        #  print(length)
        #  print(colWidths)

    # assuming each inner list is the same length as the first, iterate over the input list
    # printing the x value from each inner list, right justified to its corresponding value in colWidths
    for x in range(len(inputList[0])):
        for y in range(len(inputList)):
            print(inputList[y][x].rjust(colWidths[y]), end=' ')
        print('')


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(tableData)

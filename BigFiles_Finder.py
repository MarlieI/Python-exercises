#! python3

import os
import time
import pyinputplus as pyip

start = time.time()
path = os.getcwd()

print('\tWelcome to the Big File Finder!')

print('\n\tThis program will give an overview of files starting from a certain size.')
print('\tThe filename with its size and location will be displayed to the user.')
print('\tWith the help of this list, the user can remove their choice of files.')

print('\n\tDrop this program in the folder you want to start the search from.')
print('\tStarting from the current working directory, this program will walk a directory tree.')
print('\tThe current working directory is ' + path + '.')
print('\tIf the current path is not the right one, please 1) exit \
2) drop the program in the right folder 3) restart and check again.')


extension = input('\n\tPlease choose a file extension (press enter if you want to search for all file types): ')
if extension == None:
    extension = ''
filesize = pyip.inputInt(prompt='\tPlease choose a minimum file size (MB): ', min=0)
convert = 1000000

print('\n\tSearching...\n')

for folderName, subfolders, filenames in os.walk(path):
    for filename in filenames:
        try:
            if os.path.getsize(folderName + '\\' + filename) >= (filesize * convert) and filename.endswith(extension):
                print('\t' + filename + ' has a size of ' + str((os.path.getsize(folderName + '\\' + filename))/convert) + 'MB and was found in ' + folderName)
        except OSError:
            print('Could not access this folder: ' + folderName + '\\' + filename) # moet gelogged worden
            continue
        
end = time.time()
print('\n\tFINISHED.')
print('\n\tThis process took ' + (str(end - start)[:4]) + ' seconds in total.')
input('\n\tPlease press enter to close the program.')

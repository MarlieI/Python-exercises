import os
import time
import pyinputplus as pyip
import send2trash

os.system('color C')
start = time.time()
path = os.getcwd()

print('Welcome to the \'Big File Finder & Deleter\'!')

print('\nThis program will give an overview of files starting from a certain size.')
print('The filename with its size and location will be displayed to the user.')
print('With the help of this list, the user can remove their choice of files.')

print('\nDrop this program in the folder you want to start the search from.')
print('Starting from the current working directory, this program will walk a directory tree.')

print('\nThe current working directory is ' + path + '.')
print('If the current path is not the right one, please:')
print('1) Exit. \n2) Drop the program in the right folder. \n3) Restart and check again.')
print('____________________________')

extension = input('\nPlease choose a file extension (just press enter if you want to search for all file types): ')
if extension == None:
    extension = ''
filesize = pyip.inputInt(prompt='Please choose a minimum file size (MB): ', min=0)
convert = 1000000

print('\nSearching...\n')

results = []
index = 0
for folderName, subfolders, filenames in os.walk(path):
    for filename in filenames:
        try:
            if os.path.getsize(folderName + '\\' + filename) >= (filesize * convert) and filename.endswith(extension):
                index += 1
                print(str(index) + ') ' + filename + ' has a size of ' + str((os.path.getsize(folderName + '\\' + filename))/convert)[:7] + ' MB and was found in ' + folderName)
                addFile = folderName + '\\' + filename
                results.append(addFile)
        except OSError:
            print('Could not access this folder: ' + folderName + '\\' + filename) # moet gelogged worden
            continue
        
end = time.time()
if results == []:
    print('\nNo files were found.')
print('\nFinished searching. This process took ' + (str(end - start)[:4]) + ' seconds in total.')
print('____________________________')

if results:
    print('\n- Type \'exit\' and press enter to close the program.')
    print('- Type \'overview\' and press enter to see which files have been removed and how much MB\s you have deleted.')


deletedFiles = []
totalSize = 0
# let user pick a file to delete and ask for conformation before actually sending the file to the Recycle Bin.
while results:
    index = pyip.inputNum('\nWhich file would you like to delete? Please pick a number: ', min=0, lessThan=len(results)+1, allowRegexes=[r'exit','overview'])
    if index == 'exit':
        break
    elif index == 'overview':
        print('A total of ' + str(totalSize)[:9] + ' MB has been deleted.')
        if deletedFiles:
            print('You have deleted the following files: ' + ', '.join(deletedFiles))
        continue
    confirm = pyip.inputYesNo('Are you sure you want to delete ' + results[index-1] + '? ')
    if confirm == 'yes':
        try:
            deletedFiles.append(results[index-1])
            totalSize += os.path.getsize(results[index-1])/convert
            send2trash.send2trash(results[index-1])
            print(results[index-1] + ' has been deleted.')
        except FileNotFoundError:
            print('This file has already been deleted!')
    else:
        continue

input('\nThank you for using the \'Big File Finder & Deleter\'!')

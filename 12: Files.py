import os

with open('12: Files.txt', 'w+') as f:  # syntax to open and write to a file
    f.write(
        'Hello this is a text file\n'
        'this is the second line\n'
        'this is the third line\n'
        'this is the fourth line'
    )
    f.seek(0)  # resets the cursor back to the beginning of the file
    print(f.read())
    f.seek(0)
    print(f.readlines())  # returns each separate line in a list
    f.close()  # closes the document
print(os.getcwd())  # syntax to print current working directory

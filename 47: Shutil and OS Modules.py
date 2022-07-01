import os
import shutil
import send2trash

f = open('practice.txt', 'w+')
f.write('This is a test string')
f.close()
print(os.getcwd())  # gets your current working directory
print(os.listdir('/Users/mac/Desktop'))  # lists everything in the current working directory or the directory provided.
print(shutil.move('/Users/mac/Desktop/Python Bootcamp/practice.txt', '/Users/mac/Desktop'))
print(send2trash.send2trash('/Users/mac/Desktop/practice.txt'))

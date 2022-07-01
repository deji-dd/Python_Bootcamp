# import shutil
# import send2trash
import os
import re

# shutil.unpack_archive('unzip_me_for_instructions.zip', 'dir1', 'zip')
# send2trash.send2trash('unzip_me_for_instructions.zip')
# send2trash.send2trash('dir1')
f = open('extracted_content/Instructions.txt', 'r')
# for x in f.readlines():
#    print(f'{x}\n')
f.close()
for root, dirs, files in os.walk('extracted_content', True):
    #    print(root)
    #    print(dirs)
    #    print(files)
    #    print('\n')
    for x in files:
        file = open(f'{root}/{x}', 'r')
        lin = file.readlines()
        str1 = ' '
        result = str1.join(lin)
        for y in re.findall(r'\d{3}-\d{3}-\d{4}', result):
            print(y)
        file.close()

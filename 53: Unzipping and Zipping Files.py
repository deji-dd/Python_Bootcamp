import zipfile
import shutil

f = open('file1.txt', 'w+')
f.write('one file')
f.close()
f = open('file2.txt', 'w+')
f.write('two file')
f.close()
comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()
zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extracted_content')
dir_to_zip = '/Users/mac/Desktop/Python Bootcamp/extracted_content'
output = 'example'
shutil.make_archive(output, 'zip', dir_to_zip)
shutil.unpack_archive('example.zip', 'final_unzip', 'zip')

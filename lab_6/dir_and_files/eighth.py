# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os

path = '/Users/kenn_/my_file/Semester_2nd/lab_6/dir_and_files/sample_3.txt'

if os.path.exists(path):
    if os.access(path, os.F_OK) and os.access(path, os.R_OK) and os.access(path, os.W_OK):
        os.remove(path)
    else: 
        print('File is not accessible')
else:
    print('File does not exist')
    
# os.rmdir - removes a directory 
# os.remove - removes a files
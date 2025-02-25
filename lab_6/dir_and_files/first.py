# Write a Python program to list only directories, files and all directories, files in a specified path.

# if the file and the terminal are located in different places, getcwd() returns the path of the terminal that we're running on

import os

path = '/Users/kenn_/my_file/Semester_2nd/lab_6'

my_list = os.listdir(path)

print('Only directories: ')

# for element in my_list:
#     if os.path.isdir(element): # this way os.path.isdir() checks elements that are in cwd, not in the specified path ('/Users/kenn_/my_file/Semester_2nd/lab_6)
#         print(element)         # but we need, '/Users/kenn_/my_file/Semester_2nd/lab_6/element'


# we have to join the 'path' and the 'element' inside this path

for element in my_list:
    full_path = os.path.join(path, element)
    if os.path.isdir(full_path):
        print(element)

print('-----------------------')

print('Only files: ')

for element in my_list:
    full_path = os.path.join(path, element)
    if os.path.isfile(full_path):
        print(element)

# If your terminal is in '/Users/kenn_/my_file/semester_2nd/lab_6/dir_and_files'
# This means that os.path.isdir(element) is checking inside '/Users/kenn_/my_file/semester_2nd/lab_6/dir_and_files' instead of /Users/kenn_/my_file/Semester_2nd/lab_6


print('-----------------------')

print('Directories and files: ')

for element in my_list: 
    print(element)


import os

path = os.getcwd() # current working directory 

# cwd is the folder, where the terminal is currently open, i.e, the cwd of the terminal

print(path)

x = os.listdir(path)

for element in x:
    print(element)

# if I'll be in the file 'Semester_2nd', I'll get as a result: 
# .DS_Store
# lab_6
# lab_1
# lab_4
# lab_3
# lab_2
# lab_5
# .git

print('------------------')

# Checking if an element is a file or a folder

for element in x:
    print('Name', element)
    print('Is a file:', os.path.isfile(element))
    print('Is a folder:', os.path.isdir(element))
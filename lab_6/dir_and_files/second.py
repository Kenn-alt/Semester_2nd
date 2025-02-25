# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

import os

path = '/Users/kenn_/my_file/Semester_2nd/lab_6/sample.py'

print(os.access(path, os.F_OK)) # existence
print(os.access(path, os.R_OK)) # readability 
print(os.access(path, os.W_OK)) # writability
print(os.access(path, os.X_OK)) # executability 

